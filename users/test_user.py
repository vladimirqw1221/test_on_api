import pytest
import requests
from configuration import SERVICE_URL
from src.baseclasses.responce import Responce

# resp = requests.get(SERVICE_URL)
# print(resp.json())
from src.shemes.user import User


@pytest.mark.devopopment
@pytest.mark.production
@pytest.mark.skip("issue - 21212")
def test_ggeters_userts_list(get_user, make_number, calculite):
    Responce(get_user).assert_response(200).validate(User)
    # print(make_number)
    # print(f"result :\n {calculite(1,1)}")


@pytest.mark.skip("issue -2323")
def test_calculator_1(calculite):
    """test on test"""
    print(calculite(2, 2))


def test_calculator_2(calculite):
    print(calculite(-2, 2))


def test_calculator_3(calculite):
    print(calculite(-1, -2))


def test_calculator_4(calculite):
    print(calculite("b", 2))


def test_calculator_5(calculite):
    print(calculite("b", "b"))


@pytest.mark.devopopment
@pytest.mark.parametrize('first_value , second_value, result', [
    (2, 2, 4),
    (-2, 2, 0),
    (-1, -2, -3),
    ("b", 2, None),
    ('b', 'b', None)

])
def test_calc(first_value, second_value, result, calculite):
    assert calculite(first_value, second_value) == result


def test_on_asser_for_allure():
    """Test on assert"""
    try:
        assert 1 == 2
    except AssertionError:
        assert 1 == 1
