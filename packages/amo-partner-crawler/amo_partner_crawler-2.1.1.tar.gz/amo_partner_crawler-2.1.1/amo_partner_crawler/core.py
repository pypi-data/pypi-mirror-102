import time
import logging
from enum import Enum
from typing import Union

from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import (NoSuchElementException,
                                        TimeoutException,
                                        ElementClickInterceptedException,
                                        UnexpectedAlertPresentException,
                                        WebDriverException)

from . import exceptions, schemas


class Selector(Enum):
    by_class_name = By.CLASS_NAME
    by_id = By.ID
    by_name = By.NAME
    by_xpath = By.XPATH


docker_remote_options = {
    'command_executor': "http://selenium:4444/wd/hub",
    'desired_capabilities': DesiredCapabilities.FIREFOX
}


def alert_window_escaping(attempts: int):
    def actual_wrapper(func):
        def wrapper(*args, **kwargs):
            attempt = 0

            self = args[0]
            while attempt <= attempts:
                try:
                    return func(*args, **kwargs)
                except (UnexpectedAlertPresentException,
                        ElementClickInterceptedException):
                    self.unlock_screen()
                attempt += 1

        return wrapper

    return actual_wrapper


class Crawler:
    """
    BASE CRAWLER CLASS
    """
    remote_options = docker_remote_options
    base_options = FirefoxOptions()
    base_options.headless = True

    def __init__(self, url: str, remote: bool = False, debug: bool = False):
        self.url = url
        self.remote = remote
        self.debug = debug
        self.driver = None

    def _init_driver(self) -> None:
        self.driver = self._get_driver()

    def _get_driver(self) -> WebDriver:
        if self.remote:
            return webdriver.Remote(**self.remote_options, options=self.base_options)
        if self.debug:
            self.base_options.headless = False
        return webdriver.Firefox(options=self.base_options)

    def start(self) -> None:
        # инициализируем драйвер явныи образом в момент запуска краулера
        self._init_driver()
        self.driver.get(self.url)

    @alert_window_escaping(attempts=3)
    def wait_element(self, selector: Selector,
                     value: str,
                     visible: bool = True,
                     invisible: bool = False,
                     _all: bool = False) -> WebElement:
        # ждем появления и возвращаем элемент по типу селектора и значению
        wait = WebDriverWait(self.driver, 30)
        wait_condition = EC.visibility_of_element_located
        if _all:
            wait_condition = EC.presence_of_element_located
        if invisible:
            wait_condition = EC.invisibility_of_element
        try:
            return wait.until(wait_condition((selector.value, value)))
        except TimeoutException:
            raise exceptions.ElementHiddenException

    @alert_window_escaping(attempts=3)
    def wait_select_element(self, element: WebElement) -> Select:
        return Select(element)

    @alert_window_escaping(attempts=3)
    def choice_select_element_value(self, select: Select, value: Union[str, int]) -> WebElement:
        return select.select_by_value(value)

    @alert_window_escaping(attempts=3)
    def send_keys(self, element: WebElement, value: Union[str, int]) -> None:
        element.send_keys(value)

    @alert_window_escaping(attempts=2)
    def click_on_element(self, element: WebElement) -> None:
        element.click()

    def element_is_exists(self, selector: Selector, value: str) -> bool:
        try:
            self.driver.find_element(selector.value, value)
        except NoSuchElementException:
            return False
        return True

    def stop(self) -> None:
        self.driver.quit()

    @classmethod
    def wait(cls, seconds: int = 3) -> None:
        time.sleep(seconds)


def attempted_crawling(attempts: int):
    # декоратор увеличения попыток краулинга
    def actual_decorator(func):

        def wrapper(*args, **kwargs):
            attempt = 0
            self = args[0]
            while attempt < attempts:
                logging.warning(f'ATTEMPT# {attempt}')
                try:
                    return func(*args, **kwargs)
                except (NoSuchElementException,
                        TimeoutException,
                        AttributeError,
                        WebDriverException,
                        exceptions.ElementHiddenException,
                        exceptions.NotAuthorizeException,
                        ElementClickInterceptedException) as e:
                    logging.warning(e)
                    self.stop()
                    attempt += 1
            return schemas.BillingSchema(is_unrecognized=True)

        return wrapper

    return actual_decorator


def logg_func_execution(func):
    def echo_func(*func_args, **func_kwargs):
        logging.warning(f'{func.__name__}: in process')
        result = func(*func_args, **func_kwargs)
        logging.warning(f'{func.__name__}: done')
        return result

    return echo_func


