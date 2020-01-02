import json
from selenium import webdriver
from selenium.webdriver import firefox
from webdriver_manager.firefox import GeckoDriverManager


def _read_config(file, tag):
    with open(file) as json_file:
        as_dict = json.load(json_file)[tag]
        return as_dict


def get_browser(browser):
    if browser.upper() == "FF":
        return webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser.upper() == "FF_HL":
        options = firefox.options.Options()
        options.headless = True
        return webdriver.Firefox(executable_path=GeckoDriverManager().install(),
                                 options=options)


def get_env(env):
    if env.upper() == "LINKEDIN":
        return _read_config("config.json", "Linkedin")
    else:
        raise TypeError("Unexpected Env.")
