import time

from Init_chrome_selenium import init_webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ex


def save_file(driver):
    """
    Нажатие кнопки скачать в Excel внизу страницы
    :param driver:
    :return:
    """
    WebDriverWait(driver, timeout=10).until(ex.presence_of_element_located((By.CLASS_NAME, '_93444fe79c--main--PpO9F._93444fe79c--light--fV8h9')))
    button_download = driver.find_element(By.CLASS_NAME, '_93444fe79c--main--PpO9F._93444fe79c--light--fV8h9')
    button_download.send_keys(Keys.ENTER)
    WebDriverWait(driver, timeout=10).until(ex.presence_of_element_located((By.CLASS_NAME,
                                       '_93444fe79c--button--Cp1dl._93444fe79c--button--IqIpq._93444fe79c--M--T3GjF._93444fe79c--button--jVM22')))
    button_save = driver.find_elements(By.CLASS_NAME,
                                       '_93444fe79c--button--Cp1dl._93444fe79c--button--IqIpq._93444fe79c--M--T3GjF._93444fe79c--button--jVM22')
    if len(button_save) == 1:
        button_save[0].send_keys(Keys.ENTER)
    elif len(button_save) == 2:
        button_save[1].send_keys(Keys.ENTER)


def authorization(driver):
    """
    Авторизация после нажатия кнопки скачать в Excell

    :param driver:
    :return:
    """
    WebDriverWait(driver, timeout=10).until(ex.presence_of_element_located((By.CLASS_NAME,
                                             '_25d45facb5--button--Cp1dl._25d45facb5--button--IqIpq._25d45facb5--M--T3GjF.'
                                             '_25d45facb5--button--jfWOF._25d45facb5--full-width--MF714')))
    authorization_type = driver.find_element(By.CLASS_NAME,
                                             '_25d45facb5--button--Cp1dl._25d45facb5--button--IqIpq._25d45facb5--M--T3GjF.'
                                             '_25d45facb5--button--jfWOF._25d45facb5--full-width--MF714')
    authorization_type.send_keys((Keys.ENTER))

    WebDriverWait(driver, timeout=10).until(ex.presence_of_element_located((By.NAME, 'username')))
    email = driver.find_element(By.NAME, 'username')
    email.send_keys('karbushev-1991@mail.ru')

    WebDriverWait(driver, timeout=10).until(ex.presence_of_element_located((By.CLASS_NAME,
                                    '_25d45facb5--button--Cp1dl._25d45facb5--button--IqIpq._25d45facb5--M--T3GjF.'
                                    '_25d45facb5--button--OhHnj._25d45facb5--full-width--MF714')))
    continuee = driver.find_element(By.CLASS_NAME,
                                    '_25d45facb5--button--Cp1dl._25d45facb5--button--IqIpq._25d45facb5--M--T3GjF.'
                                    '_25d45facb5--button--OhHnj._25d45facb5--full-width--MF714')
    continuee.send_keys(Keys.ENTER)

    WebDriverWait(driver, timeout=10).until(ex.presence_of_element_located((By.NAME, 'password')))
    password = driver.find_element(By.NAME, 'password')
    time.sleep(1)
    password.send_keys('k700399100')
    time.sleep(2)
    password.send_keys(Keys.ENTER)


def main():
    driver = init_webdriver()
    url = 'https://krasnoyarsk.cian.ru/cat.php?deal_type=sale&' \
          'engine_version=2&' \
          'floornl=1&' \
          'house_material%5B0%5D=1&' \
          'house_material%5B1%5D=2&' \
          'house_material%5B2%5D=4&' \
          'house_material%5B3%5D=8&' \
          'is_first_floor=0&' \
          'min_balconies=1&' \
          'minsu_r=1&' \
          'offer_type=flat&' \
          'region=4827&' \
          'room1=1&' \
          'room2=1&' \
          'room3=1'

    driver.get(url)
    driver.set_window_size(1920, 1080)
    time.sleep(15)
    save_file(driver)
    time.sleep(1)
    authorization(driver)
    time.sleep(10)
    error = driver.find_element(By.CLASS_NAME, '_93444fe79c--color_white_100--YUO3d.'
                                               '_93444fe79c--lineHeight_5u--cJ35s.'
                                               '_93444fe79c--fontWeight_normal--P9Ylg.'
                                               '_93444fe79c--fontSize_14px--TCfeJ.'
                                               '_93444fe79c--display_block--pDAEx.'
                                               '_93444fe79c--text--g9xAG.'
                                               '_93444fe79c--text_letterSpacing__0--mdnqq')
    if error:
        print('[-] DownloadError: Превышен лимит скачиваний для некоммерческого использования, попробуйте завтра')
        time.sleep(300)
    driver.quit()
    #добавить првоерку на сохранеие


if __name__ == '__main__':
    main()