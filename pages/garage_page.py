from selenium.webdriver.common.by import By
from .base_page_with_driver import BasePageWithDriver
from controls.button import Button
from controls.textbox import TextBox


class GaragePage(BasePageWithDriver):
    def __init__(self):
        super().__init__()
        self._my_profile_button = None
        self._edit_button = None
        self._model_field = None
        self._mileage_field = None
        self._save_button = None
        self._remove_car_button = None
        self._remove_danger_car_button = None

    def get_my_profile_button(self):
        self._my_profile_button = Button(self._driver.find_element(By.ID, "userNavDropdown"))
        return self._my_profile_button

    def get_edit_button(self):
        self._edit_button = Button(self._driver.find_element(By.XPATH, "//*[@class='car_edit btn btn-edit']"))
        return self._edit_button

    def get_model_field(self):
        self._model_field = TextBox(self._driver.find_element(By.ID, 'addCarModel'))
        return self._model_field

    def get_mileage_field(self):
        self._mileage_field = TextBox(self._driver.find_element(By.ID, 'addCarMileage'))
        return self._mileage_field

    def get_save_button(self):
        self._save_button = Button(self._driver.find_element(By.XPATH, "//*[text()='Save']"))
        return self._save_button

    def get_remove_car_button(self):
        self._remove_car_button = Button(self._driver.find_element(By.XPATH, "//*[text()='Remove car']"))
        return self._remove_car_button

    def get_remove_danger_car_button(self):
        self._remove_danger_car_button = Button(self._driver.find_element(By.XPATH, "//*[@class ='btn btn-danger']"))
        return self._remove_danger_car_button




