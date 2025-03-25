# PubMed Fetcher

A Python tool to fetch research papers from PubMed with at least one author affiliated with a pharmaceutical or biotech company, returning the results as a CSV file or console output.

## Code Organization

- **`pubmed_fetcher/`**: Main package directory.
  - **`__init__.py`**: Marks the directory as a Python package.
  - **`fetcher.py`**: Core logic for querying the PubMed API, processing paper details, and saving results to CSV.
  - **`cli.py`**: Command-line interface (CLI) handling user inputs and program execution.

## Installation

To set up the project on your system, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd pubmed-fetcher
   ```

Replace `<repository-url>` with the GitHub URL once you host it.

2. **Install Python**:
   Ensure Python 3.10 or higher is installed:

   ```bash
   python --version
   ```

   Download from [python.org](https://www.python.org) if needed.

3. **Install Poetry**:
   Install Poetry for dependency management:

   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

   Add Poetry to your PATH as instructed during installation (e.g., update your shell config or Windows environment variables).

4. **Install Dependencies**:
   Run Poetry to set up the virtual environment and install dependencies:
   ```bash
   poetry install
   ```

## Usage

The program is run via the `get-papers-list` command using Poetry. It accepts a PubMed query and optional arguments.

### Step-by-Step Instructions to Test on Your System

1. **Navigate to the Project Directory**:
   Open a terminal and change to the project folder:

   ```bash
   cd path/to/pubmed-fetcher
   ```

   Replace `path/to/pubmed-fetcher` with the actual path where you cloned the repo.

2. **Activate the Poetry Shell (Optional)**:
   To use Poetry commands without prefixing `poetry.exe run`:

   ```bash
   poetry shell
   ```

   If you skip this, prepend `poetry.exe run` to the commands below.

3. **Set Your Email**:
   Open `pubmed_fetcher/fetcher.py` in a text editor and replace:

   ```python
   Entrez.email = "abc@gmail.com"
   ```

   with your email address (required by the PubMed API).

4. **Run a Test Query**:
   Fetch papers for "cancer therapy" with debug output:

   ```bash
   poetry.exe run get-papers-list "cancer therapy" -d
   ```

   - Expected output: Console prints paper details for those with pharma/biotech authors.

5. **Save Results to CSV**:
   Save the results to a file named `results.csv`:

   ```bash
   poetry.exe run get-papers-list "cancer therapy" -f results.csv -d
   ```

   - Check `results.csv` in the directory for the output.

6. **View Help**:
   See all available options:

   ```bash
   poetry.exe run get-papers-list -h
   ```

   - Output:

     ```
     usage: get-papers-list [-h] [-f FILE] [-d] query

     Fetch PubMed papers with non-academic authors.

     positional arguments:
       query            PubMed search query

     options:
       -h, --help       show this help message and exit
       -f FILE, --file FILE
                        Output CSV filename
       -d, --debug      Print debug info
     ```

### Command-Line Options

- **`query`**: The PubMed search query (e.g., `"cancer therapy"`, `"vaccine pfizer"`).
- **`-f/--file`**: Specify an output CSV file (e.g., `results.csv`).
- **`-d/--debug`**: Print debug information (query and number of papers found).
- **`-h/--help`**: Display usage instructions.

## Tools Used

- **[BioPython](https://biopython.org/)**: For interacting with the PubMed API via the `Entrez` module.
- **[Pandas](https://pandas.pydata.org/)**: For creating and saving CSV files.
- **[Requests](https://requests.readthedocs.io/)**: Included as a dependency (though not directly used in this version).
- **[Poetry](https://python-poetry.org/)**: For dependency management and packaging.

## Notes

- The program identifies pharma/biotech affiliations using a keyword list (e.g., "Pfizer", "Novartis", "Pharma"). Modify `pharma_keywords` in `fetcher.py` to refine this.
- Corresponding author emails are set to "N/A" as they’re not reliably available via PubMed’s API.

### How to Add This to Your Project

1. **Create the `README.md` File**:
   In your project directory (`~/Python/Assignment`):

   ```bash
   touch README.md
   ```

2. **Copy the Content**:

   - Open `README.md` in a text editor (e.g., `nano README.md` or use VS Code/Notepad).
   - Paste the entire content from above.
   - Save and exit.

3. **Verify**:
   Check the file exists:

   ```bash
   ls -l README.md  # On Windows Git Bash, use `dir` if `ls` fails
   ```

4. **Update Git**:
   If you’ve initialized Git:
   ```bash
   git add README.md
   git commit -m "Add README.md with project details"
   ```

---

### Testing on Another System

The "Step-by-Step Instructions to Test on Your System" section in the `README.md` is designed for someone else to follow. Here’s a quick summary of what they’d do:

1. Clone your GitHub repo (once hosted).
2. Install Python 3.10+ and Poetry.
3. Run `poetry install` in the project directory.
4. Update the email in `fetcher.py`.
5. Test with commands like `poetry.exe run get-papers-list "cancer therapy" -f output.csv -d`.

---
