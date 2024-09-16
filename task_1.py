import pandas as pd

# Manually list the CSV file names
csv_files = ["CSV1.csv", "CSV2.csv", "CSV3.csv", "CSV4.csv"]

# List of possible columns to extract text from
columns_to_extract = ['Short_TEXT', 'TEXT', 'entites']  # Adjust based on actual column names

# Open a new text file to store the combined text
with open("combined_text.txt", "w", encoding='utf-8') as output_file:
    # Loop through each CSV file
    for file in csv_files:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file)

        # Clean the column names: Strip leading/trailing spaces and convert to lowercase
        df.columns = df.columns.str.strip().str.lower()
        
        # Print the cleaned columns to verify
        print(f"Cleaned columns in {file}: {df.columns}")

        # Check if any of the desired columns are present in the file (case-insensitive)
        for column in columns_to_extract:
            column = column.lower()  # Ensure the column name is lowercase
            if column in df.columns:
                # Extract the text from the column and write it to the text file
                for text in df[column]:
                    if pd.notna(text):  # Ensure text is not empty or NaN
                        output_file.write(str(text) + '\n')  # Write each text line into the .txt file
            else:
                print(f"Column '{column}' not found in {file}")
