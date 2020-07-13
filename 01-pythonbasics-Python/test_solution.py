import os,sys
sys.path.append(os.getcwd())
from pythonbasics import show_excitement
import pytest

result = "I am super excited for this course! I am super excited for this course! I am super excited for this course! I am super excited for this course! I am super excited for this course! "
@pytest.mark.parametrize('x,result',[
    (2, result)
])
def test_maxblock(x,result):
    assert show_excitement() == result
def test_maxblock1(y,result):
    assert show_excitement() == result