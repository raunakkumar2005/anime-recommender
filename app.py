import streamlit as st 
import pickle
import pandas as pd
import requests
def poster(anime_id,anime_name):
    path = f"https://myanimelist.net/anime/{anime_id}/{anime_name}/pics"
    return path

def recommend(movie):
    movie_index = movies[movies['names'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movie_posters = []
    recomended_movies = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].anime_id
        movie_name = movies.iloc[i[0]].names
        movie_name.replace(" ","_")
        recomended_movies.append(movies.iloc[i[0]].names)
        recommended_movie_posters.append(poster(movie_id,movie_name))
    return recomended_movies,recommended_movie_posters


movies_dict= pickle.load(open('animes_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)


similarity= pickle.load(open('similarity1.pkl','rb'))

st.title('Movie Recommender System')
selected_movie_name = st.selectbox('choose a movie here',movies['names'].values)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)

    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])