from functools import reduce
import numpy as np


def np_search_sequence(a, seq, distance=1):
    """
    Search for the occurrence of a given sequence within a NumPy array.

    Parameters:
    - a (numpy.ndarray): The input NumPy array to search within.
    - seq (numpy.ndarray): The sequence to search for within the array.
    - distance (int, optional): The distance between consecutive elements
      of the sequence in the array. Default is 1.

    Returns:
    numpy.ndarray:
        An array of indices where the given sequence is found in the input array.

    Example:
    seq = np.array([3, 6, 8, 4])
    arr = np.random.randint(0, 9, (1000000,))
    np_search_sequence(a=arr, seq=seq, distance=1)
    array([  8370,  24712,  25143, ..., 999287, 999493, 999805])

    """

    return np.where(
        reduce(
            lambda a, b: a & b,
            (
                (
                    np.concatenate(
                        [
                            (a == s)[i * distance :],
                            np.zeros(i * distance, dtype=np.uint8),
                        ],
                        dtype=np.uint8,
                    )
                )
                for i, s in enumerate(seq)
            ),
        )
    )[0]


def np_search_string(string, substring, distance=1):
    r"""
    Search for the occurrence of a given substring within a string using NumPy.

    Parameters:
    - string (str or bytes): The input string to search within.
    - substring (str or bytes): The substring to search for within the string.
    - distance (int, optional): The distance between consecutive characters
      of the substring in the string. Default is 1.

    Returns:
    numpy.ndarray:
        An array of indices where the given substring is found in the input string.

    Example:
    text = '''Welcome! Are you completely new to programming? If not then we presume you will be looking for information about why and how to get started with Python. Fortunately an experienced programmer in any programming language (whatever it may be) can pick up Python very quickly. It's also easy for beginners to use and learn, so jump in!
    Installing Python is generally easy, and nowadays many Linux and UNIX distributions include a recent Python. Even some Windows computers (notably those from HP) now come with Python already installed. If you do need to install Python and aren't confident about the task you can find a few notes on the BeginnersGuide/Download wiki page, but installation is unremarkable on most platforms.'''
    res = np_search_string(string=text*10000, substring='man', distance=1)
    array([  119,   238,   357, ..., 93382, 93533, 93709])
    res2 = np_search_string(string=(text * 10000).encode(), substring=b"man", distance=1)

    """
    if isinstance(substring, bytes):
        return np_search_sequence(
            a=np.array([string]).view("S1"),
            seq=np.array([substring]).view("S1"),
            distance=distance,
        )
    return np_search_sequence(
        a=np.array([string]).view("U1"), seq=substring, distance=distance
    )

