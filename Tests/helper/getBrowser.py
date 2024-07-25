from selenium import webdriver

def get_browser(browser_name):
    browser_name=browser_name.lower()
    

    if browser_name == "firefox":
        options = webdriver.FirefoxOptions()

        driver = webdriver.Firefox(options=options)
    elif browser_name == "chrome":
         options = webdriver.ChromeOptions()

         driver = webdriver.Chrome(options=options)
    else:
        options = webdriver.EdgeOptions()

        driver = webdriver.Edge(options=options)

    
    return driver

