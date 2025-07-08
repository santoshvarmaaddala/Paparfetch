import argparse
import csv
from src.get_papers.main import fetch_paper_details, fetch_pubmed_ids

# entry point for cmd line tool
def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers for pharma authors.")

    # arguments or flags 
    parser.add_argument("query", help="Search query for PubMed")
    parser.add_argument("-d", "--debug", action="store_true")
    parser.add_argument("-f", "--file", help="Output CSV filename")

    args = parser.parse_args()

    ids = fetch_pubmed_ids(args.query) # extracted pubmedids
    if args.debug:
        print(f"Found PubMed IDs: {ids}")

    results = fetch_paper_details(ids) # extracted papaer details
    if args.file:
        with open(args.file, "w", newline="", encoding="utf-8") as f: # writing results into csv file
            writer = csv.DictWriter(f, fieldnames=results[0].keys())
            writer.writeheader()
            writer.writerows(results)
    else:
        for row in results: 
            print(row)

if __name__ == '__main__':
    main()