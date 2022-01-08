import streamlit as st

from pynse import *
import datetime 
import matplotlib.pyplot as plt
import mplfinance
import plotly.express as px

nse = Nse()
def bhavcopy_display():
    with st.sidebar:
        st.write('Bhavcopy Inputs')
        req_date = st.date_input('Select Date',datetime.date.today())
        segment = st.selectbox('Select Segment', ['Cash','FnO'])
        
    req_date = None if req_date >= datetime.date.today() else req_date()
    
    if segment == 'Cash':
        bhavcopy = nse.bhavcopy(req_date)
    else:
        bhavcopy = nse.bhavcopy_fno(req_date)
    st.write(f'{segment} bhavcopy for {req_date}')
    st.download_button(
        'Download', bhavcopy.to_csv(),file_name=f'{segment}_bhav_{req_date}.csv'
    )
    st.write(bhavcopy)



analysis_dict = {'Bhavcopy':bhavcopy_display}

with st.sidebar:
    selected_analysis = st.radio('Select Analysis', list(analysis_dict.keys()))
    st.write('-------')
st.header(selected_analysis)

analysis_dict[selected_analysis]()
