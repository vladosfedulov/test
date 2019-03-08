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
        self.driver.get('https://mysite.ru/new_worker')
        
        self.name = self.driver.find_element_by_id("index_name")
        self.fname = self.driver.find_element_by_id("index_fname")
        self.second_name = self.driver.find_element_by_id("index_patr")
        self.datepicker_bday = self.driver.find_element_by_id("birth")
        self.datepicker_recruit = self.driver.find_element_by_id("recruit")
        self.datepicker_dis = self.driver.find_element_by_id("dismissal")
        self.btn_save = self.driver.find_element_by_id("save")
        self.btn_cancel = self.driver.find_element_by_id("cancel")
        
        logging.config.fileConfig('logger_config.conf')
        self.logger = logging.getLogger("test")
        self.logger.info("Test started")

    # Все данные верны
    def test_form_00(self):
        NAME = 'Alex'
        FNAME = 'IVANOV'
        BDAY = '17/12/1994'
        RECRUIT_DAY = '15/01/2019'

        self.logger.info("Test 00")

        self.name.send_keys(NAME)
        self.logger.info("name added")
        self.fname.send_keys(FNAME)
        self.logger.info("fname added")

        self.datepicker_bday.click()
        month = self.driver.find_element_by_xpath("//div/select[@class='ui-datepicker-month']")
        select_month = Select(month)
        select_month.select_by_visible_text("December")

        year = self.driver.find_element_by_xpath("//div/select[@class='ui-datepicker-year']")
        select_year = Select(year)
        select_year.select_by_visible_text("1994")

        day_from = self.driver.find_element_by_xpath("//table/tbody/tr/td/a[text()='17']")
        day_from.click()

        self.logger.info("bday picked")

        bday_string = self.datepicker_bday.get_attribute('value')
        try:
            self.assertEqual(bday_string, BDAY)
            self.logger.info("bday date correct")
        except:
            self.logger.info("bday date is not correct")

        self.datepicker_recruit.click()
        month = self.driver.find_element_by_xpath("//div/select[@class='ui-datepicker-month']")
        select_month = Select(month)
        select_month.select_by_visible_text("January")

        year = self.driver.find_element_by_xpath("//div/select[@class='ui-datepicker-year']")
        select_year = Select(year)
        select_year.select_by_visible_text("2019")

        day_from = self.driver.find_element_by_xpath("//table/tbody/tr/td/a[text()='15']")
        day_from.click()

        self.logger.info("recruit day picked")

        recday_string = self.datepicker_bday.get_attribute('value')
        try:
            self.assertEqual(recday_string, RECRUIT_DAY)
            self.logger.info("recruit date correct")
        except:
            self.logger.info("recruit date is not correct")

        self.btn_save.click()
        self.logger.info("button 'save' clicked")

        src = self.driver.page_source
        text_found = re.search(r'Данные сохранены', src)
        if text_found:
            self.logger.info("failed save")
        else:
            self.logger.info("sucsess save")

        text_found_nm = re.search(NAME, src)
        text_found_fnm = re.search(FNAME, src)
        text_found_bday = re.search(BDAY, src)
        text_found_rec = re.search(RECRUIT_DAY, src)
        text_header = re.search(r'Создание нового сотрудника', src)
        if text_found_nm or text_found_fnm or text_found_bday or text_found_rec:
            self.logger.info("form not clear")
        if text_header == False:
            self.logger.info("form closed")

    # Не заполнено обязательное поле NAME
    def test_form_01(self):
        NAME = ''
        FNAME = 'IVANOV'
        BDAY = '17/12/1994'
        RECRUIT_DAY = '15/01/2019'

        self.logger.info("Test 00")

        self.name.send_keys(NAME)
        self.logger.info("name added")
        self.fname.send_keys(FNAME)
        self.logger.info("fname added")

        self.datepicker_bday.click()
        month = self.driver.find_element_by_xpath("//div/select[@class='ui-datepicker-month']")
        select_month = Select(month)
        select_month.select_by_visible_text("December")

        year = self.driver.find_element_by_xpath("//div/select[@class='ui-datepicker-year']")
        select_year = Select(year)
        select_year.select_by_visible_text("1994")

        day_from = self.driver.find_element_by_xpath("//table/tbody/tr/td/a[text()='17']")
        day_from.click()

        self.logger.info("bday picked")

        bday_string = self.datepicker_bday.get_attribute('value')
        try:
            self.assertEqual(bday_string, BDAY)
            self.logger.info("bday date correct")
        except:
            self.logger.info("bday date is not correct")

        self.datepicker_recruit.click()
        month = self.driver.find_element_by_xpath("//div/select[@class='ui-datepicker-month']")
        select_month = Select(month)
        select_month.select_by_visible_text("January")

        year = self.driver.find_element_by_xpath("//div/select[@class='ui-datepicker-year']")
        select_year = Select(year)
        select_year.select_by_visible_text("2019")

        day_from = self.driver.find_element_by_xpath("//table/tbody/tr/td/a[text()='15']")
        day_from.click()

        self.logger.info("recruit day picked")

        recday_string = self.datepicker_bday.get_attribute('value')
        try:
            self.assertEqual(recday_string, RECRUIT_DAY)
            self.logger.info("recruit date correct")
        except:
            self.logger.info("recruit date is not correct")

        self.btn_save.click()
        self.logger.info("button 'save' clicked")

        src = self.driver.page_source
        text_found = re.search(r'Данные сохранены', src)
        if text_found:
            self.logger.info("failed save")
        else:
            self.logger.info("sucsess save")

        text_found_nm = re.search(NAME, src)
        text_found_fnm = re.search(FNAME, src)
        text_found_bday = re.search(BDAY, src)
        text_found_rec = re.search(RECRUIT_DAY, src)
        text_header = re.search(r'Создание нового сотрудника', src)
        if text_found_nm or text_found_fnm or text_found_bday or text_found_rec:
            self.logger.info("form not clear")
        if text_header == False:
            self.logger.info("form closed")

        
    # Дата рождения < даты приема на работу
    def test_form_02(self):
        NAME = 'Alex'
        FNAME = 'IVANOV'
        BDAY = '17/12/2015'
        RECRUIT_DAY = '15/01/2014'

        self.logger.info("Test 00")

        self.name.send_keys(NAME)
        self.logger.info("name added")
        self.fname.send_keys(FNAME)
        self.logger.info("fname added")

        self.datepicker_bday.click()
        month = self.driver.find_element_by_xpath("//div/select[@class='ui-datepicker-month']")
        select_month = Select(month)
        select_month.select_by_visible_text("December")

        year = self.driver.find_element_by_xpath("//div/select[@class='ui-datepicker-year']")
        select_year = Select(year)
        select_year.select_by_visible_text("1994")

        day_from = self.driver.find_element_by_xpath("//table/tbody/tr/td/a[text()='17']")
        day_from.click()

        self.logger.info("bday picked")

        bday_string = self.datepicker_bday.get_attribute('value')
        try:
            self.assertEqual(bday_string, BDAY)
            self.logger.info("bday date correct")
        except:
            self.logger.info("bday date is not correct")

        self.datepicker_recruit.click()
        month = self.driver.find_element_by_xpath("//div/select[@class='ui-datepicker-month']")
        select_month = Select(month)
        select_month.select_by_visible_text("January")

        year = self.driver.find_element_by_xpath("//div/select[@class='ui-datepicker-year']")
        select_year = Select(year)
        select_year.select_by_visible_text("2019")

        day_from = self.driver.find_element_by_xpath("//table/tbody/tr/td/a[text()='15']")
        day_from.click()

        self.logger.info("recruit day picked")

        recday_string = self.datepicker_bday.get_attribute('value')
        try:
            self.assertEqual(recday_string, RECRUIT_DAY)
            self.logger.info("recruit date correct")
        except:
            self.logger.info("recruit date is not correct")

        self.btn_save.click()
        self.logger.info("button 'save' clicked")

        src = self.driver.page_source
        text_found = re.search(r'Данные сохранены', src)
        if text_found:
            self.logger.info("failed save")
        else:
            self.logger.info("sucsess save")

        text_found_nm = re.search(NAME, src)
        text_found_fnm = re.search(FNAME, src)
        text_found_bday = re.search(BDAY, src)
        text_found_rec = re.search(RECRUIT_DAY, src)
        text_header = re.search(r'Создание нового сотрудника', src)
        if text_found_nm or text_found_fnm or text_found_bday or text_found_rec:
            self.logger.info("form not clear")
        if text_header == False:
            self.logger.info("form closed")

        
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
