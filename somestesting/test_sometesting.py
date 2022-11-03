import pytest
from src.generators.player_localization import PlayerLocalization
from src.baseclasses.bullder_base import BulderClass

def test_smetesting(get_number):
    assert 1==1
    print(get_number)

@pytest.mark.parametrize("status" , [
    "ACTIVE",
    "BANNED",
    "DELETED",
    "INACTIVE"
])


def test_sometesting_2(status, get_player_generator ):
    print(get_player_generator.set_status(status).build())


@pytest.mark.parametrize("balance_value" , [
    "100",
    "0",
    "-10",
    "sdda"
])


def test_sometesting_2(balance_value, get_player_generator ):
    print(get_player_generator.set_balance(balance_value).build())

@pytest.mark.parametrize("delete_key" , [
    "account_status",
    "balance",
    "localize",
    "avatar"
])


def test_sometesting_3(delete_key, get_player_generator ):
    object_to_send = get_player_generator.build()
    del object_to_send[delete_key]
    print(object_to_send)

@pytest.mark.parametrize('loalisattion',["fr" ,"de","gb", "ch"])
def test_sometesting_4(get_player_generator,loalisattion ):
    object_to_send = get_player_generator.update_inner_value(['localize', loalisattion], PlayerLocalization("fr_FR").set_number(15).build()
                                                             ).build()
    print(object_to_send)


