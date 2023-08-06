from fannys_math_package.functions import add, sub, mul, div


def test_add_zero():
    result = add(1, 0)
    assert result == 1


def test_sub_negative():
    result = sub(5, 28)
    assert result == -23


def test_mul_zero():
    result = mul(0, 12)
    assert result == 0


def test_div_zero():
    try:
        div(5, 0)
    except ZeroDivisionError:
        assert True
    else:
        assert False
