import pytest
from unittest.mock import patch 
from src.get_papers.main import fetch_pubmed_ids

SAMPLE_ESEARCH_XML = """
<eSearchResult>
    <IdList>
        <Id>123456</Id>
        <Id>789012</Id>
    </IdList>
</eSearchResult>
"""

@patch("src.get_papers.main.requests.get")
def test_fetch_pubmed_ids(mock_get):
    mock_get.return_value.text = SAMPLE_ESEARCH_XML
    ids = fetch_pubmed_ids("cancer")
    assert ids == ["123456", "789012"]