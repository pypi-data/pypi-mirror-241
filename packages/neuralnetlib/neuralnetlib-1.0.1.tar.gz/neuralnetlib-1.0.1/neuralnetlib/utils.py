import time

import numpy as np


def one_hot_encode(labels: np.ndarray, num_classes: int) -> np.ndarray:
    """One hot encoded labels are binary vectors representing categorical values,
    with exactly one high (or "hot" = 1) bit indicating the presence of a specific category
    and all other bits low (or "cold" = 0)."""
    if labels.ndim > 1:
        labels = labels.reshape(-1)

    labels = labels.astype(int)
    one_hot = np.zeros((labels.size, num_classes))
    one_hot[np.arange(labels.size), labels] = 1
    return one_hot


def dict_with_ndarray_to_dict_with_list(d: dict) -> dict:
    for k, v in d.items():
        if isinstance(v, np.ndarray):
            d[k] = v.tolist()
    return d


def dict_with_list_to_dict_with_ndarray(d: dict) -> dict:
    for k, v in d.items():
        if isinstance(v, list):
            d[k] = np.array(v)
    return d


def apply_threshold(y_pred, threshold: float = 0.5):
    """Applies a threshold to the predictions. Typically used for binary classification."""
    return (y_pred > threshold).astype(int)


def shuffle(x, y, random_state: int = None) -> tuple:
    rng = np.random.default_rng(random_state if random_state is not None else int(time.time_ns()))
    indices = rng.permutation(len(x))
    return x[indices], y[indices]
