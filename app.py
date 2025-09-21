import streamlit as st
import pickle

# Load the pickled files
movies = pickle.load(open('movies.pkl', "rb"))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Prepare movie titles for dropdown
movies_list = movies['title'].values

# Recommend function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list_idx = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = [movies.iloc[i[0]].title for i in movies_list_idx]
    return recommended_movies

# Streamlit UI
st.title('🎬 Movie Recommender System')

selected_movie = st.selectbox(
    "Select a movie:",
    movies_list
)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    st.write(f"{selected_movie}:")
    for movie in recommendations:
        st.write('*', movie)
