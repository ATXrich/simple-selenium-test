"""
This module contains DuckDuckGo result page object.
"""

from selenium.webdriver.common.by import By

class DuckDuckGoResultPage:

    RESULTS_LINKS = (By.CSS_SELECTOR, 'a.result__a')
    SEARCH_INPUT = (By.ID, 'search_form_input')

    def __init__(self, browser):
        self.browser = browser

    def result_link_titles(self):
        links = self.browser.find_elements(*self.RESULTS_LINKS)
        titles = [link.text for link in links]
        return titles

    def search_input_values(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        return value

    def title(self):
        return self.browser.title
    