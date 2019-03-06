import pytest
from fixture.application import Application


@pytest.fixture
def fixture(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


__author__ = 'GiSDeCain'
