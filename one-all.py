import time
import streamlit as st
st.set_page_config(
    page_title='One Is All',
    page_icon='🌐',
    layout='wide',
    initial_sidebar_state='collapsed',
    menu_items={}
)

container = st.empty()
for i in range(10):
    with container:
        st.text('''
            Start
        ''')
    time.sleep(0.5)
    with container:
        st.text('''
            Start .
        ''')
    time.sleep(0.5)
    with container:
        st.text('''
            Start ..
        ''')
    time.sleep(0.5)
    with container:
        st.text('''
            Start ...
        ''')
    time.sleep(0.5)
time.sleep(0.5)
container.empty()

with st.columns([1,1,1])[1]:
    st.text('''
        Index Page
    ''')