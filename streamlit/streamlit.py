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
recommend = read_csv('result_use.csv')

def read_csv(path):
    # Read types first line of csv
    dtypes = pd.read_csv(path, nrows=1).iloc[0].to_dict()
    # Read the rest of the lines with the types from above
    return pd.read_csv(path, dtype=dtypes, skiprows=[1,2])
articles = read_csv('articles_use.csv')

#collaborative displayresult functions (p1-p10)

def displayresult_p1():
    p1 = target_df.at[target_df.index.item(),'p1']
    p1="0"+p1
    p1_article_df = articles[articles['article_id']== p1]
    p1_prod_name = p1_article_df.at[p1_article_df.index.item(),'prod_name']
    #p1_colour_group_name = p1_article_df.at[p1_article_df.index.item(),'colour_group_name']
    #p1_section_name = p1_article_df.at[p1_article_df.index.item(),'section_name']
    image = Image.open(f'/Users/yuenchitcheng/Downloads/h-and-m-personalized-fashion-recommendations/images/{p1[:3]}/{p1}.jpg')
    st.image(image, width=130, caption=f'{p1_prod_name}')
    st.text('')

def displayresult_p2():
    p2 = target_df.at[target_df.index.item(),'p2']
    p2="0"+p2
    p2_article_df = articles[articles['article_id']== p2]
    p2_prod_name = p2_article_df.at[p2_article_df.index.item(),'prod_name']
    image = Image.open(f'/Users/yuenchitcheng/Downloads/h-and-m-personalized-fashion-recommendations/images/{p2[:3]}/{p2}.jpg')
    st.image(image, width=130, caption=f'{p2_prod_name}')
    st.text('')

def displayresult_p3():
    p3 = target_df.at[target_df.index.item(),'p3']
    p3="0"+p3
    p3_article_df = articles[articles['article_id']== p3]
    p3_section_name = p3_article_df.at[p3_article_df.index.item(),'section_name']
    p3_prod_name = p3_article_df.at[p3_article_df.index.item(),'prod_name']
    image = Image.open(f'/Users/yuenchitcheng/Downloads/h-and-m-personalized-fashion-recommendations/images/{p3[:3]}/{p3}.jpg')
    st.image(image, width=130, caption=f'{p3_prod_name}')
    st.text('')

def displayresult_p4():
    p4 = target_df.at[target_df.index.item(),'p4']
    p4="0"+p4
    p4_article_df = articles[articles['article_id']== p4]
    p4_prod_name = p4_article_df.at[p4_article_df.index.item(),'prod_name']
    image = Image.open(f'/Users/yuenchitcheng/Downloads/h-and-m-personalized-fashion-recommendations/images/{p4[:3]}/{p4}.jpg')
    st.image(image, width=130, caption=f'{p4_prod_name}')
    st.text('')

def displayresult_p5():
    p5 = target_df.at[target_df.index.item(),'p5']
    p5="0"+p5
    p5_article_df = articles[articles['article_id']== p5]
    p5_prod_name = p5_article_df.at[p5_article_df.index.item(),'prod_name']
    image = Image.open(f'/Users/yuenchitcheng/Downloads/h-and-m-personalized-fashion-recommendations/images/{p5[:3]}/{p5}.jpg')
    st.image(image, width=130, caption=f'{p5_prod_name}')
    st.text('')

def displayresult_p6():
    p6 = target_df.at[target_df.index.item(),'p5']
    p6="0"+p6
    p6_article_df = articles[articles['article_id']== p6]
    p6_prod_name = p6_article_df.at[p6_article_df.index.item(),'prod_name']
    image = Image.open(f'/Users/yuenchitcheng/Downloads/h-and-m-personalized-fashion-recommendations/images/{p6[:3]}/{p6}.jpg')
    st.image(image, width=130, caption=f'{p6_prod_name}')
    st.text('')

