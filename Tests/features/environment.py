from selenium import webdriver
from configparser import ConfigParser
from unittest import TestCase
from helper.getBrowser import get_browser

def before_all(context):
    # Read the configuration file
    config = ConfigParser()
    config.read('setup.cfg')
    
    context.test = TestCase()
    context.config = config # Save the configuration object to the context
    # Get the browser name from the configuration file
    context.driver = get_browser(context.config.get('Browser', 'browser'))
    # Set the implicit wait time
    context.driver.implicitly_wait(10)
    # Set the window size
    context.driver.set_window_size(context.config.get('Browser', 'width'), context.config.get('Browser', 'height'))
    
    
def after_all(context):
    context.driver.quit()