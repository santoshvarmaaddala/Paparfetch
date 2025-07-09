# 🧪 PubMEd-CLI-Tool

A Python command-line tool that fetches PubMed research articles based on a search query, extracts metadata, and filters for non-academic pharmaceutical authors. Outputs can be saved in CSV format.

---

## 🚀 Features

- 🔍 Search PubMed articles using any keyword or phrase
- 🧬 Extract metadata including:
  - PubMed ID
  - Title
  - Publication Year
  - Company/Pharma-affiliated authors
  - Corresponding author email
- 📄 Save results to CSV or print to console
- 🐍 Built and managed with [Poetry](https://python-poetry.org)

---

## 📦 Installation

1. **Clone the project**
   ```bash
   git clone https://github.com/santoshvarmaaddala/Paper-Fetch
   cd get_papers
   ```

2. **Install dependencies**
   ```bash
   poetry install
   ```

## 🔧 Usage
 **Search and print results**
  ```bash
  poetry run get-papers-list "cancer pharma"
  ```
  **Search and save to CSV**
  ```bash
  poetry run get-papers-list "covid-19" -f covid_results.csv
  ```
  **Enable debug logs**
  ```bash
  poetry run get-papers-list "diabetes biotech" -d
  ```

## 🧪 Testing
To run the test suite:

```bash
poetry run pytest
```
Unit tests are located in the ``tests/`` directory and cover:
 - PubMed ID fetching
 - Paper detail parsing
 - Email extraction logic

## 📁 Project Structure
```
get_papers/
├── src/
│   └── get_papers/
        ├── cli.py         # CLI entry point
│       ├── main.py        # Core logic for fetching & parsing
│       └── __init__.py    
├── tests/
│   └── test_*.py          # Modular tests per feature
├── pyproject.toml         # Poetry config
└── README.md
```

## Requirements
  - Python 3.12+
  - Poetry

## Author
Santosh Varma Addala – santoshvarma2166@gmail.com
Github - https://github.com/santoshvarmaaddala
