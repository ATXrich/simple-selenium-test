"""
These tests cover DuckDuckGo searches.
"""

import pytest

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


@pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])
def test_basic_duckduckgo_search(browser, phrase):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for phrase
    search_page.search(phrase)

     # And the search result query is phrase
    assert phrase == result_page.search_input_values()

    # And the search result links pertain to phrase
    for title in result_page.result_link_titles():
        assert phrase.lower() in title.lower()

    # Then the search result title contains phrase
    assert phrase in result_page.title()

    # This exception can be removed after the test is fully implemented.
    # raise Exception("Incomplete Test")