def displayresult_p7():
    p7 = target_df.at[target_df.index.item(),'p7']
    p7="0"+p7
    p7_article_df = articles[articles['article_id']== p7]
    p7_prod_name = p7_article_df.at[p7_article_df.index.item(),'prod_name']
    image = Image.open(f'/Users/yuenchitcheng/Downloads/h-and-m-personalized-fashion-recommendations/images/{p7[:3]}/{p7}.jpg')
    st.image(image, width=130, caption=f'{p7_prod_name}')
    st.text('')

def displayresult_p8():
    p8 = target_df.at[target_df.index.item(),'p8']
    p8="0"+p8
    p8_article_df = articles[articles['article_id']== p8]
    p8_prod_name = p8_article_df.at[p8_article_df.index.item(),'prod_name']
    image = Image.open(f'/Users/yuenchitcheng/Downloads/h-and-m-personalized-fashion-recommendations/images/{p8[:3]}/{p8}.jpg')
    st.image(image, width=130, caption=f'{p8_prod_name}')
    st.text('')

def displayresult_p9():
    p9 = target_df.at[target_df.index.item(),'p9']
    p9="0"+p9
    p9_article_df = articles[articles['article_id']== p9]
    p9_prod_name = p9_article_df.at[p9_article_df.index.item(),'prod_name']
    image = Image.open(f'/Users/yuenchitcheng/Downloads/h-and-m-personalized-fashion-recommendations/images/{p9[:3]}/{p9}.jpg')
    st.image(image, width=130, caption=f'{p9_prod_name}')
    st.text('')

def displayresult_p10():
    p10 = target_df.at[target_df.index.item(),'p10']
    p10="0"+p10
    p10_article_df = articles[articles['article_id']== p10]
    p10_prod_name = p10_article_df.at[p10_article_df.index.item(),'prod_name']
    image = Image.open(f'/Users/yuenchitcheng/Downloads/h-and-m-personalized-fashion-recommendations/images/{p10[:3]}/{p10}.jpg')
    st.image(image, width=130, caption=f'{p10_prod_name}')
    st.text('')

def displayresult_p11():
    p11 = trend_list[0]
    p11="0"+p11
    p11_article_df = articles[articles['article_id']== p11]
    p11_prod_name = p11_article_df.at[p11_article_df.index.item(),'prod_name']
    image = Image.open(f'/Users/yuenchitcheng/Downloads/h-and-m-personalized-fashion-recommendations/images/{p11[:3]}/{p11}.jpg')
    st.image(image, width=130, caption=f'{p11_prod_name}')
    st.text('')

def displayresult_p12():
    p12 = trend_list[1]
    p12="0"+p12
    p12_article_df = articles[articles['article_id']== p12]
    p12_prod_name = p12_article_df.at[p12_article_df.index.item(),'prod_name']
    image = Image.open(f'/Users/yuenchitcheng/Downloads/h-and-m-personalized-fashion-recommendations/images/{p12[:3]}/{p12}.jpg')
    st.image(image, width=130, caption=f'{p12_prod_name}')
    st.text('')

def displayresult_p13():
    p13 = trend_list[2]
    p13="0"+p13
    p13_article_df = articles[articles['article_id']== p13]
    p13_prod_name = p13_article_df.at[p13_article_df.index.item(),'prod_name']
    image = Image.open(f'/Users/yuenchitcheng/Downloads/h-and-m-personalized-fashion-recommendations/images/{p13[:3]}/{p13}.jpg')
    st.image(image, width=130, caption=f'{p13_prod_name}')
    st.text('')

def displayresult_p14():
    p14 = trend_list[3]
    p14="0"+p14
    p14_article_df = articles[articles['article_id']== p14]
    p14_prod_name = p14_article_df.at[p14_article_df.index.item(),'prod_name']
    image = Image.open(f'/Users/yuenchitcheng/Downloads/h-and-m-personalized-fashion-recommendations/images/{p14[:3]}/{p14}.jpg')
    st.image(image, width=130, caption=f'{p14_prod_name}')
    st.text('')

