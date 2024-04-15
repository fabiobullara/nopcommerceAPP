from selenium import webdriver
import pytest
''' This block of code will be modified to run multiple browsers
@pytest.fixture()
def setup():
    driver=webdriver.Chrome()
    return driver
'''
@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver=webdriver.Chrome()
        print("Launching Chrome browser . . .")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser . . .")
    else:
        driver = webdriver.Edge()
        print("Launching Edge (default) browser . . .")
    return driver

def pytest_addoption(parser):           # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):                   # This will return the Browser value to setup method
    return request.config.getoption("--browser")
'''
########################## PyTest HTML Report (failing video code) ##########################

# This is a hook for Adding Environment info to the HTML Report
def pytest_configure(config):           # These are customizable, where we can add or remove them as needed
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Pavan'

# This is a hook to Delete/Modify Environment info to the HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):          # Allows us to remove what we don't want to see in the HTML Report
    metadata.pop("JAVA_HOME", None)     # None, because it's not needed in the report
    metadata.pop("Plugins", None)       # None, because it's not needed in the report
'''
########################## PyTest HTML Report (Corrected in Video Comments) ##########################

# This is a hook for Adding Environment info to the HTML Report
def pytest_configure(config):
    metadata = config.pluginmanager.getplugin("metadata")
    if metadata:
        from pytest_metadata.plugin import metadata_key
        config.stash[metadata_key]['Project Name'] = 'nop Commerce'
        config.stash[metadata_key]['Module Name'] = 'Customers'
        config.stash[metadata_key]['Tester'] = 'Durga Prasad Devarakonda'

# This is a hook to Delete/Modify Environment info to the HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
