import sys
import streamlit as st
import requests
import pandas as pd
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from component.config import AP_SERVER_URL 
URL = AP_SERVER_URL + "/stock/"

st.title('🔍 입고 조회')

col1, col2 = st.columns(2)

with col1:
    front_time = st.date_input("조회 시작 기간")
    front_time = str(front_time).replace("-", "/")
with col2:
    back_time = st.date_input("조회 종료 기간")
    back_time = str(back_time).replace("-", "/")
if st.button('입고 조회'):
    if front_time != None and back_time != None:
        res = requests.get(url=URL, params = {"period_front":front_time, "period_back":back_time})
    stock_json = res.json() # type = list

    if len(stock_json) == 0:
        st.write("해당 기간에 입고된 내역이 없습니다.")
    else:
        df = pd.DataFrame.from_records(stock_json)
        df = df[['ls_cd', 'ls_dt', 'ex_dt', 'ls_ct', 'barcode']]
        df.rename(columns={'barcode':'바코드', 'ls_cd':'입고코드', 'ex_dt':'유효기간', 'ls_dt':'입고일자', 'ls_ct':'수량'}, inplace=True)
        st.dataframe(df)
