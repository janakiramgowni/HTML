import pytest

"""
@pytest.mark.markername 
this will mark the test case and run the that test using flag
-m 
pytest modulename -m markername
The above will run that test.
"""


@pytest.mark.test1
def test_variables():
    a = 5
    b = 4
    print("Hello this is test1")
    assert a > b, 'a is not greaterthan b'


def test_sum():
    a = 3
    b = 4
    c = a + b
    assert c == 7, "Sum of a,b is not 10"

def test_sub():
        a=5
        b=2
        c=a-b
        assert c==3,"subtraction not working"


@pytest.mark.test1
def test_letter():
    a = 'selenium'
    b = "Selenium"
    assert a.title() == b, 'Both are not same'


# sending different data as parameter to test
@pytest.mark.parametrize('a,b,c', [(1, 2, 3), ('I', 'N', 'IN'), (5, 6, 11)])
def test_add(a, b, c):
    assert a + b == c