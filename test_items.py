from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"



def test_guest_should_see_basket_link_on_the_main_page(browser):
    browser.get(link)
    assert browser.find_element(By.ID, "add_to_basket_form")
    
    
