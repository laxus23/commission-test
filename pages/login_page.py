from grappa import should
from pages.base_page import BasePage


class LoginPage(BasePage):
    _CLICK_LOGIN = "//*[contains(@class,'nav__button-secondary')]"
    _LOGIN_USER_INPUT = "//*[contains(@name, 'session_key')]"
    _LOGIN_PASSWORD_INPUT = "//*[contains(@type,'password')]"
    _CLICK_TO_LOG_IN = "//*[contains(@type, 'submit')]"
    _WELCOME_MESSAGE = "(By.XPATH, ""//*[contains(@class,'profile-rail')]/../div[2]"


    def __init__(self, context):
        super().__init__(context.browser, context.env)
        self.env = context.env

    def login_to_app(self):
        try:
            # self.goto_url(self.env["app_url"])
            self.click(self._CLICK_LOGIN)
            self.fill(self._LOGIN_USER_INPUT, self.env["user"])
            self.fill(self._LOGIN_PASSWORD_INPUT, self.env["pswd"])
            self.click(self._CLICK_TO_LOG_IN)
        except Exception:
            raise PermissionError('Login to application permissed.')