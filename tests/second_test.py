import pytest

@pytest.mark.parametrize("a,b,c",
                         [
                             (1,2,3),
                             (2,3,5),
                             (1,1,4),
                             (0,1,1)
                         ])
def test_sum(a,b,c,setup_teardown_test):
    '''если сложить 2 и 2
    то получится 4'''
    assert a + b == c