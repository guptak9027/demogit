# test_app.py
from app import add

def test_add():
    assert add(5, 7) == 12
    assert add(-1, 1) == 0

print("All tests passed!")
test_add()
