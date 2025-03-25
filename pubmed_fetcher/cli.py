import argparse
import sys
from .fetcher import fetch_pubmed_papers, get_paper_details, save_to_csv


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Fetch PubMed papers with non-academic authors.")
    parser.add_argument("query", help="PubMed search query")
    parser.add_argument("-f", "--file", help="Output CSV filename")
    parser.add_argument("-d", "--debug", action="store_true",
                        help="Print debug info")
    return parser.parse_args()


def main() -> None:
    """Main function to run the CLI."""
    args = parse_args()

    if args.debug:
        print(f"Query: {args.query}")

    try:
        pubmed_ids = fetch_pubmed_papers(args.query)
        if not pubmed_ids:
            print("No papers found for the query.")
            sys.exit(1)

        if args.debug:
            print(f"Found {len(pubmed_ids)} papers")

        papers = get_paper_details(pubmed_ids)

        if not papers:
            print("No papers with non-academic authors found.")
            sys.exit(1)

        if args.file:
            save_to_csv(papers, args.file)
            print(f"Results saved to {args.file}")
        else:
            for paper in papers:
                print(paper)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
