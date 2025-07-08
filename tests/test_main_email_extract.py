import pytest
from unittest.mock import patch
from src.get_papers.main import extract_email


def test_extract_email():
    text = "Contact us at hello@pharma.com for more info."
    assert extract_email(text) == "hello@pharma.com"

    text2 = "No email here."
    assert extract_email(text2) == "N/A"