# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver= webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get("https://prueba.undostres.com.mx")
time.sleep(5)
driver.find_element(By.NAME, 'operator').click()
driver.find_element(By.XPATH,"//*[@data-name='telcel']").click()

driver.find_element(By.NAME,'mobile').send_keys('5523261151')
driver.find_element(By.NAME, 'amount').click()
driver.find_element(By.XPATH,'(//*[@class="main-info data-value"])[1]').click()
driver.find_element(By.XPATH, '//*[@class="button buttonRecharge"]').click()
try:
    element_present = EC.presence_of_element_located((By.ID, 'payment-form'))
    WebDriverWait(driver,5).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")
finally:

    #  is_displayed() will check the presence of "Pagar con Tarjeta" button to verify the payment page.
    driver.find_element(By.XPATH,"(//*[@name='formsubmit'])[1]").is_displayed()
    driver.find_element(By.XPATH, '(//*[@class="form-control cardname"])[2]').send_keys('test')
    driver.find_element(By.XPATH, '(//*[@class="form-control cardnumber"])[2]').send_keys('4111111111111111')
    driver.find_element(By.XPATH, '(//*[@class="form-control expmonth"])[2]').send_keys('11')
    driver.find_element(By.XPATH, '(//*[@class="form-control expyear"])[2]').send_keys('2025')
    driver.find_element(By.XPATH, '(//*[@class="form-control cvv"])[2]').send_keys('111')

    driver.find_element(By.XPATH, '//*[@class="form-control email"]').send_keys('test@test.com')
    driver.find_element(By.ID, 'paylimit').click()
    time.sleep(5)

    driver.find_element(By.XPATH,'//*[@id="usrname"]').send_keys('automationexcersise@test.com')
    driver.find_element(By.XPATH, '//*[@id="psw"]').send_keys('123456')
    time.sleep(5)

    #Switch to the iframe to click on captcha

    iframe = driver.find_element(By.XPATH, "(//iframe[contains(@src,'recaptcha/api2')])[1]")
    driver.switch_to.frame(iframe)
    driver.find_element(By.XPATH,'//*[@class="recaptcha-checkbox-border"]').click()
    driver.switch_to.default_content()

    time.sleep(5)
    driver.find_element(By.XPATH,'//*[@id="loginBtn"]').click()

    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//*[@class='col-sm-10']"))
        WebDriverWait(driver, 5).until(element_present)

    except TimeoutException:
        print("Timed out waiting for page to load")
    finally:
        print("process suceessful")
        time.sleep(2)
        string_msg = driver.find_element(By.XPATH,"//span[contains(@class, 'recharge-status')]").text
        print(string_msg)

        # Verify whether "Success" message is being displayed or not
        assert string_msg == '¡Exitosa!'

