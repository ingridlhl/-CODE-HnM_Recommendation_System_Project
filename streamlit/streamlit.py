import pandas as pd
import numpy as np
import streamlit as st
#from streamlit_option_menu import option_menu
from PIL import Image

#read csv without changing the dtypes

def read_csv(path):
    # Read types first line of csv
    dtypes = pd.read_csv(path, nrows=1).iloc[0].to_dict()
    # Read the rest of the lines with the types from above
    return pd.read_csv(path, dtype=dtypes, skiprows=[1])
recommend = read_csv('/Users/ingrid/Documents/FTDS/recommendationproject-0322/streamlit/result_use.csv')

def read_csv(path):
    # Read types first line of csv
    dtypes = pd.read_csv(path, nrows=1).iloc[0].to_dict()
    # Read the rest of the lines with the types from above
    return pd.read_csv(path, dtype=dtypes, skiprows=[1,2])
articles = read_csv('/Users/ingrid/Documents/FTDS/recommendationproject-0322/streamlit/articles_use.csv')

#collaborative displayresult functions (p1-p10)

def displayresult_p1():
    p1 = target_df.at[target_df.index.item(),'p1']
    p1_article_df = articles[articles['article_id']== p1]
    p1_prod_name = p1_article_df.at[p1_article_df.index.item(),'prod_name']
    #p1_colour_group_name = p1_article_df.at[p1_article_df.index.item(),'colour_group_name']
    #p1_section_name = p1_article_df.at[p1_article_df.index.item(),'section_name']
    image = Image.open(f'/Users/ingrid/Documents/FTDS/recommendationproject-0322/streamlit/images/{p1[:3]}/{p1}.jpg')
    st.image(image, width=130, caption=f'{p1_prod_name}')

def displayresult_p2():
    p2 = target_df.at[target_df.index.item(),'p2']
    p2_article_df = articles[articles['article_id']== p2]
    p2_prod_name = p2_article_df.at[p2_article_df.index.item(),'prod_name']
    image = Image.open(f'/Users/ingrid/Documents/FTDS/recommendationproject-0322/streamlit/images/{p2[:3]}/{p2}.jpg')
    st.image(image, width=130, caption=f'{p2_prod_name}')

def displayresult_p3():
    p3 = target_df.at[target_df.index.item(),'p3']
    p3_article_df = articles[articles['article_id']== p3]
    p3_section_name = p3_article_df.at[p3_article_df.index.item(),'section_name']
    p3_prod_name = p3_article_df.at[p3_article_df.index.item(),'prod_name']
    image = Image.open(f'/Users/ingrid/Documents/FTDS/recommendationproject-0322/streamlit/images/{p3[:3]}/{p3}.jpg')
    st.image(image, width=130, caption=f'{p3_prod_name}')

def displayresult_p4():
    p4 = target_df.at[target_df.index.item(),'p4']
    p4_article_df = articles[articles['article_id']== p4]
    p4_prod_name = p4_article_df.at[p4_article_df.index.item(),'prod_name']
    image = Image.open(f'/Users/ingrid/Documents/FTDS/recommendationproject-0322/streamlit/images/{p4[:3]}/{p4}.jpg')
    st.image(image, width=130, caption=f'{p4_prod_name}')

def displayresult_p5():
    p5 = target_df.at[target_df.index.item(),'p5']
    p5_article_df = articles[articles['article_id']== p5]
    p5_prod_name = p5_article_df.at[p5_article_df.index.item(),'prod_name']
    image = Image.open(f'/Users/ingrid/Documents/FTDS/recommendationproject-0322/streamlit/images/{p5[:3]}/{p5}.jpg')
    st.image(image, width=130, caption=f'{p5_prod_name}')

def displayresult_p6():
    p6 = target_df.at[target_df.index.item(),'p5']
    p6_article_df = articles[articles['article_id']== p6]
    p6_prod_name = p6_article_df.at[p6_article_df.index.item(),'prod_name']
    image = Image.open(f'/Users/ingrid/Documents/FTDS/recommendationproject-0322/streamlit/images/{p6[:3]}/{p6}.jpg')
    st.image(image, width=130, caption=f'{p6_prod_name}')

def displayresult_p7():
    p7 = target_df.at[target_df.index.item(),'p7']
    p7_article_df = articles[articles['article_id']== p7]
    p7_prod_name = p7_article_df.at[p7_article_df.index.item(),'prod_name']
    image = Image.open(f'/Users/ingrid/Documents/FTDS/recommendationproject-0322/streamlit/images/{p7[:3]}/{p7}.jpg')
    st.image(image, width=130, caption=f'{p7_prod_name}')

def displayresult_p8():
    p8 = target_df.at[target_df.index.item(),'p8']
    p8_article_df = articles[articles['article_id']== p8]
    p8_prod_name = p8_article_df.at[p8_article_df.index.item(),'prod_name']
    image = Image.open(f'/Users/ingrid/Documents/FTDS/recommendationproject-0322/streamlit/images/{p8[:3]}/{p8}.jpg')
    st.image(image, width=130, caption=f'{p8_prod_name}')

def displayresult_p9():
    p9 = target_df.at[target_df.index.item(),'p9']
    p9_article_df = articles[articles['article_id']== p9]
    p9_prod_name = p9_article_df.at[p9_article_df.index.item(),'prod_name']
    image = Image.open(f'/Users/ingrid/Documents/FTDS/recommendationproject-0322/streamlit/images/{p9[:3]}/{p9}.jpg')
    st.image(image, width=130, caption=f'{p9_prod_name}')

def displayresult_p10():
    p10 = target_df.at[target_df.index.item(),'p10']
    p10_article_df = articles[articles['article_id']== p10]
    p10_prod_name = p10_article_df.at[p10_article_df.index.item(),'prod_name']
    image = Image.open(f'/Users/ingrid/Documents/FTDS/recommendationproject-0322/streamlit/images/{p10[:3]}/{p10}.jpg')
    st.image(image, width=130, caption=f'{p10_prod_name}')

#streamlit code start--


st.image('hmlogo.png', width=100)
#st.subheader(':jeans: H&M Items Recommendation Tool')
target = st.text_input("Please input customer id:")
submitted = st.button('Submit')

if submitted:
    target_df = recommend[recommend['customer_id']== target]
    st.subheader('1/ Collaborative Recommendation System')
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        displayresult_p1()
    with col2:
        displayresult_p2()
    with col3:
        displayresult_p3()
    with col4:
        displayresult_p4()
    with col5:
        displayresult_p5()
    col6,col7,col8,col9,col10 = st.columns(5)
    with col1:
        displayresult_p6()
    with col2:
        displayresult_p7()
    with col3:
        displayresult_p8()
    with col4:
        displayresult_p9()
    with col5:
        displayresult_p10()





