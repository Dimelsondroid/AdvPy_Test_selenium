import time
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class TestSelenium:
    driver = webdriver.ChromiumEdge(EdgeChromiumDriverManager().install())

    def get_login_page(self):
        try:
            self.driver.get('https://passport.yandex.ru/auth/')
            print(self.driver.title)
            assert 'Авторизация' in self.driver.title and 'Введите ваш ID' in self.driver.page_source
            return 'Login page Test Passed'
        except AssertionError:
            return 'Login page Test Failed'

    def enter_correct_username(self, user):
        try:
            search_username_input = self.driver.find_element(By.ID, 'passp-field-login')
            search_username_input.send_keys(Keys.CONTROL + 'a')
            search_username_input.send_keys(Keys.DELETE)
            search_username_input.send_keys(user)
            search_username_input.send_keys(Keys.RETURN)
            assert 'Логин введен некорректно или удален' in self.driver.page_source
            return 'Correct Username test Passed'
        except AssertionError:
            return 'Incorrect Username test Passed'

    def enter_correct_password(self, password):
        try:
            search_pass_input = self.driver.find_element(By.CLASS_NAME, 'Textinput-Control')
            search_pass_input.send_keys(Keys.CONTROL + 'a')
            search_pass_input.send_keys(Keys.DELETE)
            search_pass_input.send_keys(password)
            search_pass_input.send_keys(Keys.RETURN)
            assert 'Неверный пароль' in self.driver.page_source
            return 'Correct password test Passed'
        except AssertionError:
            return 'Incorrect password test Passed'


if __name__ == '__main__':
    correct_username = ''
    correct_password = ''

    # Tests for correct data
    test_success = TestSelenium()
    print(test_success.get_login_page())
    time.sleep(2)
    print(test_success.enter_correct_username('user'))
    time.sleep(2)
    print(test_success.enter_correct_username(correct_username))
    time.sleep(2)
    print(test_success.enter_correct_password('password'))
    time.sleep(2)
    print(test_success.enter_correct_password(correct_password))
    time.sleep(2)
    test_success.driver.quit()

