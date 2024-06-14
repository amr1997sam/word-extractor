from collections import Counter
import string
import csv
import re
import os

# Get the current working directory
current_directory = os.getcwd()

# Set relative paths from the current working directory
csv_file_relative_path = 'English_vocabulary_ordered_by_frequency.csv'
output_file_relative_path = 'output.txt'

# Combine the relative paths with the current directory to get the absolute paths
csv_file_path = os.path.join(current_directory, csv_file_relative_path)
output_file_path = os.path.join(current_directory, output_file_relative_path)


def process_csv_file(csv_file_path):
    # Create an empty list to store the values from the first column
    first_column_values = []

    # Open the CSV file and read the first column into the list
    with open(csv_file_path, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
    
        # Assuming the first column is at index 0
        for row in csv_reader:
            if row:  # Check if the row is not empty
                first_column_values.append(row[0])

    return first_column_values

def remove_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def process_text_file(file_path):
    with open(file_path, 'r', encoding='latin-1') as file:
        text = file.read()

    # Remove HTML-like tags
    cleaned_text = remove_tags(text)
    
    # Remove punctuation and convert to lowercase
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = cleaned_text.translate(translator).lower()

    # Split text into words
    ls_of_vocab_B = cleaned_text.split()

    return ls_of_vocab_B

def main():
    print("\n\n")
    print(">>> This program takes your file and gives you ordered list of the vocabulary based in its commonality in the English language\n")
    file_path = input("Enter the path to the text file you want to be processed: ")

    try:
        ordered_ls_of_vocab_based_on_freq_A = process_csv_file(csv_file_path) 
        dictionary_of_A = {val: ix for ix, val in enumerate(ordered_ls_of_vocab_based_on_freq_A)}
        ls_of_vocab_B = process_text_file(file_path)

        # Filter out words not present in ordered_ls_of_vocab_based_on_freq_A
        ls_of_vocab_B = [word for word in ls_of_vocab_B if word in dictionary_of_A]
        
        ls_of_vocab_op = sorted(ls_of_vocab_B, key=lambda word: dictionary_of_A.get(word, float('inf')), reverse=True)
        
        # Use a set to track printed words and avoid repetitions
        printed_words = set()

        # Write ordered words to the output text file
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            for word in ls_of_vocab_op:
                if word not in printed_words:
                    output_file.write(word + '\n')
                    printed_words.add(word)
                    
        print(f"Ordered words have been written to '{output_file_path}'.")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' could not be found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
