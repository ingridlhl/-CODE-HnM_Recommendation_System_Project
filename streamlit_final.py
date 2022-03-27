import pandas as pd
import numpy as np
import streamlit as st
#from streamlit_option_menu import option_menu
from PIL import Image
from scipy.spatial import distance
from scipy.spatial.distance import euclidean

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

def read_csv_contentbase_customerdata(path):
    dtypes = {
    'customer_id':'str',
    'article_id':np.int32}
    return pd.read_csv(path, dtype=dtypes)

contentbased_customers = read_csv_contentbase_customerdata('customers_3months.csv')

def read_csv_contentbase_itemdata(path):
    #dtypes = pd.read_csv(path, nrows=1).iloc[0].to_dict()
    return pd.read_csv(path, dtype=int)

contentbased_items=read_csv_contentbase_itemdata('item_feature.csv')

def read_csv_productname(path):
    dtypes = {'article_id':np.int32,'prod_name':str}
    #dtypes = pd.read_csv(path, nrows=1).iloc[0].to_dict()
    return pd.read_csv(path, dtype=dtypes)

productname=read_csv_productname('productname_list.csv')


#collaborative displayresult functions (p1-p10)
#target_df = recommend[recommend['customer_id']== target]
def displayresult_p1():
    p1=recommend.loc[recommend['customer_id'] == target, 'p1'].iloc[0]
    #p1 = target_df.at[target_df.index.item(),'p1']
    p1="0"+p1
    p1_article_df = articles[articles['article_id']== p1]
    p1_prod_name = p1_article_df.at[p1_article_df.index.item(),'prod_name']
    #p1_colour_group_name = p1_article_df.at[p1_article_df.index.item(),'colour_group_name']
    #p1_section_name = p1_article_df.at[p1_article_df.index.item(),'section_name']
    image = Image.open(f'images/{p1[:3]}/{p1}.jpg')
    st.image(image, width=130, caption=f'{p1_prod_name}')
    st.text('')

def displayresult_p2():
    p2=recommend.loc[recommend['customer_id'] == target, 'p2'].iloc[0]
    p2="0"+str(p2)
    p2_article_df = articles[articles['article_id']== p2]
    p2_prod_name = p2_article_df.at[p2_article_df.index.item(),'prod_name']
    image = Image.open(f'images/{p2[:3]}/{p2}.jpg')
    st.image(image, width=130, caption=f'{p2_prod_name}')
    st.text('')

def displayresult_p3():
    p3 = recommend.loc[recommend['customer_id'] == target, 'p3'].iloc[0]
    p3="0"+str(p3)
    p3_article_df = articles[articles['article_id']== p3]
    p3_section_name = p3_article_df.at[p3_article_df.index.item(),'section_name']
    p3_prod_name = p3_article_df.at[p3_article_df.index.item(),'prod_name']
    image = Image.open(f'images/{p3[:3]}/{p3}.jpg')
    st.image(image, width=130, caption=f'{p3_prod_name}')
    st.text('')

def displayresult_p4():
    p4 = recommend.loc[recommend['customer_id'] == target, 'p4'].iloc[0]
    p4="0"+str(p4)
    p4_article_df = articles[articles['article_id']== p4]
    p4_prod_name = p4_article_df.at[p4_article_df.index.item(),'prod_name']
    image = Image.open(f'images/{p4[:3]}/{p4}.jpg')
    st.image(image, width=130, caption=f'{p4_prod_name}')
    st.text('')

def displayresult_p5():
    p5 = recommend.loc[recommend['customer_id'] == target, 'p5'].iloc[0]
    p5="0"+str(p5)
    p5_article_df = articles[articles['article_id']== p5]
    p5_prod_name = p5_article_df.at[p5_article_df.index.item(),'prod_name']
    image = Image.open(f'images/{p5[:3]}/{p5}.jpg')
    st.image(image, width=130, caption=f'{p5_prod_name}')
    st.text('')

def displayresult_p6():
    p6 = recommend.loc[recommend['customer_id'] == target, 'p6'].iloc[0]
    p6="0"+str(p6)
    p6_article_df = articles[articles['article_id']== p6]
    p6_prod_name = p6_article_df.at[p6_article_df.index.item(),'prod_name']
    image = Image.open(f'images/{p6[:3]}/{p6}.jpg')
    st.image(image, width=130, caption=f'{p6_prod_name}')
    st.text('')

