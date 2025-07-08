import requests
import xml.etree.ElementTree as ET
from typing import List, Tuple, Dict

# function responsible for fetching pubmed ids
def fetch_pubmed_ids(query: str) -> List[str]:
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed", # database name
        "term": query,
        "retmax": 20
    }
    res = requests.get(url, params=params)
    tree = ET.fromstring(res.text)
    return [id_elem.text for id_elem in tree.findall(".//Id")]

# function responsiable for fetching paper details based on pubmedids
def fetch_paper_details(pubmub_ids: List[str]) -> List[Dict]:
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(pubmub_ids),
        "retmode": "xml"
    }
    res = requests.get(url, params=params)
    root = ET.fromstring(res.text)

    results = [] # list to store results
    for article in root.findall(".//PubmedArticle"):
        pmid = article.findtext(".//PMID")
        title = article.findtext(".//ArticleTitle", default="No Title")
        date = article.findtext(".//PubDate/Year", default="Unknown")
        affiliations = article.findall(".//AffiliationInfo")

        non_academic_authors = []
        company_names = []

        for affiliation in affiliations:
            affiliation_text = affiliation.findtext("Affiliation", default="").lower()
            if not any(x in affiliation_text for x in ["university", "college", "research", "school", "institute"]): # filtering the article by affiliation
                if any(x in affiliation_text for x in ["pharma", "biotech", "inc", "ltd", "corp"]):
                    company_names.append(affiliation_text)
                    non_academic_authors.append(affiliation_text)

        email = None
        if "@" in str(affiliations):
            email = extract_email(str(affiliations)) # extracting email

        # adding result
        results.append({
            "PubmedID": pmid,
            "Title": title,
            "Publication Date": date,
            "Non-academic Author(s)": "; ".join(set(non_academic_authors)),
            "Company Affiliation(s)": "; ".join(set(company_names)),
            "Corresponding Author Email": email or "N/A"
        }) 

    return results

# function for email extraction
def extract_email(text: str) -> str:
    import re
    match = re.search(r"[\w\.-]+@[\w\.-]+", text) # email regular expression to match string
    return match.group(0) if match else "N/A"