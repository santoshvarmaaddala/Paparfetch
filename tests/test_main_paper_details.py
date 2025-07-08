import pytest
from unittest.mock import patch 
from src.get_papers.main import fetch_paper_details

SAMPLE_EFETCH_XML = """
<PubmedArticleSet>
    <PubmedArticle>
        <MedlineCitation>
            <PMID>123456</PMID>
            <Article>
                <ArticleTitle>Test Title</ArticleTitle>
                <Journal>
                    <JournalIssue>
                        <PubDate>
                            <Year>2024</Year>
                        </PubDate>
                    </JournalIssue>
                </Journal>
                <AuthorList>
                    <Author>
                        <AffiliationInfo>
                            <Affiliation>Test Biotech Inc., USA. author@example.com</Affiliation>
                        </AffiliationInfo>
                    </Author>
                </AuthorList>
            </Article>
        </MedlineCitation>
    </PubmedArticle>
</PubmedArticleSet>
"""

@patch("get_papers.main.requests.get")
def test_fetch_paper_details(mock_get):
    mock_get.return_value.text = SAMPLE_EFETCH_XML
    result = fetch_paper_details(["123456"])

    assert len(result) == 1
    assert result[0]["PubmedID"] == "123456"
    assert result[0]["Title"] == "Test Title"
    assert result[0]["Publication Date"] == "2024"
    assert "biotech" in result[0]["Company Affiliation(s)"].lower()
    assert result[0]["Corresponding Author Email"] == "author@example.com"