def displayresult_p7():
    p7 = recommend.loc[recommend['customer_id'] == target, 'p7'].iloc[0]
    p7="0"+str(p7)
    p7_article_df = articles[articles['article_id']== p7]
    p7_prod_name = p7_article_df.at[p7_article_df.index.item(),'prod_name']
    image = Image.open(f'images/{p7[:3]}/{p7}.jpg')
    st.image(image, width=130, caption=f'{p7_prod_name}')
    st.text('')

def displayresult_p8():
    p8 = recommend.loc[recommend['customer_id'] == target, 'p8'].iloc[0]
    p8="0"+str(p8)
    p8_article_df = articles[articles['article_id']== p8]
    p8_prod_name = p8_article_df.at[p8_article_df.index.item(),'prod_name']
    image = Image.open(f'images/{p8[:3]}/{p8}.jpg')
    st.image(image, width=130, caption=f'{p8_prod_name}')
    st.text('')

def displayresult_p9():
    p9 = recommend.loc[recommend['customer_id'] == target, 'p9'].iloc[0]
    p9="0"+p9
    p9_article_df = articles[articles['article_id']== p9]
    p9_prod_name = p9_article_df.at[p9_article_df.index.item(),'prod_name']
    image = Image.open(f'images/{p9[:3]}/{p9}.jpg')
    st.image(image, width=130, caption=f'{p9_prod_name}')
    st.text('')

def displayresult_p10():
    p10 = recommend.loc[recommend['customer_id'] == target, 'p10'].iloc[0]
    p10="0"+p10
    p10_article_df = articles[articles['article_id']== p10]
    p10_prod_name = p10_article_df.at[p10_article_df.index.item(),'prod_name']
    image = Image.open(f'images/{p10[:3]}/{p10}.jpg')
    st.image(image, width=130, caption=f'{p10_prod_name}')
    st.text('')

#trending displayresult functions (p11-p20)
def displayresult_p11():
    p11 = trend_list[0]
    p11="0"+p11
    p11_article_df = articles[articles['article_id']== p11]
    p11_prod_name = p11_article_df.at[p11_article_df.index.item(),'prod_name']
    image = Image.open(f'images/{p11[:3]}/{p11}.jpg')
    st.image(image, width=130, caption=f'{p11_prod_name}')
    st.text('')

def displayresult_p12():
    p12 = trend_list[1]
    p12="0"+p12
    p12_article_df = articles[articles['article_id']== p12]
    p12_prod_name = p12_article_df.at[p12_article_df.index.item(),'prod_name']
    image = Image.open(f'images/{p12[:3]}/{p12}.jpg')
    st.image(image, width=130, caption=f'{p12_prod_name}')
    st.text('')

def displayresult_p13():
    p13 = trend_list[2]
    p13="0"+p13
    p13_article_df = articles[articles['article_id']== p13]
    p13_prod_name = p13_article_df.at[p13_article_df.index.item(),'prod_name']
    image = Image.open(f'images/{p13[:3]}/{p13}.jpg')
    st.image(image, width=130, caption=f'{p13_prod_name}')
    st.text('')

def displayresult_p14():
    p14 = trend_list[3]
    p14="0"+p14
    p14_article_df = articles[articles['article_id']== p14]
    p14_prod_name = p14_article_df.at[p14_article_df.index.item(),'prod_name']
    image = Image.open(f'images/{p14[:3]}/{p14}.jpg')
    st.image(image, width=130, caption=f'{p14_prod_name}')
    st.text('')

def displayresult_p15():
    p15 = trend_list[4]
    p15="0"+p15
    p15_article_df = articles[articles['article_id']== p15]
    p15_prod_name = p15_article_df.at[p15_article_df.index.item(),'prod_name']
    image = Image.open(f'images/{p15[:3]}/{p15}.jpg')
    st.image(image, width=130, caption=f'{p15_prod_name}')
    st.text('')

def displayresult_p16():
    p16 = trend_list[5]
    p16="0"+p16
    p16_article_df = articles[articles['article_id']== p16]
    p16_prod_name = p16_article_df.at[p16_article_df.index.item(),'prod_name']
    image = Image.open(f'images/{p16[:3]}/{p16}.jpg')
    st.image(image, width=130, caption=f'{p16_prod_name}')
    st.text('')