class AmoPartnerCrawler(Crawler):
    """
    CLASS FOR SCRAPING BILLING DATA FROM AMO PARTNER CABINET
    """

    def __init__(self, email: str, password: str, remote: bool, debug: bool = False):
        self.email = email
        self.password = password
        super().__init__(url='https://www.amocrm.ru/partners/private/shop/bill', remote=remote, debug=debug)

    @logg_func_execution
    def login(self, email: str, password: str) -> None:
        login_button = self.wait_element(Selector.by_class_name, 'page_header__auth_button')
        self.click_on_element(login_button)
        email_field = self.wait_element(Selector.by_class_name, 'form_auth__type_email')
        self.send_keys(email_field, email)
        password_field = self.wait_element(Selector.by_class_name, 'form_auth__type_password')
        self.send_keys(password_field, password)
        submit_button = self.wait_element(Selector.by_class_name, 'form_auth__button_submit')
        self.click_on_element(submit_button)

    def unlock_screen(self) -> None:
        # избавление от всплывающего окна
        try:
            locker = self.wait_element(Selector.by_class_name, 'hb-animateIn')
            self.driver.execute_script("arguments[0].style.visibility='hidden'", locker)
        except (NoSuchElementException, exceptions.ElementHiddenException):
            pass

    @property
    @logg_func_execution
    def billing_is_available(self):
        try:
            self.wait_element(Selector.by_class_name, 'js-months_without_discount', invisible=True)
            return True
        except exceptions.ElementHiddenException:
            return False

    @logg_func_execution
    def check_tariff(self):
        tariff_select = self.wait_select_element(self.wait_element(Selector.by_id, 'tariff_id'))
        current_tariff_value = tariff_select.first_selected_option.get_attribute("value")

        if not current_tariff_value.isdigit() or \
                int(current_tariff_value) in [22000000, 20533490, 8404105]:
            raise exceptions.BadTariffException()

    @property
    @logg_func_execution
    def account_id_is_recognized(self):
        try:
            self.wait_element(Selector.by_class_name, 'bill_error', invisible=True)
            return True
        except exceptions.ElementHiddenException:
            return False

    @classmethod
    def is_equals_values(cls, element: WebElement, value: str) -> bool:

        if element.get_attribute('value') == value:
            return True
        return False

    @logg_func_execution
    def fill_form(self, account_id: int, pay_period: int = 12) -> None:
        # заполнение биллинговой формы
        try:
            account_id_field = self.wait_element(Selector.by_name, 'account_id')
        except exceptions.ElementHiddenException:
            raise exceptions.NotAuthorizeException()
        self.send_keys(account_id_field, str(account_id))
        self.wait(5)
        self.unlock_screen()
        # проверям соответсвие инпута с нашим id (amo иногда изменяет цифры)
        if not self.is_equals_values(account_id_field, str(account_id)):
            account_id_field.clear()
            self.send_keys(account_id_field, str(account_id))

        if not self.account_id_is_recognized:
            raise exceptions.IDNotFoundException()

        self.check_tariff()
        currency_select_field = self.wait_select_element(self.wait_element(Selector.by_id, 'currency_id'))
        self.choice_select_element_value(currency_select_field, "RUB")
        tariff_select_field = self.wait_element(Selector.by_id, 'tariff_id')
        self.wait()
        if not self.billing_is_available:
            raise exceptions.AlreadyPaidException()
        # тариф иногда невозможно выбрать, стоит дефол
        if tariff_select_field.is_enabled():
            tariff_select = self.wait_select_element(tariff_select_field)
            self.choice_select_element_value(tariff_select, '19208542')
        count_users_field = self.wait_element(Selector.by_id, 'col_users')
        self.send_keys(count_users_field, 0)
        period_to_pay_select_field = self.wait_select_element(self.wait_element(Selector.by_id, 'period_id'))
        self.choice_select_element_value(period_to_pay_select_field, str(pay_period))
        # пользователь мог уже оплатить, пробив билинга недоступен
        if not self.billing_is_available:
            raise exceptions.AlreadyPaidException()
        contract_select_field = self.wait_select_element(self.wait_element(Selector.by_id, 'contract_id'))
        self.choice_select_element_value(contract_select_field, '10952733')

    @logg_func_execution
    def approve_form(self) -> None:
        # подтверждение формы и переход к тоталу по введенным данным
        self.wait(5)
        start_bill_button = self.wait_element(Selector.by_id, 'start_bill')
        self.click_on_element(start_bill_button)

    @logg_func_execution
    def extract_data(self) -> dict:

        tariff = self.wait_element(Selector.by_xpath, "//div[contains(@class, 'tariff_value')]/input", _all=True)
        count_users = self.wait_element(Selector.by_xpath, "//div[contains(@class, 'col_user')]/div[2]/input", _all=True)
        pay_period = self.wait_element(Selector.by_xpath, "(//div[@class='row_field'])[3]/input", _all=True)
        price = self.wait_element(Selector.by_xpath, "(//div[@class='row_field'])[4]/input", _all=True)
        return {'price': price.get_attribute('value'),
                'users_count': count_users.get_attribute('value'),
                'tariff': tariff.get_attribute('value'),
                'pay_period': pay_period.get_attribute('value')}

    @attempted_crawling(attempts=2)
    def get_billing_data(self, account_id: int, pay_period: int) -> schemas.BillingSchema:
        self.start()
        # если не авторизованы - логинимся
        if not self.element_is_exists(Selector.by_id, 'user-select__header'):
            self.login(self.email, self.password)
        try:
            self.wait()
            self.fill_form(account_id, pay_period)
            self.wait()
            self.approve_form()
            self.wait()
            data = self.extract_data()
            self.stop()
            return schemas.BillingSchema(**data, pay_period_in_months=pay_period)
        except exceptions.AlreadyPaidException:
            self.stop()
            return schemas.BillingSchema(is_paid=True)
        except (exceptions.IDNotFoundException,
                exceptions.BadTariffException,
                exceptions.FatalityException):
            self.stop()
            return schemas.BillingSchema(is_unrecognized=True)
