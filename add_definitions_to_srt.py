import re

def load_srt_file(file_path):
    with open(file_path, 'r', encoding='latin-1') as file:
        lines = file.readlines()
    return lines

def save_srt_file(file_path, lines):
    with open(file_path, 'w', encoding='latin-1') as file:
        file.writelines(lines)

def load_word_definitions_from_file(definitions_file_path):
    word_definitions = {}

    # Open the file and read word definitions
    with open(definitions_file_path, 'r', encoding='latin-1') as file:
        for line in file:
            line = line.strip()
            if line:
                word, definition = line.split(':', 1)
                word_definitions[word.strip()] = definition.strip()

    return word_definitions

def add_definitions_to_srt(srt_lines, word_definitions):
    for word, definition in word_definitions.items():
        for i, line in enumerate(srt_lines):
            if word in line:
                for j in range(1, len(srt_lines) - i):
                    if srt_lines[i + j].strip() == '':
                        srt_lines[i + j] = f"{word}: {definition}\n\n"
                        break
                break
    return srt_lines

def main():
    srt_file_path = input('Enter path to your subtitles.srt: ')
    definitions_file_path = input('path to your definitions.txt: ')

    try:
        # Load the SRT file
        srt_lines = load_srt_file(srt_file_path)

        # Load word definitions from file
        word_definitions = load_word_definitions_from_file(definitions_file_path)
        #print(word_definitions)
        
        # Add definitions to the SRT file
        srt_lines = add_definitions_to_srt(srt_lines, word_definitions)

        # Save the modified SRT file
        save_srt_file(srt_file_path, srt_lines)

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' could not be found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