def displayresult_p17():
    p17 = trend_list[6]
    p17="0"+p17
    p17_article_df = articles[articles['article_id']== p17]
    p17_prod_name = p17_article_df.at[p17_article_df.index.item(),'prod_name']
    image = Image.open(f'images/{p17[:3]}/{p17}.jpg')
    st.image(image, width=130, caption=f'{p17_prod_name}')
    st.text('')

def displayresult_p18():
    p18 = trend_list[7]
    p18="0"+p18
    p18_article_df = articles[articles['article_id']== p18]
    p18_prod_name = p18_article_df.at[p18_article_df.index.item(),'prod_name']
    image = Image.open(f'images/{p18[:3]}/{p18}.jpg')
    st.image(image, width=130, caption=f'{p18_prod_name}')
    st.text('')

def displayresult_p19():
    p19 = trend_list[8]
    p19="0"+p19
    p19_article_df = articles[articles['article_id']== p19]
    p19_prod_name = p19_article_df.at[p19_article_df.index.item(),'prod_name']
    image = Image.open(f'images/{p19[:3]}/{p19}.jpg')
    st.image(image, width=130, caption=f'{p19_prod_name}')
    st.text('')

def displayresult_p20():
    p20 = trend_list[9]
    p20="0"+p20
    p20_article_df = articles[articles['article_id']== p20]
    p20_prod_name = p20_article_df.at[p20_article_df.index.item(),'prod_name']
    image = Image.open(f'images/{p20[:3]}/{p20}.jpg')
    st.image(image, width=130, caption=f'{p20_prod_name}')
    st.text('')

#content-based displayresult functions (p11-p20)
def displayresult_p21():
    p21 = predictionlist[0]
    p21="0"+str(p21)
    p21_article_df = articles[articles['article_id']== p21]
    p21_prod_name = p21_article_df.at[p21_article_df.index.item(),'prod_name']
    image = Image.open(f'images/{p21[:3]}/{p21}.jpg')
    st.image(image, width=130, caption=f'{p21_prod_name}')
    st.text('')

def displayresult_p22():
    p22 = predictionlist[1]
    p22="0"+str(p22)
    p22_article_df = articles[articles['article_id']== p22]
    p22_prod_name = p22_article_df.at[p22_article_df.index.item(),'prod_name']
    image = Image.open(f'images/{p22[:3]}/{p22}.jpg')
    st.image(image, width=130, caption=f'{p22_prod_name}')
    st.text('')

def displayresult_p23():
    p23 = trend_list[2]
    p23="0"+str(p23)
    p23_article_df = articles[articles['article_id']== p23]
    p23_prod_name = p23_article_df.at[p23_article_df.index.item(),'prod_name']
    image = Image.open(f'images/{p23[:3]}/{p23}.jpg')
    st.image(image, width=130, caption=f'{p23_prod_name}')
    st.text('')

def displayresult_p24():
    p24 = trend_list[3]
    p24="0"+str(p24)
    p24_article_df = articles[articles['article_id']== p24]
    p24_prod_name = p24_article_df.at[p24_article_df.index.item(),'prod_name']
    image = Image.open(f'images/{p24[:3]}/{p24}.jpg')
    st.image(image, width=130, caption=f'{p24_prod_name}')
    st.text('')

def displayresult_p25():
    p25 = trend_list[4]
    p25="0"+str(p25)
    p25_article_df = articles[articles['article_id']== p25]
    p25_prod_name = p25_article_df.at[p25_article_df.index.item(),'prod_name']
    image = Image.open(f'images/{p25[:3]}/{p25}.jpg')
    st.image(image, width=130, caption=f'{p25_prod_name}')
    st.text('')

def displayresult_p26():
    p26 = trend_list[5]
    p26="0"+str(p26)
    p26_article_df = articles[articles['article_id']== p26]
    p26_prod_name = p26_article_df.at[p26_article_df.index.item(),'prod_name']
    image = Image.open(f'images/{p26[:3]}/{p26}.jpg')
    st.image(image, width=130, caption=f'{p26_prod_name}')
    st.text('')

