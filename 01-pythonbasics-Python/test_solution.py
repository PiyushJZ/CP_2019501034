import pytest
from pythonbasics import show_excitement
import os
import sys
sys.path.append(os.getcwd())

result = "I am super excited for this course! I am super excited for this course! I am super excited for this course! I am super excited for this course! I am super excited for this course! "


@pytest.mark.parametrize('x,result', [
    (2, result)
])
def test_maxblock(x, result):
    assert show_excitement() == result
