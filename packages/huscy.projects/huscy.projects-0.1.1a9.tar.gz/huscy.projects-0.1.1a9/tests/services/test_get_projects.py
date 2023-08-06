import pytest

from huscy.projects.services import get_projects

pytestmark = pytest.mark.django_db


def test_get_projects(public_projects, private_projects):
    result = get_projects()

    assert list(result) == public_projects


def test_include_private_projects(public_projects, private_projects):
    result = get_projects(include_private_projects=True)

    assert list(result) == public_projects + private_projects
