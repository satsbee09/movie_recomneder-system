import streamlit as st
import pickle
import requests
import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Movie Recommender"}




# ---------------- Fetch poster from TMDB ----------------
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=5c50a6bde501df1cb4c462f7187628cd&language=en-US"
    response = requests.get(url)
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# ---------------- Recommendation function ----------------
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters


# ---------------- Load Pickle Files ----------------
movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

# ---------------- Streamlit UI ----------------
st.title("🎬 Movie Recommender System")
st.write("Get similar movie suggestions with posters using TMDB API")

selected_movie = st.selectbox("Select a movie:", movies['title'].values)

if st.button("Recommend"):
    names, posters = recommend(selected_movie)

    cols = st.columns(5)  # 5 recommendations side by side
    for col, name, poster in zip(cols, names, posters):
        with col:
            st.text(name)
            st.image(poster)
