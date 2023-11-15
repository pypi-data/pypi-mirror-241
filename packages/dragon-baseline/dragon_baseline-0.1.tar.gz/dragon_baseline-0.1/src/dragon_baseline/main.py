#  Copyright 2022 Diagnostic Image Analysis Group, Radboudumc, Nijmegen, The Netherlands
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import subprocess
from pathlib import Path
from typing import List

import numpy as np
import pandas as pd
import torch
from scipy.special import expit, softmax
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import StandardScaler
from tqdm import tqdm
from transformers import (AutoModelForSequenceClassification,
                          AutoModelForTokenClassification, AutoTokenizer,
                          TokenClassificationPipeline)
from transformers.modeling_outputs import SequenceClassifierOutput

from dragon_baseline.architectures.clf_multi_head import \
    AutoModelForMultiHeadSequenceClassification
from dragon_baseline.architectures.ner_multi_head import \
    AutoModelForMultiHeadTokenClassification
from dragon_baseline.architectures.reg_multi_head import \
    AutoModelForMultiHeadSequenceRegression
from dragon_baseline.nlp_algorithm import NLPAlgorithm, ProblemType

__all__ = [
    # expose the algorithm classes
    "AutoModelForMultiHeadSequenceClassification",
    "AutoModelForMultiHeadTokenClassification",
    "AutoModelForMultiHeadSequenceRegression",
]

class CustomLogScaler(TransformerMixin, BaseEstimator):
    def __init__(self):
        self.standard_scaler = StandardScaler()

    def fit(self, X, y=None):
        # Apply log(1 + value) transformation
        log_X = np.log1p(X)

        # Fit the standard scaler
        self.standard_scaler.fit(log_X)
        return self

    def transform(self, X, y=None):
        # Apply log(1 + value) transformation
        log_X = np.log1p(X)

        # Transform using standard scaler
        return self.standard_scaler.transform(log_X)

    def inverse_transform(self, X):
        # Reverse the standard scaling
        inv_X = self.standard_scaler.inverse_transform(X)

        # Reverse the log(1 + value) transformation
        return np.expm1(inv_X)


