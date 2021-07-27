import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose your language")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language_site = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language_site})

    if len(language_site) == 2:
        if browser_name == "chrome":
            print("\nstart chrome browser for test..")
            browser = webdriver.Chrome(options=options)
        elif browser_name == "firefox":
            print("\nstart firefox browser for test..")
            fp = webdriver.FirefoxProfile()
            fp.set_preference("intl.accept_languages", language_site)
            browser = webdriver.Firefox(firefox_profile=fp)
        else:
            raise pytest.UsageError("--browser_name should be chrome or firefox")
    else:
        raise pytest.UsageError("--language should contained only two letters")
    yield browser
    print("\nquit browser..")
    browser.quit()