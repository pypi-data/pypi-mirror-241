from a_pandas_ex_apply_ignore_exceptions import pd_add_apply_ignore_exceptions
from npsearchsequence import np_search_sequence, np_search_string
from pandas.core.frame import Series
import pandas as pd

pd_add_apply_ignore_exceptions()


def _find_sequence(series, seq, exception_val=pd.NA, distance=1):
    """
    Find the occurrences of a given sequence or substring within each element of a pandas Series.

    Parameters:
    - series (pandas.Series): The input Series to search within.
    - seq (str or bytes): The sequence or substring to search for within each element of the Series.
    - exception_val: The value to use for elements where an exception occurs during the search. Default is pd.NA.
    - distance (int, optional): The minimum distance between consecutive characters
      of the sequence or substring in each element of the Series. Default is 1.

    Returns:
    pandas.Series:
        A new Series where each element contains an array of indices where the given sequence or substring is found.

    Example:
    import pandas as pd
    from a_pandas_ex_sequence_search import pd_add_find_sequence
    pd_add_find_sequence()
    df = pd.read_csv("https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv")
    df.Name.s_find_sequence('Mr', exception_val=pd.NA, distance=1)
    0     [8]
    1     [9]
    2      []
    3    [10]
    4     [7]
    5     [7]
    6    [10]
    7      []
    8     [9]
    9     [8]

    Notes:
    - If the element is of type bytes, the function uses 'S1' encoding for NumPy arrays.
    """

    return series.ds_apply_ignore(exception_val, lambda q:
    np_search_string(string=q, substring=seq, distance=distance)
    if isinstance(q, (str, bytes)) else np_search_sequence(a=q, seq=seq, distance=distance))


def pd_add_find_sequence():
    Series.s_find_sequence = _find_sequence
