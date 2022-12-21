import pytest


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox')


@pytest.fixture
def init_params(request):
    args = {}
    args['browser'] = request.config.getoption('--browser')
    request.cls.params = args
