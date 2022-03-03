import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index= movies[movies['title'] == movie].index[0]
    distance =similarity[movie_index]
    movie_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_movie= []
    for i in movie_list:
        recommended_movie.append(movies.iloc[i[0]].title)
    return recommended_movie    

movie_dict=pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)

similarity=pickle.load(open('similarity.pkl','rb'))

st.title("Movie Recommender System")

option = st.selectbox('What you would like to watch',
movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(option)
    for i in recommendations:
        st.write(i)

