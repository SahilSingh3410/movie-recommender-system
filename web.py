import streamlit as st
import pickle
import pandas as pd

movies = pickle.load(open('movies.pkl','rb'))
movie_list = pd.DataFrame(movies)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie = st.selectbox('Get the right movie here...',movie_list['title'].values)

def recommend(movie):
    movie_index = movie_list[movie_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movie_poster = []
    recommended_movie_details = []
    recommended_movie_genre = []
    for i in movies_list:
        recommended_movies.append(movie_list.iloc[i[0]].title)
        recommended_movie_poster.append(movie_list.iloc[i[0]].poster)
        recommended_movie_genre.append(movie_list.iloc[i[0]].genre)
        recommended_movie_details.append(movie_list.iloc[i[0]].details)
    return recommended_movies,recommended_movie_poster,recommended_movie_genre,recommended_movie_details


if st.button('Recommend'):
    names,poster,genres,detail5 = recommend(selected_movie)
    # movie_details = recommended_movie_details(selected_movie)

    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        url1 = detail5[0]
        text1 = names[0]
        link1 = f'[{text1}]({url1})'
        st.markdown(link1,unsafe_allow_html=True)
        st.text(genres[0])
        st.image(poster[0])
    with col2:
        url2 = detail5[1]
        text2 = names[1]
        link2 = f'[{text2}]({url2})'
        st.markdown(link2, unsafe_allow_html=True)
        st.text(genres[1])
        st.image(poster[1])
    with col3:
        url3 = detail5[2]
        text3 = names[2]
        link3 = f'[{text3}]({url3})'
        st.markdown(link3, unsafe_allow_html=True)
        st.text(genres[2])
        st.image(poster[2])
    with col4:
        url4 = detail5[3]
        text4 = names[3]
        link4 = f'[{text4}]({url4})'
        st.markdown(link4, unsafe_allow_html=True)
        st.text(genres[3])
        st.image(poster[3])
    with col5:
        url5 = detail5[4]
        text5 = names[4]
        link5 = f'[{text5}]({url5})'
        st.markdown(link5, unsafe_allow_html=True)
        st.text(genres[4])
        st.image(poster[4])