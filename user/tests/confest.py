import pytest
from .fixtures import ASANA_USER


@pytest.fixture(autouse=True)
def mock_create_asana_user(mocker):
    """create asana user mock object for check the function call"""
    mock = mocker.patch(
        'asana.resources.gen.workspaces._Workspaces.add_user_for_workspace'
    )
    mock.return_value = ASANA_USER
    yield mock
