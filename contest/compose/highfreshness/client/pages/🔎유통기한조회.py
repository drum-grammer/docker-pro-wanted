import sys
import streamlit as st
import requests
import pandas as pd
from pathlib import Path
from datetime import datetime, timedelta
sys.path.append(str(Path(__file__).resolve().parent.parent))
from component.config import AP_SERVER_URL 

URL = AP_SERVER_URL + "/ex_date/"

st.title('🔍 유통기한 조회')

col1, col2, col3 = st.columns(3)

with col1:
    days_7 = st.button("7일")
    
with col2:
    days_14 = st.button("14일")
    
with col3:
    days_21 = st.button("21일")
    
if days_7:
    today = datetime.today().strftime("%Y/%m/%d")
    ex_date = datetime.today() + timedelta(days=7)
    ex_date = ex_date.strftime("%Y/%m/%d")
    res = requests.get(url=URL, params={"today":today, "ex_date":ex_date})
    if res.status_code == 200:    
        if len(res.json()) == 0 :
            st.write("해당 기간 내 유통기한 도래 상품이 존재하지 않습니다.")
        else:
            df = pd.DataFrame.from_records(res.json())
            df = df[['ls_cd', 'barcode', 'ls_dt', 'ex_dt', 'ls_ct']]
            df.rename(columns={'ls_cd':'입고코드', 'ls_dt':'입고일자', 'ex_dt':'유효기간', 'ls_ct':'수량'}, inplace=True)
            st.dataframe(df)
    else:
        st.write("현재 통신이 원활하지 않습니다. 관리자를 찾아주세요")
            
elif days_14:
    today = datetime.today().strftime("%Y/%m/%d")
    ex_date = datetime.today() + timedelta(days=14)
    ex_date = ex_date.strftime("%Y/%m/%d")
    res = requests.get(url=URL, params={"today":today, "ex_date":ex_date})
    if res.status_code == 200:    
        if len(res.json()) == 0 :
            st.write("해당 기간 내 유통기한 도래 상품이 존재하지 않습니다.")
        else:
            df = pd.DataFrame.from_records(res.json())
            df = df[['ls_cd', 'barcode', 'ls_dt', 'ex_dt', 'ls_ct']]
            df.rename(columns={'ls_cd':'입고코드', 'ls_dt':'입고일자', 'ex_dt':'유효기간', 'ls_ct':'수량'}, inplace=True)
            st.dataframe(df)
    else:
        st.write("현재 통신이 원활하지 않습니다. 관리자를 찾아주세요")
        
elif days_21:
    today = datetime.today().strftime("%Y/%m/%d")
    ex_date = datetime.today() + timedelta(days=21)
    ex_date = ex_date.strftime("%Y/%m/%d")
    res = requests.get(url=URL, params={"today":today, "ex_date":ex_date})
    if res.status_code == 200:    
        if len(res.json()) == 0 :
            st.write("해당 기간 내 유통기한 도래 상품이 존재하지 않습니다.")
        else:
            df = pd.DataFrame.from_records(res.json())
            df = df[['ls_cd', 'barcode', 'ls_dt', 'ex_dt', 'ls_ct']]
            df.rename(columns={'ls_cd':'입고코드', 'ls_dt':'입고일자', 'ex_dt':'유효기간', 'ls_ct':'수량'}, inplace=True)
            st.dataframe(df)
    else:
        st.write("현재 통신이 원활하지 않습니다. 관리자를 찾아주세요")