import pytest

@pytest.fixture()
def set_up():
    print('Start test buying')
    yield
    print('End test buying')

@pytest.fixture(scope='module')
def set_group():
    print('Enter test')
    yield
    print('Exit test')