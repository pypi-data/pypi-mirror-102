from .o3iss import compute
from sklearn.base import BaseEstimator, ClassifierMixin, TransformerMixin
from sklearn.linear_model import RidgeClassifierCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import numpy as np
import multiprocessing as mp


class IssTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, level=4, n_jobs=None):
        self.level = level
        self.n_jobs = mp.cpu_count() if n_jobs == None else n_jobs

    def fit(self, X, y=None):
        self.n_jobs = (
            self.n_jobs
            if X.shape[1] >= self.level * self.n_jobs
            else max(X.shape[1] // self.level, 1)
        )
        return self

    def transform(self, X):
        if X.shape[1] <= self.level * self.n_jobs:
            sigs = [
                np.hstack(
                    [
                        np.hstack(
                            [
                                compute(sample_chunk, len(sample_chunk)),
                                np.zeros(2 ** self.level - 2 ** len(sample_chunk)),
                            ]
                        )
                        for sample_chunk in np.array_split(sample, self.n_jobs)
                    ]
                )
                for sample in X
            ]
        else:
            sigs = [
                np.hstack(
                    [
                        compute(sample_chunk, self.level)
                        for sample_chunk in np.array_split(sample, self.n_jobs)
                    ]
                )
                for sample in X
            ]
        return np.array(sigs)


class IssClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self, level=4, n_jobs=None):
        self.level = level
        self.n_jobs = n_jobs

    def fit(self, X, y):
        self.pipeline = Pipeline(
            [
                ("scale", StandardScaler()),
                ("iss", IssTransformer(level=self.level, n_jobs=self.n_jobs)),
                ("class", RidgeClassifierCV()),
            ]
        )
        return self.pipeline.fit(X, y)

    def predict(self, X):
        return self.pipeline.predict(X)
