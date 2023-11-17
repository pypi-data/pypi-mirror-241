"""
This module contains classes for comparing machine learning models and selecting the best one.
"""

from typing import List

import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV


class DataLoader:
    """
    A class for loading and splitting data.

    Attributes:
        X_train: Training feature data.
        y_train: Training target data.
        X_test: Test feature data.
        y_test: Test target data.
    """

    def __init__(self):
        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None

    def load(self, X, target, test_size=0.2, univariate=True, columns=None):
        """
        Load and split the data into training and test sets.

        Parameters:
            X (DataFrame): The input data.
            target (str): The target column name.
            test_size (float, optional): The proportion of data to include in the test split. Defaults to 0.2.
            univariate (bool, optional): Whether to use only one column. Defaults to True.
            columns (list, optional): A list of columns to select. Defaults to None.
        """
        self._check_dimensions(univariate, columns)
        _X = self._get_dimensions(X, columns)
        if test_size > 0:
            _X_train, _X_test = train_test_split(_X, test_size=test_size, random_state=42)
            _X_test, _y_test = self._split_target_feature(_X_test, target)
            self.X_test, self.y_test = _X_test, _y_test
        else:
            _X_train = _X
        _X_train, _y_train = self._split_target_feature(_X_train, target)

        self.X_train, self.y_train = _X_train, _y_train

    @staticmethod
    def _split_target_feature(X, feature):
        """Split the target feature from the input data."""

        X_train = X.drop(columns=[feature])
        y_train = X[feature]
        return X_train, y_train

    @staticmethod
    def _check_dimensions(univariate, columns):
        """Check if the dimensions of data are valid."""
        if columns is None:
            return True
        if len(columns) == 0:
            raise ValueError("Need one column minimum")
        if univariate and len(columns) > 1:
            raise TypeError("Univariate can't be True with more than one column")
        return True

    @staticmethod
    def _get_dimensions(X, columns):
        """Select specific columns from the input data."""
        return X[columns] if columns is not None else X


class ModelLoader:
    """
    A class for loading and fitting machine learning models.

    Attributes:
        model_name (str): The name of the model.
        model: The machine learning model.
        params (dict): Hyperparameters to tune.
        loader (DataLoader): DataLoader instance for loading data.
        n_jobs (int, optional): Number of CPU cores to use for parallel execution. Defaults to None.
        grid_model: GridSearchCV model for hyperparameter tuning.
    """

    def __init__(self, model, model_name, params, loader, n_jobs=None):
        self.model_name = model_name
        self.model = model
        self.params = params
        self.loader: DataLoader = loader
        self.n_jobs = n_jobs
        self.grid_model = None

    def fit(self, scoring, grid_search=True, cv=None):
        """
        Fit the machine learning model.

        Parameters:
            scoring (str, callable, list, tuple, or dict): Strategy to evaluate the performance of the model.
            grid_search (bool, optional): Whether to perform hyperparameter tuning using GridSearchCV. Defaults to True.
            cv (int, cross-validation generator, or iterable, optional): Cross-validation strategy. Defaults to None.
        """
        if grid_search:
            self.grid_model = GridSearchCV(self.model,
                                           self.params,
                                           scoring=scoring,
                                           cv=cv,
                                           n_jobs=self.n_jobs)
            self.grid_model.fit(self.loader.X_train, self.loader.y_train)
        else:
            raise ValueError("Model that are not GridSearchCV based can't be used right now")


class Estimator:
    """
    A class to represent a model estimator.

    Attributes:
        name (str): The name of the estimator.
        score: The evaluation score of the estimator.
        params (dict): The best hyperparameters of the estimator.
    """

    def __init__(self, name, score, loader, params=None, model=None):
        self.name = name
        self.score = score
        self.params = params
        self.model = model
        self.loader = loader


class ModelSelector:
    """
    A class for selecting the best machine learning model among multiple models.

    Attributes:
        models (List[ModelLoader]): List of ModelLoader instances representing different models.
        estimators: List of Estimator instances for each model.
        best_estimator: The best performing estimator among all models.
    """

    def __init__(self, models: List[ModelLoader]):
        self.models = models
        self.estimators = None
        self.best_estimator = None
        self.fit_params = None

    def apply(self, scoring, grid_search=False, cv=None):
        """
        Apply model selection and store the best estimator.

        Parameters:
            scoring (str, callable, list, tuple, or dict): Strategy to evaluate the performance of the model.
            grid_search (bool, optional): Whether to perform hyperparameter tuning using GridSearchCV. Defaults to False.
            cv (int, cross-validation generator, or iterable, optional): Cross-validation strategy. Defaults to None.
        """
        _estimators = []
        for model in self.models:
            model.fit(scoring=scoring, grid_search=grid_search, cv=cv)
            _estimators.append(Estimator(model.model_name,
                                         model.grid_model.best_score_,
                                         loader=model.loader,
                                         params=model.grid_model.best_params_)
                               )
        self.estimators = _estimators
        _best_estimator_name, _best_score, _data_loader, _best_params = self._compare()
        self.best_estimator = Estimator(_best_estimator_name,
                                        _best_score,
                                        loader=_data_loader,
                                        params=_best_params)
        self.fit_params = {
            "scoring": scoring,
            "grid_search": grid_search,
            "cv": cv
        }

    def _compare(self):
        """Compare the performance of different estimators and return the best one."""
        _best_score = None
        _best_estimator_name = None
        _best_params = None
        _data_loader = None
        for estimator in self.estimators:
            if _best_score is None:
                _best_score = estimator.score
                _best_estimator_name = estimator.name
                _best_params = estimator.params
                _data_loader = estimator.loader
            else:
                if estimator.score > _best_score:
                    _best_score = estimator
                    _best_estimator_name = estimator.name
                    _best_params = estimator.params
                    _data_loader = estimator.loader
        return _best_estimator_name, _best_score, _data_loader, _best_params


class ModelForecaster:
    """
    A class for making predictions using a trained machine learning model.

    Attributes:
        model: The trained machine learning model.
        y_pred: Predicted values generated by the model.
    """

    def __init__(self):
        self.model = None
        self.y_pred = None

    def fit(self, model, model_selector):
        """
        Fit the forecaster with a machine learning model selected by a ModelSelector instance.

        Parameters:
            model (sklearn.base.BaseEstimator): The machine learning model to fit.
            model_selector (ModelSelector): The ModelSelector instance containing the selected model.
        """
        _model = model.set_params(**model_selector.best_estimator.params)
        _model.fit(model_selector.best_estimator.loader.X_train, model_selector.best_estimator.loader.y_train)
        self.model = _model

    def predict(self, X):
        """
        Make predictions using the trained machine learning model.

        Parameters:
            X (array-like): The input data on which to make predictions.

        Returns:
            y_pred (array-like): The predicted values generated by the model.
        """
        self.y_pred = self.model.predict(X)
        return self.y_pred
