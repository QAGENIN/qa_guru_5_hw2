from selene import be, have
from selene.support.shared import browser


def test_google_search(browser_steps):
    browser.element('[name=q]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_negative_google_search(gen_rand_string, browser_steps):
    browser.element('[name=q]').type(gen_rand_string).press_enter()
    browser.element('#result-stats').should(have.text('Результатов: примерно 0'))
    print('Поиск завершился неудачей')