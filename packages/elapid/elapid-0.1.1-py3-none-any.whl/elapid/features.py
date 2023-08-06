"""Backend helper functions that don't need to be exposed to users"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

from elapid.utils import MAXENT_DEFAULTS, repeat_array


class MaxentFeatureTransformer(object):
    def __init__(
        self,
        feature_types=MAXENT_DEFAULTS["feature_types"],
        clamp=MAXENT_DEFAULTS["clamp"],
        n_hinge_features=MAXENT_DEFAULTS["n_hinge_features"],
        n_threshold_features=MAXENT_DEFAULTS["n_threshold_features"],
    ):
        """
        Transforms covariate data into maxent-format feature data.

        :param feature_types: a list of maxent features to generate.
        :param clamp: boolean of whether to clamp feature values to global mins/maxs during inference
        :param n_hinge_features: the number of hinge knots to generate
        :param n_threshold_features: the number of threshold features to generate
        :returns: none
        """
        # user-specified parameters
        self.feature_types_ = validate_feature_types(feature_types)
        self.clamp_ = validate_boolean(clamp)
        self.n_hinge_features_ = validate_numeric_scalar(n_hinge_features)
        self.n_threshold_features_ = validate_numeric_scalar(n_threshold_features)

        # data-driven parameters
        self.initialized_ = False
        self.hinge_ranges_ = dict()
        self.threshold_ranges_ = dict()
        self.categorical_encoders_ = dict()
        self.categorical_ = None
        self.feature_mins_ = None
        self.feature_maxs_ = None
        self.labels_ = None

    def fit(self, x, categorical=None, labels=None):
        """
        Fits features to covariates x.

        :param x: array-like of shape (n_samples, n_features) with covariate data
        :param categorical: either a 2D a array-like akin to "x", or a 1d array-like of column indices indicating which columns are categorical
        :param labels: covariate labels. Ignored if x is a pandas dataframe
        :returns: none. updates the transformer object.
        """
        con, cat = self._format_covariate_data(x, categorical=categorical, labels=labels)
        self._compute_features(con, cat, transform=False)
        self.initialized_ = True

    def transform(self, x, categorical=None, labels=None):
        """
        Applies feature transformations to covariates x.

        :param x: array-like of shape (n_samples, n_features) with covariate data
        :param categorical: either a 2D a array-like akin to "x", or a 1d array-like of column indices indicating which columns are categorical
        :param labels: covariate labels. Ignored if x is a pandas dataframe
        :returns: features, a dataframe with feature transformations applied to x
        """
        assert self.initialized_, "Transformer must be fit first"

        if categorical is None:
            categorical = self.categorical_

        if labels is None:
            labels = self.labels_

        con, cat = self._format_covariate_data(x, categorical=categorical, labels=labels)
        features = self._compute_features(con, cat, transform=True)

        if self.clamp_:
            features = self._clamp_features(features)

        return features

    def fit_transform(self, x, categorical=None, labels=None):
        """
        Fits features and applies transformations to covariates x.

        :param x: array-like of shape (n_samples, n_features) with covariate data
        :param categorical: either a 2D a array-like akin to "x", or a 1d array-like of column indices indicating which columns are categorical
        :param labels: covariate labels. Ignored if x is a pandas dataframe
        :returns: features, a dataframe with feature transformation applied to x
        """
        con, cat = self._format_covariate_data(x, categorical=categorical, labels=labels)
        features = self._compute_features(con, cat, transform=False)
        self.initialized_ = True

        return features

    def _format_covariate_data(self, x, categorical=None, labels=None):
        """
        Standardizes array-like input data to a consistent data structure.

        :param x: array-like of shape (n_samples, n_features) with covariate data
        :param categorical: either a 2D a array-like akin to "x", or a 1d array-like of column indices indicating which columns are categorical
        :param labels: covariate labels. Ignored if x is a pandas dataframe
        :returns (con, cat): a tuple of pandas dataframes with continuous and categorical covariates
        """
        if isinstance(x, pd.DataFrame):
            x.drop(["geometry"], axis=1, errors="ignore", inplace=True)
            con = x.select_dtypes(exclude="category")
            cat = x.select_dtypes(include="category")
            self.labels_ = list(x.columns) if labels is None else labels
        else:
            self.categorical_ = categorical
            con, cat = self._covariates_to_df(x, categorical=categorical, labels=labels)

        return con, cat

    def _covariates_to_df(self, x, categorical=None, labels=None):
        """
        Converts 2D numerical arrays into labeled pandas DataFrames for continuous and categorical variables

        :param x: a numpy array of shape (nrows, ncols), where nrows = number of samples, ncols = number of covariates
        :param categorical: 2D a numpy array akin to "x", or a 1d array of column-wise indices indicating which columns are categorical
        :param labels: covariate labels. Ignored if x is a pandas dataframe
        :returns (con, cat): a tuple of pandas dataframes with continuous and categorical covariates
        """
        # cast x to 2d if only one feature is passed
        if np.ndim(x) == 1:
            x = x.reshape(-1, 1)

        # auto-generate class labels
        if labels is None:
            labels = [f"cov_{i+1}" for i in range(x.shape[1])]

        # subst the continuous / categorical data based on how the "categorical" argument is passed
        if categorical is None:
            con = x
            cat = None
            con_labels = labels
            cat_labels = []

        # treat 1-d categorical parameters as an index
        else:
            if np.ndim(categorical) == 1:
                continuous = list(range(x.shape[1]))
                [continuous.pop(cat_idx) for cat_idx in categorical]
                con = x[:, continuous]
                cat = x[:, categorical]
                con_labels = [labels[con_idx] for con_idx in continuous]
                cat_labels = [labels[cat_idx] for cat_idx in categorical]

            # treat n-d arrays as covariates
            else:
                con = x
                cat = categorical
                con_labels = labels
                cat_labels = [f"cov_{len(labels)+i+1}" for i in range(cat.shape[1])]

        # concatenate multiple series to get around stupid multi-category pandas issues
        if cat is None:
            cat_df = pd.DataFrame()
        else:
            cat_list = [
                pd.Series(cat[:, i], name=cat_label, dtype="category") for i, cat_label in enumerate(cat_labels)
            ]
            cat_df = pd.concat(cat_list, axis=1)

        con_df = pd.DataFrame(con, columns=con_labels)

        # save labels for applying to new datasets
        if not self.initialized_:
            self.labels_ = labels
            self.categorical_ = self.categorical_

        return (con_df, cat_df)

    def _compute_features(self, con, cat, transform=False):
        """
        Transforms input data to the features used for model training.

        :param con: a pandas dataframe encoded with continuous (i.e. numeric) covariates
        :param cat: a pandas dataframe encoded with categorical (i.e. class) covariates
        :param transform: boolean for whether to apply already-fit transformations.
        :returns features: a dataframe with the feature transformations applied to each column
        """
        categorical_covariates = list(cat.columns)
        continuous_covariates = list(con.columns)
        feature_list = list()

        # categorical feature transforms
        for covariate in categorical_covariates:

            series = cat[covariate]
            classes = list(series.unique())
            classes.sort()
            feature_names = [f"{covariate}_class_{clas}" for clas in classes]

            if transform:
                encoder = self.categorical_encoders_[covariate]
                one_hot_encoded = encoder.transform(series.to_numpy().reshape(-1, 1))
            else:
                encoder = OneHotEncoder(sparse=False, dtype=np.uint8)
                one_hot_encoded = encoder.fit_transform(series.to_numpy().reshape(-1, 1))
                self.categorical_encoders_[covariate] = encoder

            feature_df = pd.DataFrame(one_hot_encoded, columns=feature_names)
            feature_list.append(feature_df)

        # continuous feature transforms
        for covariate in continuous_covariates:
            series = con[covariate]

            if "linear" in self.feature_types_:

                feature_list.append(series.rename(f"{covariate}_linear"))

            if "quadratic" in self.feature_types_:

                feature_list.append((series ** 2).rename(f"{covariate}_squared"))

            if "hinge" in self.feature_types_:

                if not transform:
                    self.hinge_ranges_[covariate] = [series.min(), series.max()]

                hinges = hinge(series.to_numpy(), n_hinges=self.n_hinge_features_, range=self.hinge_ranges_[covariate])
                feature_names = [f"{covariate}_hinge_{i+1:03d}" for i in range((self.n_hinge_features_ - 1) * 2)]
                feature_df = pd.DataFrame(hinges, columns=feature_names)
                feature_list.append(feature_df)

            if "threshold" in self.feature_types_:

                if not transform:
                    self.threshold_ranges_[covariate] = [series.min(), series.max()]

                thresholds = threshold(
                    series.to_numpy(), n_thresholds=self.n_threshold_features_, range=self.threshold_ranges_[covariate]
                )
                feature_names = [f"{covariate}_threshold_{i+1:03d}" for i in range(self.n_threshold_features_ - 2)]
                feature_df = pd.DataFrame(thresholds, columns=feature_names)
                feature_list.append(feature_df)

            if "product" in self.feature_types_:

                idx_cov = continuous_covariates.index(covariate)
                for i in range(idx_cov, len(continuous_covariates) - 1):
                    feature_name = f"{covariate}_x_{continuous_covariates[i+1]}"
                    product = series * con[continuous_covariates[i + 1]]
                    feature_df = pd.DataFrame(product, columns=[feature_name])
                    feature_list.append(feature_df)

        features = pd.concat(feature_list, axis=1)

        # store mins and maxes to clamp features later
        if not transform:
            self.feature_mins_ = features.min()
            self.feature_maxs_ = features.max()

        return features

    def _clamp_features(self, features):
        """
        Sets feature values to the min/max of the global range the features were fit with.

        :param features: array-like of shape (n_samples, n_features)
        :returns: features array-like with values clamped to global min/max
        """
        assert self.initialized_, "Transformer must be fit first"

        return features.apply(clamp_row, axis=1, raw=True, mins=self.feature_mins_, maxs=self.feature_maxs_)


def hingeval(x, mn, mx):
    """
    Computes hinge transformation values.

    :param x: array-like of covariate values
    :param mn: the minimum covariate value to fit hinges to
    :param mx: the maximum covariate value to fit hinges to
    :returns: an array of hinge features
    """
    return np.minimum(1, np.maximum(0, (x - mn) / (mx - mn)))


def hinge(x, n_hinges=30, range=None):
    """
    Fits hinge transformations to an array of covariates.

    :param x: array-like of covariate values
    :param n_hinges: integer of the number of transformations to apply
    :param range: list or tuple of the range of covariate values to fit across
    :returns: an array of hinge features of shape (n_samples, (n_hinges-1) * 2)
    """
    mn = range[0] if range is not None else np.min(x)
    mx = range[1] if range is not None else np.max(x)
    k = np.linspace(mn, mx, n_hinges)

    xarr = repeat_array(x, len(k) - 1, axis=1)
    lharr = repeat_array(k[:-1], len(x), axis=0)
    rharr = repeat_array(k[1:], len(x), axis=0)

    lh = hingeval(xarr, lharr, mx)
    rh = hingeval(xarr, mn, rharr)

    return np.concatenate((lh, rh), axis=1)


def threshold(x, n_thresholds=30, range=None):
    """
    Fits arbitrary threshold transformations to an array of covariates.

    :param x: array-like of covariate values
    :param n_thresholds: integer of the number of transformations to apply
    :param range: list or tuple of the range of covariate values to fit across
    :returns: an array of thresholds features of shape (n_samples, n_thresholds - 2)
    """
    mn = range[0] if range is not None else np.min(x)
    mx = range[1] if range is not None else np.max(x)
    k = np.linspace(mn, mx, n_thresholds + 2)[2:-2]

    xarr = repeat_array(x, len(k), axis=1)
    tarr = repeat_array(k, len(x), axis=0)

    return (xarr > tarr).astype(np.uint8)


def clamp_row(row, mins, maxs):
    """
    Clamps feature data to the range of features previously estimated ranges. Designed to run with pandas df.apply()

    :param row: a row / 1-d array of feature values
    :param mins: an array of global feature minimum values
    :param maxs: an array of global ffeature maximum values
    :returns: an array of feature values clamped to the min/max range
    """
    return np.min([maxs, np.max([row, mins], axis=0)], axis=0)


def compute_lambdas(y, weights, reg, n_lambda=200):
    """
    Computes lambda parameter values for elastic lasso fits.

    :param y: array-like of shape (n_samples,) with binary presence/background (1/0) values
    :param weights: per-sample model weights
    :param reg: per-feature regularization coefficients
    :param n_lambda: the number of lambda values to estimate
    :returns lambdas: a numpy array of lambda scores of length n_lambda
    """
    n_presence = np.sum(y)
    mean_regularization = np.mean(reg)
    total_weight = np.sum(weights)
    seed_range = np.linspace(4, 0, n_lambda)
    lambdas = 10 ** (seed_range) * mean_regularization * (n_presence / total_weight)

    return lambdas


def compute_weights(y, pbr=100):
    """
    Uses Maxent's weight formulation to compute per-sample model weights.

    :param y: array-like of shape (n_samples,) with binary presence/background (1/0) values
    :param pbr: the presence-to-background weight ratio. pbr=100 sets background samples to 1/100 weight of presence samples.
    :returns weights: 1-d array-like with glmnet-formatted
    """
    weights = np.array(y + (1 - y) * pbr)

    return weights


def compute_regularization(
    f, y, beta_multiplier=1.0, beta_lqp=1.0, beta_threshold=1.0, beta_hinge=1.0, beta_categorical=1.0
):
    """
    Computes variable regularization values for all feature data.

    :param f: pandas dataframe with feature transformations applied
    :param y: array-like of shape (n_samples,) with binary presence/background (1/0) values
    :param beta_multiplier: scalar for all regularization parameters, where higher values exclude more features
    :param beta_lqp: scalar for linear, quadratic and product feature regularization parameters
    :param beta_threshold: scalar for threshold feature regularization parameters
    :param beta_hinge: scalar for hinge feature regularization parameters
    :param beta_categorical: scalar for categorical feature regularization parameters
    :returns max_reg: 1-d array with per-feature regularization parameters
    """

    # tailor the regularization to presence-only locations
    mm = f[y == 1]
    n_points = len(mm)
    features = list(f.columns)
    n_features = len(features)
    regularization = np.zeros(n_features)

    # set the default regularization values
    q_features = len([i for i in features if "_squared" in i])
    p_features = len([i for i in features if "_x_" in i])
    if q_features > 0:
        regtable = [[0, 10, 17, 30, 100], [1.3, 0.8, 0.5, 0.25, 0.05]]
    elif p_features > 0:
        regtable = [[0, 10, 17, 30, 100], [2.6, 1.6, 0.9, 0.55, 0.05]]
    else:
        regtable = [[0, 10, 30, 100], [1, 1, 0.2, 0.05]]

    for i, feature in enumerate(features):

        if "_linear" in feature or "_squared" in feature or "_x_" in feature:
            freg = regtable
            multiplier = beta_lqp
        elif "_hinge" in feature:
            freg = [[0, 1], [0.5, 0.5]]
            multiplier = beta_hinge
        elif "_threshold" in feature:
            freg = [[0, 100], [2, 1]]
            multiplier = beta_threshold
        elif "_class" in feature:
            freg = [[0, 10, 17], [0.65, 0.5, 0.25]]
            multiplier = beta_categorical

        ap = np.interp(n_points, freg[0], freg[1])
        regularization[i] = multiplier * ap / np.sqrt(n_points)

    # increase regularization for extreme hinge values
    hinge_features = [i for i in features if "_hinge_" in i]
    hinge_reg = np.zeros(n_features)
    for hinge_feature in hinge_features:
        hinge_idx = features.index(hinge_feature)
        std = np.max([np.std(mm[hinge_feature], ddof=1), (1 / np.sqrt(n_points))])
        hinge_reg[hinge_idx] = (0.5 * std) / np.sqrt(n_points)

    # increase threshold regularization for uniform values
    threshold_features = [i for i in features if "_threshold_" in i]
    threshold_reg = np.zeros(n_features)
    for threshold_feature in threshold_features:
        threshold_idx = features.index(threshold_feature)
        all_zeros = np.all(mm[threshold_feature] == 0)
        all_ones = np.all(mm[threshold_feature] == 1)
        threshold_reg[threshold_idx] = 1 if all_zeros or all_ones else 0

    # report the max regularization value
    default_reg = 0.001 * (np.max(f, axis=0) - np.min(f, axis=0))
    variance_reg = np.std(mm, axis=0, ddof=1) * regularization
    max_reg = np.max([default_reg, variance_reg, hinge_reg, threshold_reg], axis=0)

    # apply the final scaling factor
    max_reg *= beta_multiplier

    return max_reg


def validate_feature_types(features):
    """
    Ensures the feature classes passed are legitimate

    :param features: a list or string that must be in ["linear", "quadratic", "product", "hinge", "threshold", "auto"] or string "lqphta"
    :return valid_features: a list of formatted valid features
    """
    valid_list = ["linear", "quadratic", "product", "hinge", "threshold"]
    valid_string = "lqpht"
    valid_features = list()

    assert features is not None, "Features cannot be empty"

    # ensure the string features are valid, and translate to a standard feature list
    if type(features) is str:
        for feature in features:

            if feature == "a":
                return valid_list

            assert feature in valid_string, "Invalid feature passed: {}".format(feature)

            if feature == "l":
                valid_features.append("linear")
            elif feature == "q":
                valid_features.append("quadratic")
            elif feature == "p":
                valid_features.append("product")
            elif feature == "h":
                valid_features.append("hinge")
            elif feature == "t":
                valid_features.append("threshold")

    # or ensure the list features are valid
    elif type(features) is list:
        for feature in features:
            if feature == "auto":
                return valid_list

            assert feature in valid_list, "Invalid feature passed: {}".format(feature)

            valid_features.append(feature)

    return valid_features


def validate_boolean(var):
    """
    Asserts that an argument is boolean True/False

    :param var: the input argument to validate
    :returns var: returns the value if it passes validation, raises an exception on failure.
    """
    assert isinstance(var, bool), "Argument must be True/False"
    return var


def validate_numeric_scalar(var):
    """
    Asserts that an argument is a single numeric value.

    :param var: the input argument to validate
    :returns var: returns the value if it passes validation, raises an exception on failure.
    """
    assert isinstance(var, (int, float)), "Argument must be single numeric value"
    return var