def displayresult_p15():
    p15 = trend_list[4]
    p15="0"+p15
    p15_article_df = articles[articles['article_id']== p15]
    p15_prod_name = p15_article_df.at[p15_article_df.index.item(),'prod_name']
    image = Image.open(f'/Users/yuenchitcheng/Downloads/h-and-m-personalized-fashion-recommendations/images/{p15[:3]}/{p15}.jpg')
    st.image(image, width=130, caption=f'{p15_prod_name}')
    st.text('')

def displayresult_p16():
    p16 = trend_list[5]
    p16="0"+p16
    p16_article_df = articles[articles['article_id']== p16]
    p16_prod_name = p16_article_df.at[p16_article_df.index.item(),'prod_name']
    image = Image.open(f'/Users/yuenchitcheng/Downloads/h-and-m-personalized-fashion-recommendations/images/{p16[:3]}/{p16}.jpg')
    st.image(image, width=130, caption=f'{p16_prod_name}')
    st.text('')

def displayresult_p17():
    p17 = trend_list[6]
    p17="0"+p17
    p17_article_df = articles[articles['article_id']== p17]
    p17_prod_name = p17_article_df.at[p17_article_df.index.item(),'prod_name']
    image = Image.open(f'/Users/yuenchitcheng/Downloads/h-and-m-personalized-fashion-recommendations/images/{p17[:3]}/{p17}.jpg')
    st.image(image, width=130, caption=f'{p17_prod_name}')
    st.text('')

def displayresult_p18():
    p18 = trend_list[7]
    p18="0"+p18
    p18_article_df = articles[articles['article_id']== p18]
    p18_prod_name = p18_article_df.at[p18_article_df.index.item(),'prod_name']
    image = Image.open(f'/Users/yuenchitcheng/Downloads/h-and-m-personalized-fashion-recommendations/images/{p18[:3]}/{p18}.jpg')
    st.image(image, width=130, caption=f'{p18_prod_name}')
    st.text('')

def displayresult_p19():
    p19 = trend_list[8]
    p19="0"+p19
    p19_article_df = articles[articles['article_id']== p19]
    p19_prod_name = p19_article_df.at[p19_article_df.index.item(),'prod_name']
    image = Image.open(f'/Users/yuenchitcheng/Downloads/h-and-m-personalized-fashion-recommendations/images/{p19[:3]}/{p19}.jpg')
    st.image(image, width=130, caption=f'{p19_prod_name}')
    st.text('')

def displayresult_p20():
    p20 = trend_list[9]
    p20="0"+p20
    p20_article_df = articles[articles['article_id']== p20]
    p20_prod_name = p20_article_df.at[p20_article_df.index.item(),'prod_name']
    image = Image.open(f'/Users/yuenchitcheng/Downloads/h-and-m-personalized-fashion-recommendations/images/{p20[:3]}/{p20}.jpg')
    st.image(image, width=130, caption=f'{p20_prod_name}')
    st.text('')
#streamlit code start--


st.image('hmlogo.png', width=100)
#st.subheader(':jeans: H&M Items Recommendation Tool')
target = st.text_input("Please input customer id:") 
submitted = st.button('Submit')

if submitted:
    target_df = recommend[recommend['customer_id']== target]
    trend_list=['751471001','810838011','448509014','809901002','706016002','823791006','824526002','706016001','810838010','720125001']
    st.subheader('Other People Also Bought')
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

    st.subheader('Trending Products')
    col11,col12,col13,col14,col15 = st.columns(5)
    with col11:
        displayresult_p11()
    with col12:
        displayresult_p12()
    with col13:
        displayresult_p13()
    with col14:
        displayresult_p14()
    with col15:
        displayresult_p15()
    col16,col17,col18,col19,col20 = st.columns(5)
    with col16:
        displayresult_p16()
    with col17:
        displayresult_p17()
    with col18:
        displayresult_p18()
    with col19:
        displayresult_p19()
    with col20:
        displayresult_p20()





