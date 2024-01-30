# import webbrowser

# url_lists = [
#     'http://www.python.org',
#     'https://github.com/Preetiraj3697',
#     'https://www.linkedin.com/in/preetiraj3697/',
#     'https://www.google.com'
    
# ]

# # Opens the above list of websites in a different tab
# for url in url_lists:
#     webbrowser.open_new_tab(url)

# import requests

# url = 'https://api.ynos.in/collections/top-startups?page=0&N=10'
# response = requests.get(url) # opening a network and fetching a data
# print(response)
# print(response.status_code) # status code, success:200
# print(response.headers)     # headers information
# # print(response.text) # gives all the text from the page
# url = 'https://restcountries.com/v3.1/all'
# res = requests.get(url)
# print(res)
# print(res.status_code)
# countries = res.json()
# # print(countries[:1])

# Exercises: Day 20
# Read this url and find the 10 most frequent words. romeo_and_juliet = 'https://www.gutenberg.org/cache/epub/1777/pg1777-images.html'

import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

# Function to get the text content from a URL
def get_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.get_text()

# Function to get the 10 most frequent words from a given text
def get_most_frequent_words(text):
    # Use regular expression to extract words from the text
    words = re.findall(r'\b\w+\b', text.lower())

    # Count the frequency of each word
    word_counts = Counter(words)

    # Get the 10 most common words
    most_common_words = word_counts.most_common(10)

    return most_common_words

# URL of the text file
romeo_and_juliet_url = 'https://www.gutenberg.org/cache/epub/1777/pg1777-images.html'

# Get the text content from the URL
text_content = get_text_from_url(romeo_and_juliet_url)

# Get the 10 most frequent words
most_frequent_words = get_most_frequent_words(text_content)

# Print the result
print("The 10 most frequent words are:")
for word, count in most_frequent_words:
    print(f"{word}: {count}")


# 2. Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
# the min, max, mean, median, standard deviation of cats' weight in metric units.
# the min, max, mean, median, standard deviation of cats' lifespan in years.
# Create a frequency table of country and breed of cats


import requests
import numpy as np
from statistics import mean, median, stdev
from collections import Counter

# Function to fetch data from the Cat API
def get_cats_data(api_url):
    response = requests.get(api_url)
    return response.json()

# Function to calculate statistics for a list of numerical values
def calculate_statistics(data):
    return {
        'min': np.min(data),
        'max': np.max(data),
        'mean': mean(data),
        'median': median(data),
        'std_dev': stdev(data)
    }

# Function to create a frequency table for country and breed
def create_frequency_table(data, key1, key2):
    frequency_table = Counter((item[key1], item[key2]) for item in data)
    return frequency_table

# Cat API URL
cats_api = 'https://api.thecatapi.com/v1/breeds'

# Get data from the Cat API
cats_data = get_cats_data(cats_api)

# Extract weights and lifespans from the data
weights = [cat.get('weight', {}).get('metric', '').split()[0] for cat in cats_data]
lifespans = [cat.get('life_span', '').split()[0] for cat in cats_data]

# Convert weights and lifespans to numerical values
weights = [float(weight) if weight else 0 for weight in weights]
lifespans = [float(lifespan) if lifespan else 0 for lifespan in lifespans]

# Calculate statistics for weights and lifespans
weight_statistics = calculate_statistics(weights)
lifespan_statistics = calculate_statistics(lifespans)

# Create a frequency table for country and breed
frequency_table = create_frequency_table(cats_data, 'origin', 'name')

# Print the results
print("Statistics for Cat Weights (in metric units):")
print(weight_statistics)

print("\nStatistics for Cat Lifespans (in years):")
print(lifespan_statistics)

print("\nFrequency Table for Country and Breed:")
for (country, breed), count in frequency_table.items():
    print(f"{country}, {breed}: {count}")

# 3. Read the countries API and find
# the 10 largest countries
# the 10 most spoken languages
# the total number of languages in the countries API
import requests

# Function to fetch data from the Countries API
def get_countries_data(api_url):
    response = requests.get(api_url)
    return response.json()

# Function to get the 10 largest countries
def get_largest_countries(countries_data):
    largest_countries = sorted(countries_data, key=lambda x: x['area'], reverse=True)[:10]
    return largest_countries

# Function to get the 10 most spoken languages
def get_most_spoken_languages(countries_data):
    all_languages = [language for country in countries_data for language in country['languages']]
    most_spoken_languages = [language for language, count in Counter(all_languages).most_common(10)]
    return most_spoken_languages

# Function to get the total number of languages
def get_total_languages(countries_data):
    all_languages = [language for country in countries_data for language in country['languages']]
    total_languages = len(set(all_languages))
    return total_languages

# Countries API URL
countries_api = 'https://restcountries.com/v3.1/all'

# Get data from the Countries API
countries_data = get_countries_data(countries_api)
# print(countries_data)
# Get the 10 largest countries
largest_countries = get_largest_countries(countries_data)
print("\n10 Largest Countries:")
for country in largest_countries:
    print(country['name']['common'])

# Get the 10 most spoken languages
most_spoken_languages = get_most_spoken_languages(countries_data)
print("\n10 Most Spoken Languages:")
print(most_spoken_languages)

# Get the total number of languages
total_languages = get_total_languages(countries_data)
print("\nTotal Number of Languages in the Countries API:", total_languages)

