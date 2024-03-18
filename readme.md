# SANS Book Index Generator

## Description

This Python script generates an index for a SANS book by leveraging the OpenAI GPT-4 model to identify key terms and their definitions from each page of the book. The generated index is then written to a CSV file for convenience.

The project consists of two main components:

- `index.py`: Parses through each page of a given PDF(s) and utilizes GPT-4 to identify key terms and their definitions on that page, generating an index file for the book.
- `combiner.py`: Merges the .csv files from multiple books into a single composite index file.

## Setup Instructions

### Prerequisites

- Clone the repository to your local machine.
- Install the necessary Python dependencies by executing `pip install -r requirements.txt` in your terminal.
- Create a `.env` file in the root directory of the project following the template provided below.
- Download the course PDFs from [SANS Download Materials](https://www.sans.org/account/download-materials).
- Place the book PDFs inside the `Books` directory.
- Update `Index.py` to reflect your book naming convention.

### `.env` File Configuration

Your `.env` file should include:

```plaintext
OPENAI_API_KEY=<your-openai-api-key>
PDF_PASSWORD=<your-pdf-password>
```

Replace `<your-openai-api-key>` and `<your-pdf-password>` with your actual OpenAI API key and PDF password, respectively. Ensure there are no spaces or quotes around the values in the `.env` file.

### Obtaining an OpenAI API Key

1. Visit the [OpenAI website](https://openai.com/).
2. Sign up for an account or log in if you already have one.
3. Navigate to the API section in your account dashboard.
4. Generate a new API Key and ensure your account is funded.
5. **Important:** Treat your API keys as sensitive data. Do not expose them publicly or share them with untrusted parties.

### Adjustments

You may need to adjust the naming of the books/courses in the code as indicated by comments. The default setup uses names like "FOR500_B1" for book 1, "FOR500_B2" for book 2, etc. Adjust these names to match your specific class/books.

## Usage

1. Execute the `index.py` script to index each PDF in the `Books` directory. The files may not be processed in order, but this is expected behavior.
2. After all books have been indexed, run the `combiner.py` script to generate a composite index file for all the books.

## Final Notes

The provided scripts assume specific formats and content structures for the PDFs and may not work perfectly with all SANS books or different types of documents. While the output should not be blindly trusted, it can serve as a valuable starting point or a last resort if necessary.
