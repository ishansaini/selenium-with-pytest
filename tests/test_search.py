"""
These tests cover DuckDuckGo searches.
"""
import pytest
from pages.results import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage

# phrase = "panda"

@pytest.mark.parametrize("phrase", ["panda"])
def test_basic_duckduckgo_search(browser, phrase):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for "panda"
    search_page.search(phrase)

    # Then the search result query is "panda"
    assert phrase == result_page.search_input_value()

    # And the search result links pertain to "panda"
    for title in result_page.result_link_titles():
        assert phrase.lower() in title.lower()

    # And the search result title contains "panda"
    assert phrase in result_page.title()
