import pytest

from ..models import User
from .fixtures import ASANA_USER


@pytest.fixture(autouse=True)
def mock_create_asana_user(mocker):
    """create asana user mock object for check the function call"""
    mock = mocker.patch(
        'asana.resources.gen.workspaces._Workspaces.add_user_for_workspace'
    )
    mock.return_value = ASANA_USER
    yield mock


@pytest.mark.django_db
def test_user_create(mock_create_asana_user):
    """Check that after user creation the Asana API user creation was called"""
    User.objects.create(name='john@jon.com')
    assert mock_create_asana_user.called
    assert User.objects.filter(name='john@jon.com').first()