def displayresult_p27():
    p27 = trend_list[6]
    p27="0"+str(p27)
    p27_article_df = articles[articles['article_id']== p27]
    p27_prod_name = p27_article_df.at[p27_article_df.index.item(),'prod_name']
    image = Image.open(f'images/{p27[:3]}/{p27}.jpg')
    st.image(image, width=130, caption=f'{p27_prod_name}')
    st.text('')

def displayresult_p28():
    p28 = trend_list[7]
    p28="0"+str(p28)
    p28_article_df = articles[articles['article_id']== p28]
    p28_prod_name = p28_article_df.at[p28_article_df.index.item(),'prod_name']
    image = Image.open(f'images/{p28[:3]}/{p28}.jpg')
    st.image(image, width=130, caption=f'{p28_prod_name}')
    st.text('')

def displayresult_p29():
    p29 = trend_list[8]
    p29="0"+str(p29)
    p29_article_df = articles[articles['article_id']== p29]
    p29_prod_name = p29_article_df.at[p29_article_df.index.item(),'prod_name']
    image = Image.open(f'images/{p29[:3]}/{p29}.jpg')
    st.image(image, width=130, caption=f'{p29_prod_name}')
    st.text('')

def displayresult_p30():
    p30 = trend_list[9]
    p30="0"+str(p30)
    p30_article_df = articles[articles['article_id']== p30]
    p30_prod_name = p30_article_df.at[p30_article_df.index.item(),'prod_name']
    image = Image.open(f'images/{p30[:3]}/{p30}.jpg')
    st.image(image, width=130, caption=f'{p30_prod_name}')
    st.text('')
#streamlit code start--


st.image('hmlogo.png', width=100)
st.header(':jeans: H&M Items Recommendation Tool🛒')

target = st.text_input("Please input customer id:")
submitted = st.button('Submit')
if not submitted:
    imag3 = Image.open('hm1.webp')
    st.image('hm1.webp', width=700)
    st.markdown('###')
    

if submitted: 
    if len(target)<61 or len(target)<64 or target not in recommend["customer_id"]  :
        body="😔We could not find your id. But you can still see what's hot coming soon!"
        st.warning(body)
        st.subheader('🔥The Next 10 Hot Items🔥')
        trend_list=['751471001','810838011','448509014','809901002','706016002','823791006','824526002','706016001','810838010','720125001']
            
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


else: 
    #collabortive 
    recommend.set_index('customer_id')
    #target_df = recommend[recommend['customer_id']== target]
    
    trend_list=['751471001','810838011','448509014','809901002','706016002','823791006','824526002','706016001','810838010','720125001']
    #content-based
    article_id2=contentbased_customers.loc[contentbased_customers['customer_id'] == target, 'article_id'].iloc[0]
    itemlist=contentbased_items.article_id.tolist()
    itemlist.remove(article_id2)
    resultlist=[]
    for x in range(len(itemlist)):
        feature=contentbased_items.loc[contentbased_items['article_id']==itemlist[x]]
        feautre1=feature.iloc[: , 1:]
        article=contentbased_items.loc[contentbased_items['article_id']==article_id2]
        article1=article.iloc[: , 1:]
        y=euclidean(feautre1,article1)
        resultlist.append(y)

    d = {'recommended_itemid':itemlist,'distance':resultlist}
    prediction=pd.DataFrame(d)
    prediction.sort_values(by='distance',ascending=True,inplace=True)
    predictionlist=prediction['recommended_itemid'].head(10).tolist()

    st.subheader('🔥Top 10 Trending Products')
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

    st.subheader('🧑‍🤝‍🧑Customers Also Bought These:')
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

    productname.set_index('article_id')
    purchaseditem1=productname[productname['article_id']== article_id2]
    purchaseditem= purchaseditem1.at[purchaseditem1.index.item(),'prod_name']
    st.subheader('🛍️Product You May Like:')
    st.write("You bought",purchaseditem,"last time! See more similar items!")

    col21,col22,col23,col24,col25 = st.columns(5)
    with col21:
        displayresult_p21()
    with col22:
        displayresult_p22()
    with col23:
        displayresult_p23()
    with col24:
        displayresult_p24()
    with col25:
        displayresult_p25()
    
    col21,col22,col23,col24,col25 = st.columns(5)
    with col21:
        displayresult_p26()
    with col22:
        displayresult_p27()
    with col23:
        displayresult_p28()
    with col24:
        displayresult_p29()
    with col25:
        displayresult_p30()
