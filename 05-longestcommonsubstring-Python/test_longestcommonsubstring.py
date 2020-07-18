import pytest
from longestcommonsubstring import longestcommonsubstring
import os
import sys
sys.path.append(os.getcwd())


@pytest.mark.parametrize('x, y, result', [
    ("abcdef", "abqrcdest", "cde"),
    ("abcdef", "ghi", ""),
    ("abcdef", "abqrcdest",  "cde"),
    ("abcdef", "ghi",  ""),
    ("", "abqrcdest",  ""),
    ("abcdef", "",  ""),
])
def test_longestcommonsubstring(x, y, result):
    assert longestcommonsubstring(x, y) == result
