import pytest
import  requests
from configuration import SERVICE_URL
@pytest.fixture()
def get_user():
    responce = requests.get(SERVICE_URL)
    return responce