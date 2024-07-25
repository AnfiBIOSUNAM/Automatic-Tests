from selenium import webdriver
from configparser import ConfigParser
from unittest import TestCase
from helper.getBrowser import get_browser
import time

def before_all(context):
    context.test = TestCase()

    config = ConfigParser()
    config.read("setup.cfg")
    context.config = config

    browser_name = context.config.get("Browser", "navegador")
    context.driver = get_browser(browser_name)
    
    width = context.config.getint("Browser", "width")
    height = context.config.getint("Browser", "height")
    context.driver.set_window_size(width, height)
    context.driver.implicitly_wait(5)

def after_all(context):
    time.sleep(5)
    context.driver.quit()
    
