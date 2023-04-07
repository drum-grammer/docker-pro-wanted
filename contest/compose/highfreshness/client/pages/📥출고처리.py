import sys
import streamlit as st
import requests
from datetime import datetime
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from component.config import AP_SERVER_URL

st.title('📥 출고 처리')

URL = AP_SERVER_URL + "/deliver/"

qrcode = st.text_input('상품의 QR을 입력해주세요.', max_chars=21)
barcode = qrcode[:14]
ex_date = qrcode[13:17] + "/" + qrcode[17:19] + "/" + qrcode[19:]
ld_cd = datetime.today().strftime("%Y%m%d%H%M%S%f")
ld_dt = datetime.today().strftime("%Y/%m/%d")

if len(qrcode) == 21:
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"바코드 : {barcode}")
    with col2:
        st.write(f"유통기한 : {ex_date}")
    
    count = st.number_input("출고 수량을 입력해주세요.", 0, 1000)
    
    datas = {
        "ld_cd": ld_cd,
        "ld_dt": ld_dt,
        "barcode": barcode,
        "ex_dt": ex_date,
        "ld_ct": count
    }
    
    if st.button("입력"):
        res = requests.post(url=URL, json=datas)
        if res.status_code == 200:
            st.write("출고입력이 정상적으로 완료되었습니다.")
        else:
            st.write(f"HTTP Response : {res.status_code}")
    
    
else:
    st.write("정확한 QR코드를 입력해주세요. 바코드(13) + 날짜(8) 글자로 총 21글자가 되어야 합니다.")