import allure

from models.register_post_model import RegisterPostModel
import requests
from driver import Driver
from pages.login_page import LoginPage
from pages.garage_page import GaragePage
from facades.login_facade import LoginFacade
import time


class TestAuthentication:
    def setup_class(self):
        self.driver = Driver.get_chrome_driver()
        self.login_page = LoginPage()
        self.garage_page = GaragePage()
        self.login_facade = LoginFacade()
        self.session = requests.session()
        register_user = RegisterPostModel("Jon", "Snow", "tes3t5132334ts@rs.fd", "Qwerty123", "Qwerty123")
        self.session.post("https://qauto2.forstudy.space/api/auth/signup", json=register_user.__dict__)

    def setup_method(self):
        self.driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")

    def test_check_login_window(self):
        self.login_facade.click_sign_in_button()
        assert self.login_facade.check_if_email_field_displayed

    def test_check_incorrect_email(self):
        self.login_facade.click_sign_in_button()
        self.login_facade.set_email_field("qwer451")
        self.login_facade.click_remember_me_button()
        assert self.login_facade.check_if_wrong_login_alert_displayed

    def test_check_successful_login(self):
        self.login_facade.open_login_form()
        self.login_facade.set_email_and_password_and_click_login_button("test1234ts@rs.fd", "Qwerty123")
        assert self.login_facade.check_if_profile_displayed()

    def test_check_login_with_removed_user(self):
        new_user = RegisterPostModel("Jon", "Snow", "teasds3t5132334ts@rs.fd", "Qwerty123", "Qwerty123")
        self.session.post("https://qauto2.forstudy.space/api/auth/signup", json=new_user.__dict__)
        self.session.delete("https://qauto2.forstudy.space/api/users")
        self.login_facade.click_sign_in_button()
        self.login_facade.set_email_and_password("teasds3t5132334ts@rs.fd", "Qwerty123")
        self.login_facade.click_login_button()
        self.login_facade.check_if_wrong_user_alert_displayed()

    def teardown_method(self):
        screen_name_using_current_time = time.strftime("%Y%m%d-%H%M%S")
        allure.attach(self.driver.get_screenshot_as_png(), name=screen_name_using_current_time)

    def teardown_class(self):
        self.session.delete("https://qauto2.forstudy.space/api/users")


# pytest --alluredir=tmp/allure_report - run tests with allure cache
# allure serve tmp/allure_report - run allure server and view test report