st.markdown('###')
st.markdown('###')
st.markdown('###')
st.markdown('###')
    
    #if not target is recommend['customer_id']:
        #body="😔We could not find your id. But you can still see what's hot coming soon!"
        #st.warning(body)
        #st.subheader('🔥The next 10 hot items🔥')
        #trend_list=['751471001','810838011','448509014','809901002','706016002','823791006','824526002','706016001','810838010','720125001']
        
        #col11,col12,col13,col14,col15 = st.columns(5)
        #with col11:
            #displayresult_p11()
        #with col12:
            #displayresult_p12()
        #with col13:
           # displayresult_p13()
        #with col14:
            #displayresult_p14()
        #with col15:
            #displayresult_p15()
        #col16,col17,col18,col19,col20 = st.columns(5)
        #with col16:
            #displayresult_p16()
        #with col17:
            #displayresult_p17()
        #with col18:
           # displayresult_p18()
        #with col19:
            #displayresult_p19()
        #with col20:
        #    displayresult_p20()




#draft
    #collabortive 
    #target_df = recommend[recommend['customer_id']== target]
   
    #trend_list=['751471001','810838011','448509014','809901002','706016002','823791006','824526002','706016001','810838010','720125001']
    #content-based
    #article_id2=contentbased_customers.loc[contentbased_customers['customer_id'] == target, 'article_id'].iloc[0]
    #itemlist=contentbased_items.article_id.tolist()
    #itemlist.remove(article_id2)
    #resultlist=[]
    #for x in range(len(itemlist)):
        #feature=contentbased_items.loc[contentbased_items['article_id']==itemlist[x]]
        #feautre1=feature.iloc[: , 1:]
        #article=contentbased_items.loc[contentbased_items['article_id']==article_id2]
        #article1=article.iloc[: , 1:]
        #y=euclidean(feautre1,article1)
        #resultlist.append(y)

    #d = {'recommended_itemid':itemlist,'distance':resultlist}
    #prediction=pd.DataFrame(d)
    #prediction.sort_values(by='distance',ascending=True,inplace=True)
    #predictionlist=prediction['recommended_itemid'].head(10).tolist()

    #st.subheader('🔥The next 10 hot items🔥')
    #col11,col12,col13,col14,col15 = st.columns(5)
    #with col11:
        #displayresult_p11()
    #with col12:
        #displayresult_p12()
    #with col13:
        #displayresult_p13()
    #with col14:
        #displayresult_p14()
    #with col15:
        #displayresult_p15()
    #col16,col17,col18,col19,col20 = st.columns(5)
    #with col16:
        #displayresult_p16()
    #with col17:
        #displayresult_p17()
    #with col18:
        #displayresult_p18()
    #with col19:
        #displayresult_p19()
    #with col20:
        #xdisplayresult_p20(

    #st.subheader('🧑‍🤝‍🧑Customers Also Bought These:')
    #col1,col2,col3,col4,col5 = st.columns(5)
    #with col1:
        #displayresult_p1()
    #with col2:
        #displayresult_p2()
    #with col3:
        #displayresult_p3()
    #with col4:
        #displayresult_p4()
    #with col5:
        #displayresult_p5()
    #col6,col7,col8,col9,col10 = st.columns(5)
    #with col1:
        #displayresult_p6()
    #with col2:
        #displayresult_p7()
    #with col3:
        #displayresult_p8()
    #with col4:
        #displayresult_p9()
    #with col5:
        #displayresult_p10()
    
    #purchaseitem=articles.loc[articles['article_id'] == article_id2, 'prod_name'].iloc[0]
    #st.subheader('🛍️You bought',purchaseitem,'last time! Products you may also like:')

    #col21,col22,col23,col24,col25 = st.columns(5)
    #with col21:
        #displayresult_p21()
    #with col22:
        #displayresult_p22()
    #with col23:
        #displayresult_p23()
    #with col24:
        #displayresult_p24()
    #with col25:
        #displayresult_p25()
    
    #col21,col22,col23,col24,col25 = st.columns(5)
    #with col21:
        #displayresult_p26()
    #with col22:
        #displayresult_p27()
    #with col23:
        #displayresult_p28()
    #with col24:
        #displayresult_p29()
    #with col25:
        #displayresult_p30()




    