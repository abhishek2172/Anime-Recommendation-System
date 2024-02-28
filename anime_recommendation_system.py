# -*- coding: utf-8 -*-
"""anime-recommendation-system.ipynb

# **Anime Recommendation System**

Importing the dependencies
"""

import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

"""Data Collection and Pre-Processing"""

# Loading the data from csv file to pandas dataframe
anime_data = pd.read_csv('anime.csv')

# Printing the first five rows of the data frame
anime_data.head()

# Selecting the relevant features for recommendation
selected_features = ['Genres','Studios','Source']
print(selected_features)

# Replacing the missing values with null string
for feature in selected_features:
  anime_data[feature] = anime_data[feature].fillna('')

# Combining all the 3 selected features

combined_features = anime_data['Genres']+' '+anime_data['Studios']+' '+anime_data['Source']

print(combined_features)

# Converting the text data to feature vectors
vectorizer = TfidfVectorizer()

feature_vectors = vectorizer.fit_transform(combined_features)

print(feature_vectors)

"""Cosine Similarity"""

# Getting the similarity confidence value using cosine similarity
similarity = cosine_similarity(feature_vectors)

print(similarity)

print(similarity.shape)

# Getting the anime name from the user
anime_name = input('Enter your favourite anime name :')

# Creating a list will all the anime names given in the dataset
list_of_all_title = anime_data['Name'].tolist()
print(list_of_all_title)

# Finding the close match for the anime name given by the user
find_close_match = difflib.get_close_matches(anime_name, list_of_all_title)
print(find_close_match)

close_match = find_close_match[0]
print(close_match)

# Finding the index of the anime with name
index_of_the_anime = anime_data[anime_data.Name == close_match]['index'].values[0]
print(index_of_the_anime)

# Getting a list of similar anime
similarity_score = list(enumerate(similarity[index_of_the_anime]))
print(similarity_score)

len(similarity_score)

# Sorting the anime based on their similarity score
sorted_similar_anime = sorted(similarity_score, key = lambda x:x[1], reverse = True)
print(sorted_similar_anime)

# Print the name of similar anime based on the index
print('Anime Suggestions: \n')

i = 1
for anime in sorted_similar_anime:
    index = anime[0]
    name_from_index = anime_data[anime_data.index == index]['Name'].values[0]
    if (i<30):
      print(i,'.',name_from_index)
      i+=1