from cgitb import html

import streamlit as st
import pickle
import pandas as pd
import requests
import numpy as np
import streamlit.components.v1 as components
# from PIL import Image


def recommend(book_name):
    index = np.where(pt.index==book_name)[0][0]
    distances = similarity_scores[index]
    not_similar_items = sorted(list(enumerate(similarity_scores[index])),key = lambda x:x[1])[:5]
    recommended_book = []
    recommended_poster = []
    for i in not_similar_items:
        ind =df['Book-Title'][df['Book-Title'] == pt.index[i[0]]].index.tolist()

        recommended_book.append(pt.index[i[0]])
        recommended_poster.append(df['Image-URL-L'][ind])
    return recommended_book,recommended_poster

books_list = pickle.load(open('books_list.pkl','rb'))
book = pd.DataFrame(books_list)
pt_list = pickle.load(open('pt.pkl','rb'))
pt = pd.DataFrame(pt_list)
df_list = pickle.load(open('df.pkl','rb'))
df = pd.DataFrame(df_list)

similarity_scores = pickle.load(open('similarity.pkl','rb'))

st.title('Book Recommender System')

selected_book_name = st.selectbox(
     'Select the book which You have recently read',
     (book))

if st.button('Recommend'):
    names,poster = recommend(selected_book_name)
    
    # col = st.rows(5)
    # for i in range(5):
    #     # with col[i]:

    #     st.text(names[i])
        
    #     X = str(poster[i])
    #     p = X.split(" ")
    #     q = p[4].split('\n')
        
    #     st.markdown("![Alt Text]("+q[0]+")")
    #     # html_string = "<br>"
    #         # st.markdown(html_string, unsafe_allow_html=True)

    #         # st.text('\n')
    idx = 0 
    while idx < 5:
        #  for _ in range(5):
        X = str(poster[idx])
        p = X.split(" ")
        q = p[4].split('\n')
        cols = st.columns(5) 
        cols[idx].image(q[0], width=150, caption=names[idx])
        idx = idx + 1

           
    

