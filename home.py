import streamlit as st
import cv2
import numpy as np
from PIL import Image
from rembg import remove
from filters import apply_filter
from realtime import realtime_page
from drawing import drawing
from cartoon import cartoon_effect

st.set_page_config(
    page_title="VisionX Editify",
    page_icon="",
    layout="wide"
)
st.markdown("""
<h1 style='font-size:50px; text-align:center;'>
<span style='color:#4FC3F7;'>VisionX</span>
<span style='color:#7F00FF;'> Editify</span>
</h1>
""", unsafe_allow_html=True)

page = st.sidebar.radio("Choose ",["Filter Image","Real Time","Drawing","Cartoon Effect"])
if(page=="Filter Image"):
    apply_filter()
elif(page=="Real Time"):
    realtime_page()
elif(page=="Drawing"):
    drawing()
elif(page=="Cartoon Effect"):
    cartoon_effect()