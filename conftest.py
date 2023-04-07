import pytest
from selene.support.shared import browser
import random
import string


@pytest.fixture(scope='function')
def gen_rand_string():
    letters = string.ascii_lowercase
    rand_string = ''.join(random.sample(letters, 16))
    return rand_string


@pytest.fixture(scope='function')
def browser_steps():
    browser.config.window_width = 1600
    browser.config.window_height = 900
    browser.open('https://google.com')
    yield 'close'
    browser.close()
