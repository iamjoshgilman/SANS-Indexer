import pandas as pd
import glob
import re

# Use glob to find all CSV files that match the pattern
file_pattern = '*.csv'
files = glob.glob(file_pattern)

# List to store each entry
data = []

# Regular expression pattern to match the book number
pattern = r"_(B|W)(\d+)\.csv$"

# Iterating through all files matched
for file in files:
    # Loading CSV file
    df = pd.read_csv(file)
    
    # Use regular expression to extract book number
    match = re.search(pattern, file)
    if match:
        book_number = match.group(1) + match.group(2)  # Concatenate the letter and the number

        # Iterating through each row
        for index, row in df.iterrows():
            term = row['Term']
            pages = row['Pages']
            definition = str(row['Definition'])  # Convert definition to string

            # Append each term with its book number, page number, and definition
            data.append({"Term": term, "Book": f"{book_number}", "Page": pages, "Definition": definition})
    else:
        print(f"No book number found in {file}")

# Transforming list to dataframe
final_df = pd.DataFrame(data)

# Saving to composite CSV
final_df.to_csv('GCFE_Composite.csv', index=False)
