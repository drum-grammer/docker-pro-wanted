import streamlit as st
from PIL import Image

image = Image.open('freshness.png')
st.image(image)

st.title('')

st.write('무인점포의 필수 프로그램!')
st.write('점포운영의 기본인 원칙인 선도관리를 쉽고 빠르게!')
st.write('유통기한 인식을 통한 재고관리 프로그램으로 무인점포를 편리하게 운영해보세요!')