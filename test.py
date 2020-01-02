from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.config_util import get_browser, get_env




driver = get_browser('FF_HL')
driver.get(get_env("Linkedin")["app_url"])
login_in = driver.find_element(*LoginPageLocators._CLICK_LOGIN).click()
driver.find_element(*LoginPageLocators._LOGIN_USER_INPUT).send_keys(get_env("Linkedin")["user"])
driver.find_element(*LoginPageLocators._LOGIN_PASSWORD_INPUT).send_keys(get_env("Linkedin")["pswd"])
driver.find_element(*LoginPageLocators._CLICK_TO_LOG_IN).click()
text_location = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@class,'profile-rail')]/../div[2]")))
text = text_location.text
assert text == 'Welcome, Rafał!'
driver.quit()