class DragonBaseline(NLPAlgorithm):
    def __init__(self, input_path: Path = Path("/input"), output_path: Path = Path("/output"), workdir: Path = Path("/opt/app"), models_dir: Path = Path("/opt/app/models"), **kwargs):
        """
        Baseline implementation for the DRAGON Challenge (https://dragon.grand-challenge.org/).
        This baseline uses the HuggingFace Transformers library (https://huggingface.co/transformers/).

        The baseline must implement the following methods:
        - `preprocess`: preprocess the data
        - `train`: train the model
        - `predict`: predict the labels for the test data
        """
        super().__init__(input_path=input_path, output_path=output_path, **kwargs)

        # default training settings
        self.model_name = models_dir / "distilbert-base-multilingual-cased"
        self.per_device_train_batch_size = 4
        self.gradient_accumulation_steps = 2
        self.max_seq_length = 512
        self.learning_rate = 3e-5
        self.num_train_epochs = 5
        self.warmup_ratio = 0.1
        self.load_best_model_at_end = True
        self.metric_for_best_model = "loss"
        self.fp16 = True

        # paths for saving the preprocessed data and model checkpoints
        self.nlp_dataset_train_preprocessed_path = Path(workdir / "nlp-dataset-train-preprocessed.json")
        self.nlp_dataset_val_preprocessed_path = Path(workdir / "nlp-dataset-val-preprocessed.json")
        self.nlp_dataset_test_preprocessed_path = Path(workdir / "nlp-dataset-test-preprocessed.json")
        self.model_save_dir = Path(workdir / "checkpoints")

    def scale_labels(self) -> pd.DataFrame:
        """Scale the labels."""
        if self.task.target.problem_type in [ProblemType.SINGLE_LABEL_REGRESSION, ProblemType.MULTI_LABEL_REGRESSION]:
            if self.task.target.skew > 1:
                scaler = CustomLogScaler()
            else:
                scaler = StandardScaler()

            # fit the scaler on the training data
            scaler = scaler.fit(self.df_train[self.task.target.label_name].explode().values.astype(float).reshape(-1, 1))
            self.label_scalers[self.task.target.label_name] = scaler

            # scale the labels
            if self.task.target.problem_type == ProblemType.SINGLE_LABEL_REGRESSION:
                self.df_train[self.task.target.label_name] = scaler.transform(self.df_train[self.task.target.label_name].values.reshape(-1, 1))
                self.df_val[self.task.target.label_name] = scaler.transform(self.df_val[self.task.target.label_name].values.reshape(-1, 1))
            elif self.task.target.problem_type == ProblemType.MULTI_LABEL_REGRESSION:
                self.df_train[self.task.target.label_name] = self.df_train[self.task.target.label_name].apply(lambda x: np.ravel(scaler.transform(np.array(x).reshape(-1, 1))))
                self.df_val[self.task.target.label_name] = self.df_val[self.task.target.label_name].apply(lambda x: np.ravel(scaler.transform(np.array(x).reshape(-1, 1))))

    def unscale_predictions(self, predictions: pd.DataFrame) -> pd.DataFrame:
        """Unscale the predictions."""
        if self.task.target.problem_type in [ProblemType.SINGLE_LABEL_REGRESSION, ProblemType.MULTI_LABEL_REGRESSION]:
            scaler = self.label_scalers[self.task.target.label_name]
            if self.task.target.problem_type == ProblemType.SINGLE_LABEL_REGRESSION:
                predictions[self.task.target.prediction_name] = scaler.inverse_transform(predictions[self.task.target.prediction_name].values.reshape(-1, 1))
            elif self.task.target.problem_type == ProblemType.MULTI_LABEL_REGRESSION:
                predictions[self.task.target.prediction_name] = predictions[self.task.target.prediction_name].apply(lambda x: np.ravel(scaler.inverse_transform(np.array(x).reshape(-1, 1))))
        return predictions

    def add_dummy_test_labels(self):
        """Add dummy labels for test data. This allows to use the dataset in the huggingface pipeline."""
        if self.task.target.problem_type in [ProblemType.SINGLE_LABEL_NER, ProblemType.MULTI_LABEL_BINARY_NER]:
            dummy_label = self.df_train[self.task.target.label_name].iloc[0][0]
            self.df_test[self.task.target.label_name] = self.df_test.apply(lambda row: [dummy_label]*len(row[self.task.input_name]), axis=1)
        else:
            dummy_label = self.df_train[self.task.target.label_name].iloc[0]
            self.df_test[self.task.target.label_name] = [dummy_label]*len(self.df_test)

    def prepare_labels(self):
        """
        Prepare labels for training in the HuggingFace pipeline.

        For multi-label binary classification tasks, convert the list of 0/1 ints to list of "labelX" strings.
        For other multi-label tasks, convert the multiple values in the label column to one value per column.
        """
        if self.task.target.problem_type == ProblemType.MULTI_LABEL_BINARY_CLASSIFICATION:
            for df in [self.df_train, self.df_val, self.df_test]:
                # convert list of 0/1 ints to list of "labelX" strings
                df[self.task.target.label_name] = df[self.task.target.label_name].apply(lambda labels: [
                    f"label{i}" for i, lbl in enumerate(labels) if lbl == 1
                ])
            # set the possible values (exclude NaN, which we get from `.explode()` for empty lists)
            self.task.target.values = sorted([lbl for lbl in self.df_train[self.task.target.label_name].explode().unique() if isinstance(lbl, str)])
        elif self.task.target.problem_type in [
            ProblemType.MULTI_LABEL_REGRESSION,
            ProblemType.MULTI_LABEL_MULTI_CLASS_CLASSIFICATION,
        ]:
            num_labels = len(self.df_train[self.task.target.label_name].iloc[0])
            for df in [self.df_train, self.df_val, self.df_test]:
                for i in range(num_labels):
                    df[f"{self.task.target.label_name}_{i}"] = df[self.task.target.label_name].apply(lambda x: x[i])

    def shuffle_train_data(self):
        """Shuffle the training data."""
        self.df_train = self.df_train.sample(frac=1, random_state=self.task.jobid)

    def preprocess(self):
        """Preprocess the data."""
        # scale the labels
        self.scale_labels()
        self.add_dummy_test_labels()
        self.prepare_labels()
        self.shuffle_train_data()

    def train(self):
        """Train the model."""
        # save the preprocessed data for training through command line interface of the HuggingFace library
        for path in [
            self.nlp_dataset_train_preprocessed_path,
            self.nlp_dataset_val_preprocessed_path,
            self.nlp_dataset_test_preprocessed_path,
        ]:
            path.parent.mkdir(parents=True, exist_ok=True)
        self.df_train.to_json(self.nlp_dataset_train_preprocessed_path, orient="records")
        self.df_val.to_json(self.nlp_dataset_val_preprocessed_path, orient="records")
        self.df_test.to_json(self.nlp_dataset_test_preprocessed_path, orient="records")

        # load the tokenizer
        tokenizer = AutoTokenizer.from_pretrained(self.model_name, truncation_side=self.task.recommended_truncation_side)

        # train the model
        if self.task.target.problem_type == ProblemType.SINGLE_LABEL_NER:
            trainer = "ner"
        elif self.task.target.problem_type == ProblemType.MULTI_LABEL_BINARY_NER:
            trainer = "multi_label_ner"
        elif self.task.target.problem_type in [ProblemType.MULTI_LABEL_REGRESSION, ProblemType.MULTI_LABEL_MULTI_CLASS_CLASSIFICATION]:
            trainer = "multi_label_classification"
        else:
            trainer = "classification"

        cmd = [
            "python", "-m", "dragon_baseline",
            trainer,
            "--do_train",
            "--do_eval",
            "--do_predict",
            "--learning_rate", self.learning_rate,
            "--model_name_or_path", self.model_name,
            "--ignore_mismatched_sizes",
            "--num_train_epochs", self.num_train_epochs,
            "--warmup_ratio", self.warmup_ratio,
            "--max_seq_length", self.max_seq_length,
            "--truncation_side", self.task.recommended_truncation_side,
            "--load_best_model_at_end", self.load_best_model_at_end,
            "--save_strategy", "epoch",
            "--evaluation_strategy", "epoch",
            "--per_device_train_batch_size", self.per_device_train_batch_size,
            "--gradient_accumulation_steps", self.gradient_accumulation_steps,
            "--train_file", self.nlp_dataset_train_preprocessed_path,
            "--validation_file", self.nlp_dataset_val_preprocessed_path,
            "--test_file", self.nlp_dataset_test_preprocessed_path,
            "--output_dir", self.model_save_dir,
            "--overwrite_output_dir",
            "--save_total_limit", "2",
            "--seed", self.task.jobid,
            "--report_to", "none",
            "--text_column_name" + ("s" if not "ner" in trainer else ""), self.task.input_name,
            "--remove_columns", "uid",
        ]
        if self.task.target.problem_type in [
            ProblemType.MULTI_LABEL_REGRESSION,
            ProblemType.MULTI_LABEL_MULTI_CLASS_CLASSIFICATION,
        ]:
            label_names = [col for col in self.df_train.columns if col.startswith(f"{self.task.target.label_name}_")]
            cmd.extend([
                "--label_column_names", ",".join(label_names),
            ])
        else:
            cmd.extend([
                "--label_column_name", self.task.target.label_name,
            ])
        if not self.task.target.problem_type in [ProblemType.SINGLE_LABEL_NER, ProblemType.MULTI_LABEL_BINARY_NER]:
            cmd.extend([
                "--text_column_delimiter", tokenizer.sep_token,
            ])
        if self.metric_for_best_model is not None:
            cmd.extend([
                "--metric_for_best_model", str(self.metric_for_best_model),
            ])
        if self.fp16:
            cmd.append("--fp16")

        cmd = [str(arg) for arg in cmd]
        print("Training command:")
        print(" ".join(cmd))
        subprocess.check_call(cmd)

    def predict_ner(self, *, df: pd.DataFrame) -> pd.DataFrame:
        """Predict the labels for the test data.

        The pipeline below returns a list of dictionaries, one for each entity. An example is shown below:
        result = [
            {'entity_group': 'SYMPTOM', 'score': 0.25475845, 'word': 'persistent cough', 'start': 22, 'end': 38},
            {'entity_group': 'DIAGNOSIS', 'score': 0.49139544, 'word': 'likely viral infection', 'start': 39, 'end': 61},
        ]

        We convert this to a list of labels, one for each word. An example is shown below:
        prediction = [B-SYMPTOM, I-SYMPTOM, B-DIAGNOSIS, I-DIAGNOSIS, I-DIAGNOSIS]
        """
        tokenizer = AutoTokenizer.from_pretrained(self.model_save_dir, truncation_side=self.task.recommended_truncation_side)
        model = AutoModelForTokenClassification.from_pretrained(self.model_save_dir)
        classifier = TokenClassificationPipeline(
            model=model,
            tokenizer=tokenizer,
            stride=tokenizer.model_max_length // 2,
            aggregation_strategy="first",
            device=self.device,
        )

        results = []
        for _, row in tqdm(df.iterrows(), desc="Predicting", total=len(df)):
            # predict
            inputs = row[self.task.input_name]
            text = " ".join(inputs)
            result = classifier(text)

            # convert to one label per word
            start, end = 0, 0
            prediction = []
            for word in inputs:
                end = start + len(word)
                found_match = False
                for entity_group in result:
                    if entity_group["start"] <= start <= entity_group["end"]:
                        if end > entity_group["end"]:
                            # Even with `aggregation_strategy="first"` a word can span multiple entities. This happens when
                            # the word is split into multiple tokens but not merged back by the `TokenClassificationPipeline`.
                            # This happens for example with dates, e.g. "01/01/2021". We take the prediction for the first part.
                            # Feel free to implement a better solution!
                            pass

                        BI_tag = "B" if start == entity_group["start"] else "I"
                        prediction.append(BI_tag + "-" + entity_group["entity_group"])
                        found_match = True
                        break

                if not found_match:
                    prediction.append("O")
                start = end + 1

            pred = {
                self.task.target.prediction_name: prediction
            }
            results.append({"uid": row["uid"], **pred})
        return pd.DataFrame(results)

    def predict_multi_label_binary_ner(self, *, df: pd.DataFrame) -> pd.DataFrame:
        """Predict the labels for the test data."""
        # load the model and tokenizer
        tokenizer = AutoTokenizer.from_pretrained(self.model_save_dir, truncation_side=self.task.recommended_truncation_side)
        model = AutoModelForMultiHeadTokenClassification.from_pretrained(self.model_save_dir).to(self.device)

        # predict
        results = []
        for _, row in tqdm(df.iterrows(), desc="Predicting", total=len(df)):
            # tokenize inputs
            inputs = row[self.task.input_name]
            tokenized_inputs = tokenizer(inputs, return_tensors="pt", truncation=True, is_split_into_words=True, padding=True).to(self.device)

            # predict
            result: SequenceClassifierOutput = model(**tokenized_inputs)
            logits: np.ndarray = result.logits.detach().cpu().numpy()

            # select the logits for the first token of each word and convert to probabilities
            predictions = []
            for batch_idx in range(len(logits)):
                word_ids = tokenized_inputs.word_ids(batch_index=batch_idx)
                previous_word_idx = None
                batch_predictions = []
                for token_idx, word_idx in enumerate(word_ids):
                    if word_idx is None:
                        # skip special tokens
                        continue

                    if word_idx == previous_word_idx:
                        # skip subwords
                        continue

                    p = expit(logits[batch_idx, token_idx])
                    batch_predictions.append(p)
                    previous_word_idx = word_idx
                predictions.append(batch_predictions)
            predictions = np.array(predictions)

            if predictions.shape[1] < len(inputs):
                # pad the predictions to the length of the inputs
                # note: feel free to implement a better solution! For example, using stride > 0 in the pipeline.
                predictions = np.pad(predictions, ((0, 0), (0, len(inputs) - predictions.shape[1]), (0, 0)), mode="constant", constant_values=0)

            # convert to labels
            expected_shape = (1, len(inputs), model.config.num_labels)
            if predictions.shape != expected_shape:
                raise ValueError(f"Expected predictions to have shape {expected_shape}, but got {predictions.shape}")

            prediction = {self.task.target.prediction_name: predictions[0]}
            results.append({"uid": row["uid"], **prediction})

        return pd.DataFrame(results)

    def predict_huggingface(self, *, df: pd.DataFrame) -> pd.DataFrame:
        """Predict the labels for the test data."""
        # load the model and tokenizer
        tokenizer = AutoTokenizer.from_pretrained(self.model_save_dir, truncation_side=self.task.recommended_truncation_side)
        if self.task.target.problem_type == ProblemType.MULTI_LABEL_REGRESSION:
            model = AutoModelForMultiHeadSequenceRegression.from_pretrained(self.model_save_dir).to(self.device)
        elif self.task.target.problem_type == ProblemType.MULTI_LABEL_MULTI_CLASS_CLASSIFICATION:
            model = AutoModelForMultiHeadSequenceClassification.from_pretrained(self.model_save_dir).to(self.device)
        else:
            model = AutoModelForSequenceClassification.from_pretrained(self.model_save_dir).to(self.device)

        # predict
        results = []
        for _, row in tqdm(df.iterrows(), desc="Predicting", total=len(df)):
            # tokenize inputs
            inputs = row[self.task.input_name] if self.task.input_name == "text_parts" else [row[self.task.input_name]]
            tokenized_inputs = tokenizer(*inputs, return_tensors="pt", truncation=True).to(self.device)

            # predict
            result: SequenceClassifierOutput = model(**tokenized_inputs)

            if self.task.target.problem_type == ProblemType.MULTI_LABEL_MULTI_CLASS_CLASSIFICATION:
                logits: List[np.ndarray] = [logits.detach().cpu().numpy() for logits in result.logits]
            else:
                logits: np.ndarray = result.logits.detach().cpu().numpy()

            # convert to labels
            if self.task.target.problem_type == ProblemType.SINGLE_LABEL_REGRESSION:
                expected_shape = (1, 1)
                if logits.shape != expected_shape:
                    raise ValueError(f"Expected logits to have shape {expected_shape}, but got {logits.shape}")

                prediction = {self.task.target.prediction_name: logits[0][0]}
            elif self.task.target.problem_type == ProblemType.MULTI_LABEL_REGRESSION:
                expected_shape = (1, len(self.df_train[self.task.target.label_name].iloc[0]))
                if logits.shape != expected_shape:
                    raise ValueError(f"Expected logits to have shape {expected_shape}, but got {logits.shape}")

                prediction = {self.task.target.prediction_name: logits[0]}
            elif self.task.target.problem_type == ProblemType.SINGLE_LABEL_BINARY_CLASSIFICATION:
                expected_shape = (1, 2)
                if logits.shape != expected_shape:
                    raise ValueError(f"Expected logits to have shape {expected_shape}, but got {logits.shape}")

                # calculate sigmoid to map the logits to [0, 1]
                prediction = softmax(logits, axis=-1)[0, 1]
                prediction = {self.task.target.prediction_name: prediction}
            elif self.task.target.problem_type == ProblemType.SINGLE_LABEL_MULTI_CLASS_CLASSIFICATION:
                expected_shape = (1, len(self.task.target.values))
                if logits.shape != expected_shape:
                    raise ValueError(f"Expected logits to have shape {expected_shape}, but got {logits.shape}")

                p = model.config.id2label[np.argmax(logits[0])]
                prediction = {self.task.target.prediction_name: p}
            elif self.task.target.problem_type == ProblemType.MULTI_LABEL_BINARY_CLASSIFICATION:
                expected_shape = (1, len(self.task.target.values))
                if logits.shape != expected_shape:
                    raise ValueError(f"Expected logits to have shape {expected_shape}, but got {logits.shape}")

                prediction = expit(logits)[0]  # calculate sigmoid to map the logits to [0, 1]
                prediction = {self.task.target.prediction_name: prediction}
            elif self.task.target.problem_type == ProblemType.MULTI_LABEL_MULTI_CLASS_CLASSIFICATION:
                expected_length = len(self.df_train[self.task.target.label_name].iloc[0])
                if len(logits) != expected_length:
                    raise ValueError(f"Expected logits to have length {expected_length}, but got {len(logits)}")
                label_names = [f"{self.task.target.label_name}_{i}" for i in range(len(logits))]
                for logits_, label_name in zip(logits, label_names):
                    expected_shape = (1, len(self.df_train[label_name].unique()))
                    if logits_.shape != expected_shape:
                        raise ValueError(f"Expected logits to have shape {expected_shape}, but got {logits_.shape}")

                preds = [np.argmax(p) for p in logits]
                prediction = {
                    self.task.target.prediction_name: [
                        id2label[str(p)]
                        for p, id2label in zip(preds, model.config.id2labels)
                    ]
                }
            else:
                raise ValueError(f"Unexpected problem type '{self.task.target.problem_type}'")

            results.append({"uid": row["uid"], **prediction})

        df_pred = pd.DataFrame(results)

        # scale the predictions (inverse of the normalization during preprocessing)
        df_pred = self.unscale_predictions(df_pred)

        return df_pred

    def predict(self, *, df: pd.DataFrame) -> pd.DataFrame:
        """Predict the labels for the test data."""
        with torch.no_grad():
            if self.task.target.problem_type == ProblemType.SINGLE_LABEL_NER:
                return self.predict_ner(df=df)
            elif self.task.target.problem_type == ProblemType.MULTI_LABEL_BINARY_NER:
                return self.predict_multi_label_binary_ner(df=df)
            else:
                return self.predict_huggingface(df=df)


if __name__ == "__main__":
    # Note: to debug (outside of Docker), you can set the input and output paths.
    # You probably need to change self.model_name too.
    for job_name in [
        "Task000_Example_clf-fold0",
        "Task001_Example_reg-fold0",
        "Task002_Example_mutli_reg-fold0",
        "Task003_Example_mednli-fold0",
        "Task004_Example_ner-fold0",
        "Task005_Example_multi_clf-fold0",
        "Task006_Example_binary_clf-fold0",
        "Task007_Example_multi_binary_clf-fold0",
        "Task008_Example_multi_ner-fold0",
    ]:
        DragonBaseline(
            input_path=Path(f"test-input/{job_name}"),
            output_path=Path(f"test-output/{job_name}"),
            workdir=Path(f"test-workdir/{job_name}"),
            models_dir=Path(f"test-workdir/models"),
        ).process()
