# Anime Recommendation System
This **Anime Recommendation System** is a content-based recommendation system that works by comparing the selected features of anime using cosine similarity.

### Dataset
* The dataset used in this project is derived from MyAnimeList's Database.
* The provided dataset has been modified to work effectively with the code.
* You can access the original dataset from [Kaggle](https://www.kaggle.com/datasets/hernan4444/anime-recommendation-database-2020)

### Data Collection and Preprocessing:
* Loads anime data from a CSV file.
* Selects relevant features like Genres, Studios, and Source for recommendation.
* Combines these features into a single string for each anime.
* Converts text data into feature vectors using TF-IDF (Term Frequency-Inverse Document Frequency) vectorization.

### Cosine Similarity:
* Calculates the similarity between anime based on the cosine similarity of their feature vectors.
* Takes input from the user for their favorite anime.

### Recommendation Process:
* Finds the closest match for the anime name provided by the user within the dataset.
* Retrieves the index of the matched anime.
* Computes the similarity scores of all anime with respect to the user's input.
* Sorts the anime based on their similarity scores in descending order.
* Outputs a list of suggested anime titles.

### How it Recommends:
* The recommendation system relies on the idea that similar anime will have similar textual features in terms of genres, studios, and sources. By calculating the cosine similarity between the feature vectors of anime descriptions, it identifies anime with similar textual descriptions to the user's input.
* The script takes a user's favorite anime as input and compares its textual features with the entire dataset to find the most similar anime.
