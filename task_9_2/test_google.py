import pytest
from selene import browser, be, have


@pytest.fixture
def set_up():
    browser.open('https://google.com')
    browser.driver.set_window_size(1200, 800)
    yield browser
    browser.quit()


def test_google(set_up):
    browser.element('[name="q"]').should(be.blank).type('python').press_enter()
    browser.element('[id="search"]').should(have.text('Welcome to Python.org'))


def test_google_negative(set_up):
    browser.element('[name="q"]').should(be.blank).type(
        '33RERFWELKFJWEOJRO@@Y!@T#!@T#*&@!IJ2390RUFEJFD9EW2J239F').press_enter()
    browser.element('[id="search"]').should(be.hidden)
