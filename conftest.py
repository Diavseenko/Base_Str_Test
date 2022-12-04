import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def start_brows_with_lang(lang):
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': lang})
    browser = webdriver.Chrome(options=options)
    return browser


def pytest_addoption(parser):
    parser.addoption('--lang', action='store', default="en-gb",
                     help="Choose language: ru or en-gb")


@pytest.fixture(scope="function")
def browser(request):
    lang_list = ["ar", "ca", "cs", "da", "de", "en-gb", "el", "es", "fi", "fr", "it", "ko", "nl", "pl", "pt", "pt-br",
                 "ro", "ru", "sk", "uk", "zh-hans"]
    browser_lang = request.config.getoption("--lang")
    for language in lang_list:
        if browser_lang == language:
            print(language)
            browser = None
            print("\nstart browser for test..")
            browser = start_brows_with_lang(browser_lang)
            break
    else:
        raise pytest.UsageError("--lang should be ru or en-gb")
    yield browser
    print("\nquit browser..")
    browser.quit()


    #fp = webdriver.FirefoxProfile()
    #fp.set_preference("intl.accept_languages", lang)
    #browser = webdriver.Firefox(firefox_profile=fp)
