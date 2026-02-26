from src.mathoperation import add, sub

def test_add():
    assert (4,8) == 12
    assert (4,2) == 6
    assert (8,3) == 11

def test_sub():
    assert (44,33) == 11
    assert (78,57) == 21
    assert (64,7) == 57
