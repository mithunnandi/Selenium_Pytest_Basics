import pytest

@pytest.mark.login
def test_m1():
    a=3
    b=4
    assert a==b,"Not Equal"

def test_m2():
    name="Selenium"
    assert name.upper()=="SELENIUM"

def test_m3():
    assert True

def test_m4():
    assert False

def test_m5():
    assert 100==100

@pytest.mark.login
def test_m6():
    assert "mithun"=="MITHUN"

@pytest.mark.login
def test_m7():
    assert "MITHUN"=="MITHUN"
