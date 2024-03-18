# Description

This is a python script used to generate an index for a SANS book. It uses the OpenAI GPT-4 model to identify key terms and their definitions from each page of the book. The index is then written to a CSV file.

It consists of two main scripts:

1. index.py - This script goes through each page of a given PDF and uses GPT-4 to identify a key term and its definition on that page, creating an index file for that book.

2. combiner.py - This script combines the index files of multiple books into a composite index file.

# Setup Instructions

1. Clone the repository.
2. Install the necessary dependencies by running pip install -r requirements.txt in your terminal.
3. Create a .env file in the root directory of the project.
4. Download course pdfs from https://www.sans.org/account/download-materials
5. Remove pdf password through qpdf: qpdf --password=enterpasswordhere -decrypt "InputFilename.pdf" "OutputFilename.pdf"

# .env file

The file should contain the following:

```
OPENAI_API_KEY=<your-openai-api-key>
PDF_PASSWORD=<your-pdf-password>
```

Replace <your-openai-api-key> and <your-pdf-password> with your actual OpenAI API key and PDF password. Make sure to not have any spaces or single or double quotes surrouding your key and password in the .env file. 

# OpenAI API Key

To obtain an OpenAI API Key, follow these steps:

- Visit the OpenAI website.
- Sign up for an account if you don't already have one.
- Go to the API section in the account dashboard.
- Generate a new API Key.

Remember to treat your API keys as sensitive data, do not expose them publicly or to anyone you do not trust.

# Adjustments

You will need to adjust the name of the book/course at a few points in the code indicated by comments. The current scripts are set up to use book names of "SEC5881" for book 1, "SEC5882" for book 2, etc. You can change this to however you need. 

If you are creating indexes for more books or less books, adjust the range in the second for loop in combiner.py to match the number of books you are indexing.
Running the Scripts

1. Run the index.py script for each book you want to index.
2. Once all books have been indexed, run the combiner.py script to create a composite index of all the books.

# Error Handling

If you receive an error stating that gpt-4 is not available, you will need to replace "gpt-4" in the openai.ChatCompletion.create() call with the identifier of the most recent model available in the OpenAI models list.

Visit the OpenAI Models page to see the currently available models.

Please note that using a different model may result in differing results from the ones mentioned above.

# Final Notes

The scripts provided assume a specific format and content for the PDF and might not work as expected for all SANS books or other types of documents. You may need to tweak the scripts based on the specifics of your PDFs.

Once the index is fully generated you can open it in excel and format appropriately to your preference. Here is an example of the final product:

![Example Image](example.png)
