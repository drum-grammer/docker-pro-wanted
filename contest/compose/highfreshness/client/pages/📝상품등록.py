import sys
import requests
import streamlit as st
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from component.config import AP_SERVER_URL

URL = AP_SERVER_URL + "/item/"

st.title('📝 상품 등록')

item_cd = st.text_input("바코드")

col1, col2, col3= st.columns(3)

with col1:
    item_nm = st.text_input("제품명")
    
with col2:
    item_cat_nm = st.text_input("분류")
    
with col3:
    item_maker = st.text_input("제조사")
    
if st.button("전송"):
    if item_cd and item_cat_nm and item_nm and item_maker:
        datas = {
            "item_cd": item_cd,
            "item_nm": item_nm,
            "item_cat_nm": item_cat_nm,
            "item_maker" : item_maker
        }
        res = requests.post(url = URL, json=datas, timeout=3)
        print(res.json())
        
        print(type(res.json()))
        if res.status_code == 200:
            st.write("상품이 정상적으로 등록되었습니다.")
            st.write(f"등록된 상품 : {res.json()['item_nm']}")
        else:
            st.write("상품이 정상적으로 등록되지 않았습니다. 바코드 또는 입력값을 확인해주세요")
    else:
        st.write("빈 항목이 있습니다. 다시 확인 해주세요")