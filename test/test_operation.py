from src.mathoperation import add, sub

def test_add():
    assert add(4,8)==12
    assert add(4,2)==6
    assert add(8,3)==11

def test_sub():
    assert sub(44,33)==11
    assert sub(78,57)==21
    assert sub(64,7)==57
