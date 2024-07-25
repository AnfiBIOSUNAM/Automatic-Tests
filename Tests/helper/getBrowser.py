from selenium import webdriver

# This function will return a browser object based on the name of the browser
def get_browser(browser_name):
    browser_name = browser_name.lower()
    if browser_name == 'chrome':
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
        return driver
    elif browser_name == 'firefox':
        options = webdriver.FirefoxOptions()
        options.binary_location = '/snap/firefox/current/usr/lib/firefox/firefox'
        driver = webdriver.Firefox(options=options)
        return driver
    elif browser_name == 'edge':
        options = webdriver.EdgeOptions()
        driver = webdriver.Edge(options=options)
        return driver
    else:
        raise Exception(f'Browser "{browser_name}" is not supported')
    