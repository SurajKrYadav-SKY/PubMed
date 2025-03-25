from typing import List, Dict, Optional
import requests
from Bio import Entrez
import pandas as pd

Entrez.email = "sk.mails99@gmail.com"  # Your email


def fetch_pubmed_papers(query: str, max_results: int = 100) -> List[Dict]:
    """Fetch papers from PubMed based on a query."""
    handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
    record = Entrez.read(handle)
    handle.close()
    return record["IdList"]


def get_paper_details(pubmed_ids: List[str]) -> List[Dict]:
    """Fetch details for a list of PubMed IDs."""
    handle = Entrez.efetch(db="pubmed", id=",".join(pubmed_ids), retmode="xml")
    papers = Entrez.read(handle)["PubmedArticle"]
    handle.close()

    # List of pharma/biotech indicators
    pharma_keywords = {"pfizer", "novartis", "roche", "merck", "gsk", "astrazeneca", "bayer", "sanofi",
                       "inc", "ltd", "pharma", "biotech", "biogen", "amgen", "eli lilly"}

    results = []
    for paper in papers:
        authors = paper["MedlineCitation"]["Article"].get("AuthorList", [])
        if not authors:
            continue

        non_academic_authors = []
        company_affiliations = set()  # Use set to avoid duplicates
        for author in authors:
            affil_info = author.get("AffiliationInfo", [{}])
            affil = affil_info[0].get("Affiliation", "") if affil_info else ""
            if affil:
                affil_lower = affil.lower()
                # Check for pharma/biotech indicators instead of just excluding university/edu
                if any(keyword in affil_lower for keyword in pharma_keywords):
                    name = f"{author.get('ForeName', '')} {author.get('LastName', '')}".strip(
                    )
                    non_academic_authors.append(name)
                    company_affiliations.add(affil.split(",")[0].strip())

        if non_academic_authors:
            result = {
                # Convert StringElement to str
                "PubmedID": str(paper["MedlineCitation"]["PMID"]),
                "Title": paper["MedlineCitation"]["Article"]["ArticleTitle"],
                "Publication Date": paper["MedlineCitation"]["Article"].get("Journal", {}).get("JournalIssue", {}).get("PubDate", {}).get("Year", "Unknown"),
                "Non-academic Author(s)": "; ".join(non_academic_authors),
                "Company Affiliation(s)": "; ".join(company_affiliations),
                "Corresponding Author Email": "N/A"
            }
            results.append(result)

    return results


def save_to_csv(data: List[Dict], filename: str) -> None:
    """Save the results to a CSV file."""
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
