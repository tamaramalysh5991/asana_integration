import pytest

from ..models import Project
from .fixtures import ASANA_PROJECT


@pytest.fixture(autouse=True)
def mock_create_asana_project(mocker):
    """create asana project mock object for check the function call"""
    mock = mocker.patch(
        'asana.resources.projects.Projects.create'
    )
    mock.return_value = ASANA_PROJECT
    yield mock


@pytest.fixture(autouse=True)
def mock_update_asana_project(mocker):
    """update asana project mock object for check the function call"""
    mock = mocker.patch(
        'asana.resources.projects.Projects.update_project'
    )
    mock.return_value = ASANA_PROJECT
    yield mock


@pytest.mark.django_db
def test_project_create(mock_create_asana_project):
    """Check that after project creation the Asana API user
    creation was called"""
    project_name = 'my first project'
    Project.objects.create(name=project_name)
    assert mock_create_asana_project.called
    assert Project.objects.filter(name=project_name).first()


@pytest.mark.django_db
def test_project_update(mock_create_asana_project, mock_update_asana_project):
    """Check that after project update the Asana API project
    update was called"""
    project_name = 'my first project'
    project = Project.objects.create(name=project_name, gid='12324')
    project.name = 'new_name'
    project.save()
    assert mock_create_asana_project.called
    assert mock_update_asana_project.called
    assert not Project.objects.filter(name=project_name).first()
