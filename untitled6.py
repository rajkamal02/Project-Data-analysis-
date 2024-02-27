# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Qc5JIjpjYQ3YK8bool_XzNESPQIPva72
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import nltk
nltk.download('punkt')
nltk.download('stopwords')







import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrape_article(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Extract and print or process the title and content as needed
            title = soup.title.text.strip()
            content_div = soup.find('div', class_='td-post-content tagdiv-type')

            if content_div:
                content = content_div.get_text(strip=True)
                print(f"Title: {title}")
                print(f"Content: {content}")
            else:
                print(f"Content not found in {url}")
        else:
            print(f"Failed to fetch {url}. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
    except Exception as e:
        print(f"Error scraping {url}: {e}")

# Read URLs from Excel file into a DataFrame
excel_file_path = '/Input(1).xlsx'  # Replace with the actual path to your Excel file
df = pd.read_excel(excel_file_path)

# Loop through each row in the DataFrame and scrape articles
for index, row in df.iterrows():
    url = row['URL']
    scrape_article(url)

import pandas as pd
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

# Download NLTK resources (only need to run once)
nltk.download('punkt')
nltk.download('stopwords')

# Function to scrape article title and text
def scrape_article(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Extract title and content
            title = soup.title.text.strip()
            content_div = soup.find('div', class_='td-post-content tagdiv-type')

            if content_div:
                content = content_div.get_text(strip=True)
                return title, content
            else:
                print(f"Content not found in {url}")
                return None, None
        else:
            print(f"Failed to fetch {url}. Status code: {response.status_code}")
            return None, None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None, None
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None, None

# Read URLs from Excel file into a DataFrame
excel_file_path = '/Input(1).xlsx'  # Replace with the actual path to your Excel file
df = pd.read_excel(excel_file_path)

# Create empty DataFrame for article data
article_data = pd.DataFrame(columns=['Title', 'Content'])

# Loop through each row in the DataFrame, scrape articles, and append to the new DataFrame
for index, row in df.iterrows():
    url = row['URL']
    title, content = scrape_article(url)
    if title and content:
        article_data = article_data.append({'Title': title, 'Content': content}, ignore_index=True)

# Display the DataFrame with article data
print(article_data)

# Tokenize and analyze the content using NLTK
stop_words = set(stopwords.words('english'))

def process_text(text):
    tokens = word_tokenize(text)
    # Remove punctuation and convert to lowercase
    words = [word.lower() for word in tokens if word.isalpha()]
    # Remove stop words
    words = [word for word in words if word not in stop_words]
    return words

# Process text in the 'Content' column
article_data['Processed_Content'] = article_data['Content'].apply(process_text)

# Calculate word frequency distribution
all_words = [word for words in article_data['Processed_Content'] for word in words]
fdist = FreqDist(all_words)

# Plot the word frequency distribution
fdist.plot(30, cumulative=False)
plt.show()

import pandas as pd
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

# Download NLTK resources (only need to run once)
nltk.download('punkt')
nltk.download('stopwords')

# Function to scrape article title and text
def scrape_article(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Extract title and content
            title = soup.title.text.strip()
            content_div = soup.find('div', class_='td-post-content tagdiv-type')

            if content_div:
                content = content_div.get_text(strip=True)
                return title, content
            else:
                print(f"Content not found in {url}")
                return None, None
        else:
            print(f"Failed to fetch {url}. Status code: {response.status_code}")
            return None, None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None, None
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None, None

# Read URLs from Excel file into a DataFrame
excel_file_path = '/Input(1).xlsx'  # Replace with the actual path to your Excel file
df = pd.read_excel(excel_file_path)

# Create empty DataFrame for article data
article_data = pd.DataFrame(columns=['Title', 'Content'])

# Loop through each row in the DataFrame, scrape articles, and append to the new DataFrame
for index, row in df.iterrows():
    url = row['URL']
    title, content = scrape_article(url)
    if title and content:
        article_data = article_data.append({'Title': title, 'Content': content}, ignore_index=True)

# Tokenize and analyze the content using NLTK
stop_words = set(stopwords.words('english'))

def process_text(text):
    tokens = word_tokenize(text)
    # Remove punctuation and convert to lowercase
    words = [word.lower() for word in tokens if word.isalpha()]
    # Remove stop words
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)  # Join the words back into a single string

# Process text in the 'Content' column
article_data['Processed_Content'] = article_data['Content'].apply(process_text)

# Calculate word frequency distribution after removing stop words
all_words = [word for words in article_data['Processed_Content'] for word in words.split()]
fdist = FreqDist(all_words)

# Plot the word frequency distribution after removing stop words
fdist.plot(30, cumulative=False)
plt.show()

# Display the DataFrame with processed content
print(article_data[['Title', 'Processed_Content']])

import pandas as pd
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

# Download NLTK resources (only need to run once)
nltk.download('punkt')
nltk.download('stopwords')

# Function to scrape article title and text
def scrape_article(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Extract title and content
            title = soup.title.text.strip()
            content_div = soup.find('div', class_='td-post-content tagdiv-type')

            if content_div:
                content = content_div.get_text(strip=True)
                return title, content
            else:
                print(f"Content not found in {url}")
                return None, None
        else:
            print(f"Failed to fetch {url}. Status code: {response.status_code}")
            return None, None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None, None
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None, None

# Read URLs from Excel file into a DataFrame
excel_file_path = ''  # Replace with the actual path to your Excel file
df = pd.read_excel(excel_file_path)

# Create empty DataFrame for article data
article_data = pd.DataFrame(columns=['Title', 'Content'])

# Tokenize and analyze the content using NLTK
stop_words = set(stopwords.words('english'))

# Define positive and negative words
positive_words = {'good', 'happy', 'excellent', 'positive', 'joy'}
negative_words = {'bad', 'sad', 'terrible', 'negative', 'unhappy'}

# Create columns for positive and negative word counts
article_data['Positive_Count'] = 0
article_data['Negative_Count'] = 0

# Loop through each row in the DataFrame, scrape articles, and append to the new DataFrame
for index, row in df.iterrows():
    url = row['URL']
    title, content = scrape_article(url)
    if title and content:
        # Tokenize and process the content
        tokens = word_tokenize(content)
        words = [word.lower() for word in tokens if word.isalpha()]
        words = [word for word in words if word not in stop_words]
        processed_content = ' '.join(words)

        # Count positive and negative words
        positive_count = sum(1 for word in words if word in positive_words)
        negative_count = sum(1 for word in words if word in negative_words)

        # Append to the DataFrame
        article_data = article_data.append({
            'Title': title,
            'Content': content,
            'Processed_Content': processed_content,
            'Positive_Count': positive_count,
            'Negative_Count': negative_count
        }, ignore_index=True)

# Display the DataFrame with sentiment analysis results
print(article_data[['Title', 'Positive_Count', 'Negative_Count']])

# Plot the positive and negative word counts
article_data[['Positive_Count', 'Negative_Count']].plot(kind='bar', stacked=True)
plt.show()

#sucsess code in alag alag line se

import pandas as pd
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import numpy as np

# Download NLTK resources (only need to run once)
nltk.download('punkt')
nltk.download('stopwords')

# Function to scrape article title and text
def scrape_article(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Extract title and content
            title = soup.title.text.strip()
            content_div = soup.find('div', class_='td-post-content tagdiv-type')

            if content_div:
                content = content_div.get_text(strip=True)
                return title, content
            else:
                print(f"Content not found in {url}")
                return None, None
        else:
            print(f"Failed to fetch {url}. Status code: {response.status_code}")
            return None, None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None, None
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None, None

# Read URLs from Excel file into a DataFrame
excel_file_path = '/Input(1).xlsx'  # Replace with the actual path to your Excel file
df = pd.read_excel(excel_file_path)

# Define positive and negative words
positive_words = {'good', 'happy', 'excellent', 'positive', 'joy'}
negative_words = {'bad', 'sad', 'terrible', 'negative', 'unhappy'}

# Create empty DataFrame for article data
article_data = pd.DataFrame(columns=['Title', 'Content', 'Processed_Content', 'Positive_Count', 'Negative_Count'])

# Tokenize and analyze the content using NLTK
stop_words = set(stopwords.words('english'))

# Loop through each row in the DataFrame, scrape articles, and append to the new DataFrame
for index, row in df.iterrows():
    url = row['URL']
    title, content = scrape_article(url)
    if title and content:
        # Tokenize and process the content
        tokens = word_tokenize(content)
        words = [word.lower() for word in tokens if word.isalpha()]
        words = [word for word in words if word not in stop_words]
        processed_content = ' '.join(words)

        # Count positive and negative words
        positive_count = sum(1 for word in words if word in positive_words)
        negative_count = sum(1 for word in words if word in negative_words)

        # Append to the DataFrame
        article_data = article_data.append({
            'Title': title,
            'Content': content,
            'Processed_Content': processed_content,
            'Positive_Count': positive_count,
            'Negative_Count': negative_count
        }, ignore_index=True)

# 1 Sentimental Analysis
#Sentimental analysis is the process of determining whether a piece of writing is positive,
# negative, or neutral. The below Algorithm is designed for use in Financial Texts. It consists of steps:

# Display the DataFrame with sentiment analysis results
print(article_data[['Title', 'Positive_Count', 'Negative_Count']])
# Plot the positive and negative word counts
article_data[['Positive_Count', 'Negative_Count']].plot(kind='bar', stacked=True )
plt.show()

#1.3 Extracting Derived variables
#We convert the text into a list of tokens using the nltk tokenize module and use these tokens to calculate the 4 variables described below:
#Positive Score: This score is calculated by assigning the value of +1 for each word if found in the Positive Dictionary and then adding up all the values.
#Negative Score: This score is calculated by assigning the value of -1 for each word if found in the Negative Dictionary and then adding up all the values. We multiply the score with -1 so that the score is a positive number.
#Polarity Score: This is the score that determines if a given text is positive or negative in nature. It is calculated by using the formula:


nltk.download('punkt')
nltk.download('stopwords')

# Define positive and negative words
positive_words = {'good', 'happy', 'excellent', 'positive', 'joy'}
negative_words = {'bad', 'sad', 'terrible', 'negative', 'unhappy'}

# Define a function to calculate derived variables
def calculate_derived_variables(text):
    # Tokenize the text into words, remove stop words and punctuation
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    cleaned_words = [word.lower() for word in words if word.lower() not in stop_words and word.lower() not in string.punctuation]

    # Calculate Positive Score
    positive_score = sum(1 for word in cleaned_words if word in positive_words)

    # Calculate Negative Score
    negative_score = sum(1 for word in cleaned_words if word in negative_words)

    # Calculate Polarity Score
    polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)

    # Calculate Subjectivity Score
    subjectivity_score = (positive_score + negative_score) / (len(cleaned_words) + 0.000001)

    return positive_score, negative_score, polarity_score, subjectivity_score

# Calculate derived variables for each article
article_data[['Positive_Score', 'Negative_Score', 'Polarity_Score', 'Subjectivity_Score']] = article_data['Processed_Content'].apply(calculate_derived_variables).apply(pd.Series)

# Display the DataFrame with derived variables
print(article_data[['Title', 'Positive_Score', 'Negative_Score', 'Polarity_Score', 'Subjectivity_Score']])

# 2 Analysis of Readability
# Analysis of Readability is calculated using the Gunning Fox index formula described below.
# Average Sentence Length = the number of words / the number of sentences
# Percentage of Complex words = the number of complex words / the number of words
#Fog Index = 0.4 * (Average Sentence Length + Percentage of Complex words)

nltk.download('punkt')
nltk.download('stopwords')

# Define a function to calculate the Gunning Fog Index
def gunning_fog_index(text):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Tokenize each sentence into words, remove stop words and punctuation
    stop_words = set(stopwords.words('english'))
    total_words = 0
    total_sentences = len(sentences)
    total_complex_words = 0

    for sentence in sentences:
        words = word_tokenize(sentence)
        cleaned_words = [word.lower() for word in words if word.lower() not in stop_words and word.lower() not in string.punctuation]
        total_words += len(cleaned_words)
        total_complex_words += sum(count_syllables(word) > 2 for word in cleaned_words)

    # Calculate average sentence length
    average_sentence_length = total_words / total_sentences if total_sentences > 0 else 0

    # Calculate percentage of complex words
    percentage_complex_words = (total_complex_words / total_words) * 100 if total_words > 0 else 0

    # Calculate Gunning Fog Index
    fog_index = 0.4 * (average_sentence_length + percentage_complex_words)

    return fog_index

# Calculate the Gunning Fog Index for each article
article_data['Gunning_Fog_Index'] = article_data['Processed_Content'].apply(gunning_fog_index)

# Display the DataFrame with the Gunning Fog Index
print(article_data[['Title', 'Gunning_Fog_Index']])

# 3 Average Number of Words Per Sentence
#The formula for calculating is:
#Average Number of Words Per Sentence = the total number of words / the total number of sentences

import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

# Assuming you have the article_data DataFrame
# If not, load your data here

# Download NLTK resources (only need to run once)
nltk.download('punkt')

# Calculate average number of words per sentence for each article
article_data['Sentences'] = article_data['Processed_Content'].apply(sent_tokenize)
article_data['Word_Count_Per_Sentence'] = article_data['Sentences'].apply(lambda x: sum(len(word_tokenize(sentence)) for sentence in x) / len(x) if len(x) > 0 else 0)

# Display the DataFrame with the average number of words per sentence
print(article_data[['Title', 'Word_Count_Per_Sentence']])

# 4 Complex Word Count
#Complex words are words in the text that contain more than two syllables.


nltk.download('punkt')
nltk.download('stopwords')

# Define a function to count complex words in a text
def count_complex_words(text):
    # Tokenize the text into words
    words = word_tokenize(text)

    # Remove stop words and punctuation
    stop_words = set(stopwords.words('english'))
    cleaned_words = [word.lower() for word in words if word.lower() not in stop_words and word.lower() not in string.punctuation]

    # Use the syllable counting function to count syllables for each word
    syllable_counts = [count_syllables(word) for word in cleaned_words]

    # Count the number of words with more than two syllables
    complex_word_count = sum(count > 2 for count in syllable_counts)

    return complex_word_count

# Calculate complex word count for each article
article_data['Complex_Word_Count'] = article_data['Processed_Content'].apply(count_complex_words)

# Display the DataFrame with the complex word count
print(article_data[['Title', 'Complex_Word_Count']])

# 5 Word Count
#We count the total cleaned words present in the text by
#1.removing the stop words (using stopwords class of nltk package).
#2.removing any punctuations like ? ! , . from the word before counting.

# Download NLTK resources (only need to run once)
nltk.download('punkt')
nltk.download('stopwords')

# Define a function to count cleaned words in a text
def count_cleaned_words(text):
    # Tokenize the text into words
    words = word_tokenize(text)

    # Remove stop words and punctuation
    stop_words = set(stopwords.words('english'))
    cleaned_words = [word.lower() for word in words if word.lower() not in stop_words and word.lower() not in string.punctuation]

    # Count the number of cleaned words
    cleaned_word_count = len(cleaned_words)

    return cleaned_word_count

# Calculate cleaned word count for each article
article_data['Cleaned_Word_Count'] = article_data['Processed_Content'].apply(count_cleaned_words)

# Display the DataFrame with the cleaned word count
print(article_data[['Title', 'Cleaned_Word_Count']])

#6 Syllable Count Per Word
#We count the number of Syllables in each word of the text by counting the vowels present
#in each word. We also handle some exceptions like words ending
#with "es","ed" by not counting them as a syllable.

import pandas as pd
import nltk

# Assuming you have the article_data DataFrame
# If not, load your data here

# Download NLTK resources (only need to run once)
nltk.download('punkt')

# Define a function to count syllables in a word
def count_syllables(word):
    vowels = "aeiouy"
    count = 0
    prev_char = ''

    for char in word.lower():
        if char in vowels and prev_char not in vowels:
            count += 1

        # Handle exceptions like words ending with "es" or "ed"
        if char in ['e'] and prev_char == 'e' and word.lower()[-2:] not in ['le', 're']:
            count -= 1

        prev_char = char

    # Avoid counting 0 syllables for short words
    return max(1, count)

# Define a function to count syllables in a sentence
def count_syllables_in_sentence(sentence):
    # Tokenize the sentence into words
    words = nltk.word_tokenize(sentence)

    # Count syllables for each word and sum them up
    total_syllables = sum(count_syllables(word) for word in words)

    return total_syllables

# Calculate syllable count for each article
article_data['Syllable_Count'] = article_data['Processed_Content'].apply(count_syllables_in_sentence)

# Display the DataFrame with the syllable count
print(article_data[['Title', 'Syllable_Count']])

#7Personal Pronouns
#To calculate Personal Pronouns mentioned in the text, we use regex to find the
#counts of the words - “I,” “we,” “my,” “ours,” and “us”. Special care is taken so that the country
#name US is not included in the list.


import pandas as pd
import re

# Assuming you have the article_data DataFrame
# If not, load your data here

# Define a function to count personal pronouns using regex
def count_personal_pronouns(text):
    # Define a regex pattern to match personal pronouns
    pronoun_pattern = re.compile(r'\b(I|we|my|ours|us)\b', flags=re.IGNORECASE)

    # Find all matches in the text
    matches = pronoun_pattern.findall(text)

    # Count the number of matches
    personal_pronouns_count = len(matches)

    return personal_pronouns_count

# Calculate personal pronoun count for each article
article_data['Personal_Pronouns_Count'] = article_data['Processed_Content'].apply(count_personal_pronouns)

# Display the DataFrame with the personal pronoun count
print(article_data[['Title', 'Personal_Pronouns_Count']])

import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

# Define stop words
stop_words = set(stopwords.words('english'))

# Function to calculate average word length
def average_word_length(text):
    # Tokenize the text
    words = word_tokenize(text)

    # Remove stop words
    words = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]

    # Calculate total number of characters and total number of words
    total_characters = sum(len(word) for word in words)
    total_words = len(words)

    # Calculate average word length
    if total_words > 0:
        average_length = total_characters / total_words
        return average_length
    else:
        return 0

# Apply the function to calculate average word length for each article
article_data['Average_Word_Length'] = article_data['Processed_Content'].apply(average_word_length)

# Display the DataFrame with average word length
print(article_data[['Title', 'Average_Word_Length']])

