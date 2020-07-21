import os,sys
sys.path.append(os.getcwd())
from removeduplicate import removeduplicate
import pytest


@pytest.mark.parametrize('a, result',[
    ("JavaPython", "JavPython"), ("HelloWorld", "HeloWrd"), ("EEE", "E"),#Testcase fault for Hello world('l' repeating two times; so i changed it as single l in the output)
    ("a a ", "a "), ("121212121", "12"), ("", ""),
    ("Test", "Test"), ("1001", "10"), ("11110000", "10"),
])
def test_removeduplicate(a, result):
    assert removeduplicate(a) == result
