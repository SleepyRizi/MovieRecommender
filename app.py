import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movies_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=be4310f62642c1947eaef9dc791a071e&language=en-US'.format(movies_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/original/"+data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity_matrix[movie_index]
    movies_list = sorted(list(enumerate(dise)), reverse=True, key=lambda x: x[1])[1:12]
    recommend_movies = []
    recommend_movies_poster=[]
    for i in movies_list:
        recommend_movies.append(movies.iloc[i[0]].title)
        movie_id= movies.iloc[i[0]]['id']
        recommend_movies_poster.append(fetch_poster(movie_id))

    return recommend_movies,recommend_movies_poster

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity_matrix= pickle.load(open('similarity_matrix.pkl','rb'))

st.title("Xtern")

selected_movie = st.selectbox(
    "Select Movies",
    movies['title'].values
)
if st.button("Recommend"):
    name,posters = recommend(selected_movie)
    col1,col2,col3,col4,col5,col6,col7,col8,col9,col10 = st.columns(10)
    with col1:
        st.text(name[0])
        st.image(posters[0])
    with col1:
        st.text(name[1])
        st.image(posters[1])
    with col2:
        st.text(name[2])
        st.image(posters[2])
    with col3:
        st.text(name[3])
        st.image(posters[3])
    with col4:
        st.text(name[4])
        st.image(posters[4])
    with col5:
        st.text(name[5])
        st.image(posters[5])
    with col6:
        st.text(name[6])
        st.image(posters[6])
    with col7:
        st.text(name[7])
        st.image(posters[7])
    with col8:
        st.text(name[8])
        st.image(posters[5])
    with col9:
        st.text(name[9])
        st.image(posters[9])
    with col10:
        st.text(name[10])
        st.image(posters[10])

