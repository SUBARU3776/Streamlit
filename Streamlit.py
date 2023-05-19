import streamlit as st

# Streamlit Building Applications
tweets_df = pd.DataFrame()
st.write("# Twitter data scraping")
option = st.selectbox('How would you like the data to be searched?',('Keyword', 'Hashtag'))
word = st.text_input('Please enter a '+option, 'hogehoge')
start = st.date_input("Select the start date", datetime.date(202*, **, **),key='d1')
end = st.date_input("Select the end date", datetime.date(202*, **, **),key='d2')
tweet_c = st.slider('How many tweets to scrape', 0, 1000, 5)
tweets_list = []

with st.sidebar:   
    st.info('DETAILS', icon="ℹ️")
    if option=='Keyword':
        st.info('Keyword is '+word)
    else:
        st.info('Hashtag is '+word)
    st.info('Starting Date is '+str(start))
    st.info('End Date is '+str(end))
    st.info("Number of Tweets "+str(tweet_c))
    st.info("Total Tweets Scraped "+str(len(tweets_df)))
    x=st.button('Show Tweets',key=1)
    
if not tweets_df.empty:
    col1, col2, col3 = st.columns(3)
    with col1:
        csv = convert_df(tweets_df) # CSV
        c=st.download_button(label="Download data as CSV",data=csv,file_name='Twitter_data.csv',mime='text/csv',)        
    with col2:    # JSON
        json_string = tweets_df.to_json(orient ='records')
        j=st.download_button(label="Download data as JSON",file_name="Twitter_data.json",mime="application/json",data=json_string,)

    with col3: # SHOW
        y=st.button('Show Tweets',key=2)

if c:
    st.success("The Scraped Data is Downloaded as .CSV file:",icon="✅")  
if j:
    st.success("The Scraped Data is Downloaded as .JSON file",icon="✅")     
if x: # DISPLAY
    st.success("The Scraped Data is:",icon="✅")
    st.write(tweets_df)

if y: # DISPLAY
    st.balloons()
