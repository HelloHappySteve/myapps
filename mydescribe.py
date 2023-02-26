import streamlit as st
import time
st.set_page_config(
    page_title='MyDescribe',
    page_icon='🌐',
    layout='wide',
    initial_sidebar_state='collapsed'
)
container = st.container()
time.sleep(0.2)
container.markdown('# `Hello`')
container.markdown('# `My name is Steve Brown`')
container.markdown("# `I'm from QingHua Middle School`")
container.markdown('# `This is my first website`')
container.markdown('# `If you want to know about me`')
container.markdown('# `-*----**----***--**---*-**---`')
container.markdown('# `......`')
