import logging
import unittest
import time
import re

from selenium import webdriver
from selenium.webdriver.support.select import Select

import logging.config


class TestForm(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:/Users/vladi_000/chromedriver.exe')
        logging.config.fileConfig('logger_config.conf')
        logger = logging.getLogger("test00")
        logger.info("Test started")

    # Все данные верны
    def test_form_00(self):
        NAME = 'Alex'
        FNAME = 'IVANOV'
        BDAY = '17/12/1994'
        RECRUIT_DAY = '15/01/2019'

        logger = logging.getLogger("test")
        logger.info("Test 00")
        driver = self.driver

        driver.get('https://mysite.ru/new_worker')
        time.sleep(3)

        name = driver.find_element_by_id("index_name")
        fname = driver.find_element_by_id("index_fname")
        second_name = driver.find_element_by_id("index_patr")
        datepicker_bday = driver.find_element_by_id("birth")
        datepicker_recruit = driver.find_element_by_id("recruit")
        datepicker_dis = driver.find_element_by_id("dismissal")
        btn_save = driver.find_element_by_id("save")
        btn_cancel = driver.find_element_by_id("cancel")

        name.send_keys(NAME)
        logger.info("name added")
        fname.send_keys(FNAME)
        logger.info("fname added")

        datepicker_bday.click()
        month = driver.find_element_by_xpath("//div/select[@class='ui-datepicker-month']")
        select_month = Select(month)
        select_month.select_by_visible_text("December")

        year = driver.find_element_by_xpath("//div/select[@class='ui-datepicker-year']")
        select_year = Select(year)
        select_year.select_by_visible_text("1994")

        day_from = driver.find_element_by_xpath("//table/tbody/tr/td/a[text()='17']")
        day_from.click()

        logger.info("bday picked")

        bday_string = datepicker_bday.get_attribute('value')
        try:
            self.assertEqual(bday_string, BDAY)
            logger.info("bday date correct")
        except:
            logger.info("bday date is not correct")

        datepicker_recruit.click()
        month = driver.find_element_by_xpath("//div/select[@class='ui-datepicker-month']")
        select_month = Select(month)
        select_month.select_by_visible_text("January")

        year = driver.find_element_by_xpath("//div/select[@class='ui-datepicker-year']")
        select_year = Select(year)
        select_year.select_by_visible_text("2019")

        day_from = driver.find_element_by_xpath("//table/tbody/tr/td/a[text()='15']")
        day_from.click()

        logger.info("recruit day picked")

        recday_string = datepicker_bday.get_attribute('value')
        try:
            self.assertEqual(recday_string, RECRUIT_DAY)
            logger.info("recruit date correct")
        except:
            logger.info("recruit date is not correct")

        btn_save.click()
        logger.info("button 'save' clicked")

        src = driver.page_source
        text_found = re.search(r'Данные сохранены', src)
        if text_found:
            logger.info("failed save")
        else:
            logger.info("sucsess save")

        text_found_nm = re.search(NAME, src)
        text_found_fnm = re.search(FNAME, src)
        text_found_bday = re.search(BDAY, src)
        text_found_rec = re.search(RECRUIT_DAY, src)
        text_header = re.search(r'Создание нового сотрудника', src)
        if text_found_nm or text_found_fnm or text_found_bday or text_found_rec:
            logger.info("form not clear")
        if text_header == False:
            logger.info("form closed")

    # Не заполнено обязательное поле NAME
    def test_form_01(self):
        NAME = ''
        FNAME = 'IVANOV'
        BDAY = '17/12/1994'
        RECRUIT_DAY = '15/01/2019'

        logger = logging.getLogger("test")
        logger.info("Test 01")
        driver = self.driver

        driver.get('https://mysite.ru/new_worker')
        time.sleep(3)

        name = driver.find_element_by_id("index_name")
        fname = driver.find_element_by_id("index_fname")
        second_name = driver.find_element_by_id("index_patr")
        datepicker_bday = driver.find_element_by_id("birth")
        datepicker_recruit = driver.find_element_by_id("recruit")
        datepicker_dis = driver.find_element_by_id("dismissal")
        btn_save = driver.find_element_by_id("save")
        btn_cancel = driver.find_element_by_id("cancel")

        name.send_keys(NAME)
        logger.info("name added")
        fname.send_keys(FNAME)
        logger.info("fname added")

        datepicker_bday.click()
        month = driver.find_element_by_xpath("//div/select[@class='ui-datepicker-month']")
        select_month = Select(month)
        select_month.select_by_visible_text("December")

        year = driver.find_element_by_xpath("//div/select[@class='ui-datepicker-year']")
        select_year = Select(year)
        select_year.select_by_visible_text("1994")

        day_from = driver.find_element_by_xpath("//table/tbody/tr/td/a[text()='17']")
        day_from.click()

        logger.info("bday picked")

        bday_string = datepicker_bday.get_attribute('value')
        try:
            self.assertEqual(bday_string, BDAY)
            logger.info("bday date correct")
        except:
            logger.info("bday date is not correct")

        datepicker_recruit.click()
        month = driver.find_element_by_xpath("//div/select[@class='ui-datepicker-month']")
        select_month = Select(month)
        select_month.select_by_visible_text("January")

        year = driver.find_element_by_xpath("//div/select[@class='ui-datepicker-year']")
        select_year = Select(year)
        select_year.select_by_visible_text("2019")

        day_from = driver.find_element_by_xpath("//table/tbody/tr/td/a[text()='15']")
        day_from.click()

        logger.info("recruit day picked")

        recday_string = datepicker_bday.get_attribute('value')
        try:
            self.assertEqual(recday_string, RECRUIT_DAY)
            logger.info("recruit date correct")
        except:
            logger.info("recruit date is not correct")

        btn_save.click()
        logger.info("button 'save' clicked")

        src = driver.page_source
        text_found = re.search(r'Данные сохранены', src)
        print(text_found)
        if text_found:
            logger.info("failed save")
        else:
            logger.info("sucsess save")

        text_found_fnm = re.search(FNAME, src)
        text_found_bday = re.search(BDAY, src)
        text_found_rec = re.search(RECRUIT_DAY, src)
        text_header = re.search(r'Создание нового сотрудника', src)
        if text_found_fnm or text_found_bday or text_found_rec:
            logger.info("form not clear")
        if text_header == False:
            logger.info("form closed")

    # Дата рождения < даты приема на работу
    def test_form_02(self):
        NAME = 'Alex'
        FNAME = 'IVANOV'
        BDAY = '17/12/2015'
        RECRUIT_DAY = '15/01/2014'

        logger = logging.getLogger("test")
        logger.info("Test 02")
        driver = self.driver

        driver.get('https://mysite.ru/new_worker')
        time.sleep(3)

        name = driver.find_element_by_id("index_name")
        fname = driver.find_element_by_id("index_fname")
        second_name = driver.find_element_by_id("index_patr")
        datepicker_bday = driver.find_element_by_id("birth")
        datepicker_recruit = driver.find_element_by_id("recruit")
        datepicker_dis = driver.find_element_by_id("dismissal")
        btn_save = driver.find_element_by_id("save")
        btn_cancel = driver.find_element_by_id("cancel")

        name.send_keys(NAME)
        logger.info("name added")
        fname.send_keys(FNAME)
        logger.info("fname added")

        datepicker_bday.click()
        month = driver.find_element_by_xpath("//div/select[@class='ui-datepicker-month']")
        select_month = Select(month)
        select_month.select_by_visible_text("December")

        year = driver.find_element_by_xpath("//div/select[@class='ui-datepicker-year']")
        select_year = Select(year)
        select_year.select_by_visible_text("2015")

        day_from = driver.find_element_by_xpath("//table/tbody/tr/td/a[text()='17']")
        day_from.click()

        logger.info("bday picked")

        bday_string = datepicker_bday.get_attribute('value')
        try:
            self.assertEqual(bday_string, BDAY)
            logger.info("bday date correct")
        except:
            logger.info("bday date is not correct")

        datepicker_recruit.click()
        month = driver.find_element_by_xpath("//div/select[@class='ui-datepicker-month']")
        select_month = Select(month)
        select_month.select_by_visible_text("January")

        year = driver.find_element_by_xpath("//div/select[@class='ui-datepicker-year']")
        select_year = Select(year)
        select_year.select_by_visible_text("2014")

        day_from = driver.find_element_by_xpath("//table/tbody/tr/td/a[text()='15']")
        day_from.click()

        logger.info("recruit day picked")

        recday_string = datepicker_bday.get_attribute('value')
        try:
            self.assertEqual(recday_string, RECRUIT_DAY)
            logger.info("recruit date correct")
        except:
            logger.info("recruit date is not correct")

        btn_save.click()
        logger.info("button 'save' clicked")

        src = driver.page_source
        text_found = re.search(r'Данные сохранены', src)
        print(text_found)
        if text_found:
            logger.info("failed save")
        else:
            logger.info("sucsess save")

        text_found_nm = re.search(NAME, src)
        text_found_fnm = re.search(FNAME, src)
        text_found_bday = re.search(BDAY, src)
        text_found_rec = re.search(RECRUIT_DAY, src)
        text_header = re.search(r'Создание нового сотрудника', src)
        if text_found_nm or text_found_fnm or text_found_bday or text_found_rec:
            logger.info("form not clear")
        if text_header == False:
            logger.info("form closed")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
