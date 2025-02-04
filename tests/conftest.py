"""
This module contains fixtures that are used by the tests.
"""

import pytest
import selenium.webdriver


@pytest.fixture
def browser():

    # Initialize the ChromeDriver instance
    driver = selenium.webdriver.Chrome()

    # Make its calls wait for elements to appear
    driver.implicitly_wait(10)

    # Return the WebDriver instance for the setup
    yield driver

    # Quit the WebDriver instance for the cleanup
    driver.quit()
    