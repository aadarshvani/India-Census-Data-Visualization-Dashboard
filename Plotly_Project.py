import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objects as go

###### -Layout and configuration- ########

st.set_page_config(layout='wide')

###### -Data Cleaning and Pre-Processing- ########

df = pd.read_csv("D:\\DSMP\\Week 9 - Data Visualization\\Project\\India_Census.csv")

list_of_states= list(df['State'].unique())
list_of_states.sort()
list_of_states.insert(0,'Overall India')
# list_of_states.insert(0, 'Overall India')
###### -User Interface of the Application- ########

st.title('Project')

#-------Sidebar-------#

st.sidebar.title('Data Visualization Menu')

selected_state= st.sidebar.selectbox('Select a State', list_of_states)
primary = st.sidebar.selectbox('Select Primary Parameter', sorted(df.columns[5:]))
secondary = st.sidebar.selectbox('Select Secondary Parameter', sorted(df.columns[5:]))

plot = st.sidebar.button('Plot Graph')

if plot:
    st.text('Size represent Primary Parameter')
    st.text('Color represent Secondary Parameter')
    if selected_state == 'Overall India':
        #ploting for India
        fig = px.scatter_mapbox(df, lat= 'Latitude', lon='Longitude',
                                size=primary, color= secondary, 
                                zoom=4, mapbox_style='carto-positron',
                                width=300, height=700, 
                                hover_name='District'
                                )
        st.plotly_chart(fig, use_container_width=True)
    else:
        #plot for state
        state_df= df[df['State'] ==selected_state]
        fig = px.scatter_mapbox(state_df, lat= 'Latitude', lon='Longitude',
                                size=primary, color= secondary, 
                                zoom=5, mapbox_style='carto-positron',
                                width=300, height=700, 
                                hover_name='District'
                                )
        st.plotly_chart(fig, use_container_width=True)