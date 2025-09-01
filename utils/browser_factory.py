from selenium import webdriver


def get_browser(browser_name="firefox"):
    if browser_name == "firefox":
        return webdriver.Firefox()
    elif browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        return webdriver.Chrome(options=options)
    elif browser_name == "edge":
        return webdriver.Edge()
    else:
        return ValueError("unsupported browser")