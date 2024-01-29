# Opening files for reading
f = open('./files/reading_file_example.txt')
print(f)
txt = f.read()
print(type(txt))
print(txt)
f.close()
# printing all the text, let us print the first 10 characters of the text file.
f = open('./files/reading_file_example.txt')
txt = f.read(10)
print(type(txt))
print(txt)
f.close()
# readline(): read only the first line
f = open('./files/reading_file_example.txt')
line = f.readline()
print(type(line))
print(line)
f.close()
# readlines(): read all the text line by line and returns a list of lines
f = open('./files/reading_file_example.txt')
lines = f.readlines()
print(type(lines))
print(lines)
f.close()
# Another way to get all the lines as a list is using splitlines():
f = open('./files/reading_file_example.txt')
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()

with open('./files/reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)


# Opening Files for Writing and Updating

with open('./files/reading_file_example.txt', 'a') as f:
    f.write('This text has to be appended at the end.')

with open('./files/writing_file_example.txt', 'w') as f:
    f.write('This text will be written in a newly created file.')
    
# Deleting Files
# import os

# if os.path.exists('./files/example.txt'):
#     os.remove('./files/example.txt')
# else:
#     print('The file does not exist')

# File types
# file with txt extension
# file with json extension
# dictionary
# person_dct = {
#     'name':'Paarthav',
#     'country':'India',
#     'city':'Faridabad',
#     'skills':['javascript','React','Python']
# }

# # JSON: A string from a dictionary
# person_json = "{'name':'Paarthav','country':'India','city':'Faridabad','skills':['javascript','React','Python']}"

# # we use three quotes and make it multiple line to make it more readable
# person_json = '''
# {
#     'name':'Paarthav',
#     'country':'India',
#     'city':'Faridabad',
#     'skills':['javascript','React','Python']
# }
# '''
# Changing JSON to Dictionary
import json
# JSON
person_json = '''{
    "name": "Paarthav",
    "country": "India",
    "city": "Faridabad",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# let's change JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])

# Changing Dictionary to JSON
# python dictionary
person = {
     "name": "Paarthav",
    "country": "India",
    "city": "Faridabad",
    "skills": ["JavaScrip", "React", "Python"]
}
# let's convert it to json
person_json = json.dumps(person, indent=4)
print(type(person_json))
print(person_json)

# Saving as Json file
with open('./files/json_example.json','w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)

# File with csv Extension
import csv
with open('./files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are: {", ".join(row)}')
            line_count += 1
        else:
            print(
                 f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}'
            )
    
# File with xlsx Extension
# import xlrd
# excel_book = xlrd.open_workbook('sample.xls')
# print(excel_book.nsheets)
# print(excel_book.sheet_names)

# File with xml Extension
import xml.etree.ElementTree as ET
tree = ET.parse('./files/xml_example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)

# Exercises: Level 1

# Write a function which count number of lines and number of words in a text. All the files are in the data the folder: a) Read obama_speech.txt file and count number of lines and words b) Read michelle_obama_speech.txt file and count number of lines and words c) Read donald_speech.txt file and count number of lines and words d) Read melina_trump_speech.txt file and count number of lines and words

def count_lines_and_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
            
            print(f'File: {file_path}')
            print(f'Number of lines: {num_lines}')
            print(f'Number of words: {num_words}\n')
            
    except FileNotFoundError:
        print(f'Error: File {file_path} not found.\n')
    except Exception as e:
        print(f"Error: {e}\n")

# a) obama speech
count_lines_and_words('./data/obama_speech.txt')
# b) Michelle Obama speech
count_lines_and_words('data/michelle_obama_speech.txt')
# c) Donald Trump speech
count_lines_and_words('data/donald_speech.txt')
# d) Melania Trump speech
count_lines_and_words('data/melina_trump_speech.txt')

# 2. Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages

# # Your output should look like this
# print(most_spoken_languages(filename='./data/countries_data.json', 10))
# [(91, 'English'),
# (45, 'French'),
# (25, 'Arabic'),
# (24, 'Spanish'),
# (9, 'Russian'),
# (9, 'Portuguese'),
# (8, 'Dutch'),
# (7, 'German'),
# (5, 'Chinese'),
# (4, 'Swahili'),
# (4, 'Serbian')]

# # Your output should look like this
# print(most_spoken_languages(filename='./data/countries_data.json', 3))
# [(91, 'English'),
# (45, 'French'),
# (25, 'Arabic')]
import json

def most_spoken_languages(filename, top_n):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

        languages_count = {}

        for country in data:
            languages = country.get('languages', [])
            for language in languages:
                languages_count[language] = languages_count.get(language, 0) + 1

        sorted_languages = sorted(languages_count.items(), key=lambda x: x[1], reverse=True)

        return sorted_languages[:top_n]

    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
    except json.JSONDecodeError:
        print(f"Error: Unable to decode JSON in file {filename}.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage for the given outputs
print(most_spoken_languages(filename='./data/countries_data.json', top_n=10))
print(most_spoken_languages(filename='./data/countries_data.json', top_n=3))

# 3. Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries

# # Your output should look like this
# print(most_populated_countries(filename='./data/countries_data.json', 10))

# [
# {'country': 'China', 'population': 1377422166},
# {'country': 'India', 'population': 1295210000},
# {'country': 'United States of America', 'population': 323947000},
# {'country': 'Indonesia', 'population': 258705000},
# {'country': 'Brazil', 'population': 206135893},
# {'country': 'Pakistan', 'population': 194125062},
# {'country': 'Nigeria', 'population': 186988000},
# {'country': 'Bangladesh', 'population': 161006790},
# {'country': 'Russian Federation', 'population': 146599183},
# {'country': 'Japan', 'population': 126960000}
# ]

# # Your output should look like this

# print(most_populated_countries(filename='./data/countries_data.json', 3))
# [
# {'country': 'China', 'population': 1377422166},
# {'country': 'India', 'population': 1295210000},
# {'country': 'United States of America', 'population': 323947000}
# ]
def most_populated_countries(filename,top_n):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        sorted_countries = sorted(data, key=lambda x:x['population'],reverse=True)
        
        result = [
            {'country': country['name'], 'population':country['population']}
            for country in sorted_countries[:top_n]
        ]
        
        return result
    except FileExistsError:
        print(f"Error: File {filename} not found.")
    except json.JSONDecodeError:
        print(f"Error: Unable to decode JSON in file {filename}.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage for the given outputs
print(most_populated_countries(filename='./data/countries_data.json', top_n=10))
print(most_populated_countries(filename='./data/countries_data.json', top_n=3))

# Extract all incoming email addresses as a list from the email_exchange_big.txt file.
import re
def extract_email_addresses(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # use a regular expression to find email addressess
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        email_addresses = re.findall(email_pattern, content)
        
        return email_addresses
    
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
    except Exception as e:
        print(f"Error: {e}")

# # Example usage
# email_addresses = extract_email_addresses('./data/email_exchanges_big.txt')

# # Print the extracted email addresses
# print(email_addresses)

# 5. Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output
#     # Your output should look like this
#     print(find_most_common_words('sample.txt', 10))
#     [(10, 'the'),
#     (8, 'be'),
#     (6, 'to'),
#     (6, 'of'),
#     (5, 'and'),
#     (4, 'a'),
#     (4, 'in'),
#     (3, 'that'),
#     (2, 'have'),
#     (2, 'I')]

#     # Your output should look like this
#     print(find_most_common_words('sample.txt', 5))

#     [(10, 'the'),
#     (8, 'be'),
#     (6, 'to'),
#     (6, 'of'),
#     (5, 'and')]

from collections import Counter

def find_most_common_words(input_data, top_n):
    if isinstance(input_data, str):
        # If input is a string, tokenize it into words
        words = re.findall(r'\b\w+\b', input_data.lower())
    elif hasattr(input_data, 'read'):
        # If input is a file, read its content and tokenize into words
        content = input_data.read().lower()
        words = re.findall(r'\b\w+\b', content)
    else:
        raise ValueError("Input must be a string or a file object")

    # Count the frequency of each word
    word_counts = Counter(words)

    # Get the top N most common words
    most_common_words = word_counts.most_common(top_n)

    return most_common_words

# Example usage with a file
print(find_most_common_words(open('./data/sample.txt', 'r', encoding='utf-8'), 10))

# Example usage with a string
sample_text = "This is a sample text. This text contains some words. Words are repeated to demonstrate the example."
print(find_most_common_words(sample_text, 5))

# 6. Use the function, find_most_frequent_words to find: a) The ten most frequent words used in Obama's speech b) The ten most frequent words used in Michelle's speech c) The ten most frequent words used in Trump's speech d) The ten most frequent words used in Melina's speech
def find_most_frequent_words(input_data, top_n):
     if isinstance(input_data, str):
        # If input is a string, tokenize it into words
        words = re.findall(r'\b\w+\b', input_data.lower())
     elif hasattr(input_data, 'read'):
        # If input is a file, read its content and tokenize into words
        content = input_data.read().lower()
        words = re.findall(r'\b\w+\b', content)
     else:
        raise ValueError("Input must be a string or a file object")

     # Count the frequency of each word
     word_counts = Counter(words)

     # Get the top N most common words
     most_common_words = word_counts.most_common(top_n)

     return most_common_words

# a) Obama's speech
obama_speech_path = './data/obama_speech.txt'
with open(obama_speech_path, 'r', encoding='utf-8') as obama_file:
    obama_most_common_words = find_most_frequent_words(obama_file, 10)
    print(f"Ten most frequent words in Obama's speech: {obama_most_common_words}")
    
# b) Michelle's speech
michelle_speech_path = './data/michelle_obama_speech.txt'
with open(michelle_speech_path, 'r', encoding='utf-8') as michelle_file:
    michelle_most_common_words = find_most_common_words(michelle_file, 10)
    print(f"Ten most frequent words in Michelle's speech: {michelle_most_common_words}")

# c) Trump's speech
trump_speech_path = './data/donald_speech.txt'
with open(trump_speech_path, 'r', encoding='utf-8') as trump_file:
    trump_most_common_words = find_most_common_words(trump_file, 10)
    print(f"Ten most frequent words in Trump's speech: {trump_most_common_words}")

# d) Melania's speech
melania_speech_path = './data/melina_trump_speech.txt'
with open(melania_speech_path, 'r', encoding='utf-8') as melania_file:
    melania_most_common_words = find_most_common_words(melania_file, 10)
    print(f"Ten most frequent words in Melania's speech: {melania_most_common_words}")

#  9. Find the 10 most repeated words in the romeo_and_juliet.txt
def find_most_repeated_words(file_path, top_n):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        words = re.findall(r'\b\w+\b', content.lower())
        word_counts = Counter(words)

        most_repeated_words = word_counts.most_common(top_n)
        return most_repeated_words

    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
    except Exception as e:
        print(f"Error: {e}")
        
romeo_and_juliet_path = './data/romeo_and_juliet.txt'
most_repeated_words = find_most_repeated_words(romeo_and_juliet_path, 10)
print(f"10 most repeated words in 'romeo_and_juliet.txt': {most_repeated_words}")
#  10. Read the hacker news csv file and find out: a) Count the number of lines containing python or Python b) Count the number lines containing JavaScript, javascript or Javascript c) Count the number lines containing Java and not JavaScript
import csv    
def count_lines_with_keyword(csv_file_path, keyword):
    try:
        with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            lines_with_keyword = [line for line in reader if keyword.lower() in map(str.lower, line)]

        return len(lines_with_keyword)

    except FileNotFoundError:
        print(f"Error: File {csv_file_path} not found.")
    except Exception as e:
        print(f"Error: {e}") 
    
# a) Count the number of lines containing python or Python
hacker_news_csv_path = './data/hacker_news.csv'
python_lines_count = count_lines_with_keyword(hacker_news_csv_path, 'python')
print(f"Number of lines containing 'python' or 'Python': {python_lines_count}")

# b) Count the number of lines containing JavaScript, javascript, or Javascript
javascript_lines_count = count_lines_with_keyword(hacker_news_csv_path, 'javascript')
print(f"Number of lines containing 'JavaScript', 'javascript', or 'Javascript': {javascript_lines_count}")

# c) Count the number of lines containing Java and not JavaScript
java_lines_count = count_lines_with_keyword(hacker_news_csv_path, 'java')
javascript_lines_count = count_lines_with_keyword(hacker_news_csv_path, 'javascript')
java_not_javascript_lines_count = java_lines_count - javascript_lines_count
print(f"Number of lines containing 'Java' and not 'JavaScript': {java_not_javascript_lines_count}")
    
    
# 7.  Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of Michelle's and Melina's speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of stop words are in the data directory  
import re
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('stopwords')

def clean_text(text):
    # Remove special characters, digits, and convert to lowercase
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
    return cleaned_text.lower()

def remove_stop_words(text):
    stop_words = set(nltk.corpus.stopwords.words('english'))
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)

def check_text_similarity(text1, text2):
    cleaned_text1 = remove_stop_words(clean_text(text1))
    cleaned_text2 = remove_stop_words(clean_text(text2))

    vectorizer = CountVectorizer().fit_transform([cleaned_text1, cleaned_text2])
    similarity = cosine_similarity(vectorizer)
    
    return similarity[0, 1]

# Example usage
michelle_speech_path = './data/michelle_obama_speech.txt'
melania_speech_path = './data/melina_trump_speech.txt'

with open(michelle_speech_path, 'r', encoding='utf-8') as michelle_file:
    michelle_speech = michelle_file.read()

with open(melania_speech_path, 'r', encoding='utf-8') as melania_file:
    melania_speech = melania_file.read()

similarity_score = check_text_similarity(michelle_speech, melania_speech)
print(f"Similarity between Michelle's and Melania's speech: {similarity_score}")
