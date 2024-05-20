import os
import glob
import pdfplumber
from dotenv import load_dotenv
import openai
import pandas as pd
from collections import defaultdict
import time

# Load .env file and extract variables
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
PDF_PASSWORD = os.getenv('PDF_PASSWORD')

# Initialize OpenAI client
client = openai.OpenAI(api_key=OPENAI_API_KEY)

def parse_line(line):
    # Attempt to extract term and definition using a flexible approach
    if ':' in line:
        term, definition = line.split(':', 1)
    elif ' - ' in line:
        term, definition = line.split(' - ', 1)
    else:
        parts = line.split(',', 1)
        if len(parts) == 2:
            term, definition = parts
        else:
            return None, None  # Unable to parse line
    return term.strip(), definition.strip()

def process_pdf(pdf_path):
    index = defaultdict(lambda: {'pages': set(), 'definition': ''})
    with pdfplumber.open(pdf_path, password=PDF_PASSWORD) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            page_number = i - 1
            print(f'Prompting for page {page_number} in {os.path.basename(pdf_path)}...\n')
            
            
            prompt = f"Your task is to analyze a single page from a SANS textbook, focusing specifically on Cloud, Cybersecurity, and Threat Detection. Identify the most crucial term or concept on this page. If the page lacks substantive material or is a title page, respond with 'none'. The selected term must be directly related to the core topics mentioned, concise, and hold significant relevance to the content on the page. Aim for a term or a succinct phrase of no more than 3-4 words. Alongside the term, provide a comprehensive definition, prioritizing completeness over brevity. This definition should be concise, ideally between 10-25 words, and separated from the term by a comma. Ensure the term is explored in detail on the page rather than mentioned briefly. Exclude complex phrases, author names, page numbers, course titles, or overly broad concepts. For terms related to broader topics or tools with many subcategories, format them to group similar topics together. For MITRE ATT&CK techniques, list only the T-code and the technique's name. This task aims to create an index of the book, so please focus on identifying key terms that are concrete, relevant, and crucial to the page's content. Here is the next page: \n\n{text}"

            try:
                response = client.chat.completions.create(model="gpt-4o",
                messages=[{"role": "system", "content": "You are a knowledgeable assistant helping to index a book."}, {"role": "user", "content": prompt}],
                max_tokens=1024,
                temperature=0.5)

                response_text = response.choices[0].message.content
                lines = response_text.strip().split('\n')
                for line in lines:
                    term, definition = parse_line(line)
                    if term and definition and term.lower() != 'none':
                        index[term]['pages'].add(page_number)
                        if not index[term]['definition']:
                            index[term]['definition'] = definition
                    elif term or definition:  # Log partial or unclear matches
                        print(f"Partial or unclear match: '{line}'")
            except openai.RateLimitError:
                print("Rate limit exceeded. Waiting before retrying...")
                time.sleep(60)  # Sleep for 60 seconds before retrying

    return index

# Define the directory and pattern for the PDF files
pdf_files = glob.glob('./Books/FOR500_[BW]*.pdf')

# Process each PDF file found by glob
for pdf_path in pdf_files:
    print(f'Processing {pdf_path}...')
    index = process_pdf(pdf_path)

    # Prepare the DataFrame and CSV output for each PDF
    df = pd.DataFrame(
        [(term, ', '.join(map(str, sorted(data['pages']))), data['definition']) for term, data in index.items()],
        columns=['Term', 'Pages', 'Definition']
    )

    outfile = pdf_path.replace('.pdf', '.csv').split('/')[-1]
    print(f"Converting to CSV for {pdf_path}...\n")
    df.to_csv(outfile, index=False)
