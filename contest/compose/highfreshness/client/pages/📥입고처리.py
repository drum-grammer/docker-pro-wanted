# import os 
import sys
from pathlib import Path

# os.environ['DISPLAY'] = ':0'
sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st
from webcam import webcam
from datetime import datetime
import requests
import re
# import pyautogui
import qrcode

from component.config import INFERENCE_SERVER_URL, AP_SERVER_URL
from component.func import ImageFile
from component.post_processing import get_expdate

PICTURE_URL = AP_SERVER_URL + "/picture/"
STOCK = AP_SERVER_URL + "/stock/"
# 기본 설정
if 'last' not in st.session_state:
    st.session_state.last = None

if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False
                    
def button_clicked():
    st.session_state.button_clicked = True


st.title('📥 입고처리')

barcode = st.text_input('빈 칸에 바코드를 입력해주세요.', placeholder='13자리를 입력해주세요', max_chars=13)

        
if len(barcode) == 13:
    check_cam = st.radio(label = '< 내장캠 / 웹캠 > 을 선택해주세요.', options = ['Maincam', 'Webcam'])
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        
    if check_cam == 'Maincam': # 내장 캠인 경우

        image_file = ImageFile()
        captured_image = st.camera_input('상품의 유통기한을 인식해주세요.')

        if captured_image is None:
            st.write('정면으로 인식되었다면 <Take Photo> 를 눌러주세요.')
            
        else:
            buffered_stream = image_file.image_to_buffer(captured_image)
            upload = {'file': buffered_stream}
            print(upload)

            # 추론
            inference = requests.post(url=INFERENCE_SERVER_URL, files=upload)
            exp_date = get_expdate(inference.json()["exp_date"])
            print("추론 결과 :", inference, inference.text)

            # 화면에 표시할 정보
            st.write(f'< 바코드번호 : {barcode}>')
            st.write('상품정보 : 식품')
            st.write(f'유통기한 : {exp_date}')
            st.write('-------')

            # 재촬영인 경우 재학습용 DB 서버로 보냄
            if st.session_state.last != None:
                buffered_stream = image_file.image_to_buffer(captured_image)
                upload = {'file': buffered_stream}
                res = requests.post(url=PICTURE_URL, files=upload)
                print("재촬영 이미지 전송 결과 :", res, res.text)

                st.session_state.last = buffered_stream # 다음 촬영 시 보내기 위해 저장
                image_file.drop_image(buffered_stream) # 이미지 파일 삭제
            
            else:
                st.session_state.last = buffered_stream
            

            # 예측된 유통기한을 그대로 사용할지(확인), 수정하여 사용할지(직접입력) 선택
            check_info = st.radio(label = '유통기한 정보를 확인해주세요.', options = ['확인', '직접입력'])     
            
            # 확인
            if check_info == '확인':
                count = st.number_input('수량을 입력해주세요.', 0, 1000)
                
                if st.button('QR 생성'):
                    exp_date_num = re.sub(r'[^0-9]', '', str(exp_date))   
                    img = qrcode.make(f"{barcode}{exp_date_num}")
                    img.save(f"./pages/qr_code/{barcode}{exp_date_num}.jpg")
                    st.image(f"./pages/qr_code/{barcode}{exp_date_num}.jpg")

                if st.button('등록'):
                    ls_dt = datetime.now()
                    ls_dt = ls_dt.strftime('%Y/%m/%d')

                    ls_cd = datetime.today().strftime("%Y%m%d%H%M%S%f")

                    data = {
                        'ls_cd': ls_cd,
                        'ls_dt': ls_dt,
                        'barcode': barcode,
                        'ex_dt': str(exp_date),
                        'ls_ct': count
                        }

                    res = requests.post(url=STOCK, json=data)
                    print("입고 DB 전송 결과 :", res, res.text)
                    st.success(f' < 바코드번호 : {barcode} / {count} 개 > 등록되었습니다 ')
                    #pyautogui.press("f5", presses=1, interval=0.2)
                
            # 직접 입력
            else :
                ex1, co2 = st.columns(2)
                with ex1 :
                    exp_date = st.date_input('유통기한을 입력해주세요.')
                    exp_date = str(exp_date).replace('-', '/')
                with co2 :
                    count = st.number_input('수량을 입력해주세요', 0, 1000)
                    
                if st.button('QR 생성'):
                    exp_date_num = re.sub(r'[^0-9]', '', str(exp_date))   
                    img = qrcode.make(f"{barcode}{exp_date_num}")
                    img.save(f"./pages/qr_code/{barcode}{exp_date_num}.jpg")
                    st.image(f"./pages/qr_code/{barcode}{exp_date_num}.jpg")

                if st.button('등록'):
                    ls_dt = datetime.now()
                    ls_dt = ls_dt.strftime('%Y/%m/%d')

                    ls_cd = datetime.today().strftime("%Y%m%d%H%M%S%f")

                    data = {
                        'ls_cd': ls_cd,
                        'ls_dt': ls_dt,
                        'barcode': barcode,
                        'ex_dt': str(exp_date),
                        'ls_ct': count
                        }

                    res = requests.post(url=STOCK, json=data)
                    print("입고 DB 전송 결과 :", res, res.text)
                    st.success(f' < 바코드번호 : {barcode} / {count} 개 > 등록되었습니다 ')
                    #pyautogui.press("f5", presses=1, interval=0.2)

    # 외장 캠인 경우           
    else:
        image_file = ImageFile()
        captured_image = webcam('상품의 유통기한을 인식해주세요')
        
        if captured_image is None:
            st.write('정면으로 인식되었다면 <Capture frame> 을 눌러주세요')
            
        else:
            buffered_stream = image_file.image_to_buffer(captured_image)
            upload = {'file': buffered_stream}

            # 추론
            inference = requests.post(url=INFERENCE_SERVER_URL, files=upload)
            exp_date = get_expdate(inference.json()["exp_date"])
            print("추론 결과 :", inference, inference.text)

            # 화면에 표시할 정보
            st.write(f'< 바코드번호 : {barcode}>')
            st.write('상품정보 : 식품')
            st.write(f'유통기한 : {exp_date}')
            st.write('-------')

            # 재촬영인 경우 재학습용 DB 서버로 보냄
            if st.session_state.last != None:
                buffered_stream = image_file.image_to_buffer(captured_image)
                upload = {'file': buffered_stream}
                res = requests.post(url=PICTURE_URL, files=upload)
                print("재촬영 이미지 전송 결과 :", res, res.text)
            
                st.session_state.last = buffered_stream # 다음 촬영 시 보내기 위해 저장
                image_file.drop_image(buffered_stream) # 이미지 파일 삭제
            
            else:
                st.session_state.last = buffered_stream

            # 예측된 유통기한을 그대로 사용할지(확인), 수정하여 사용할지(직접입력) 선택
            check_info = st.radio(label = '유통기한 정보를 확인해주세요', options = ['확인', '직접입력'])
            
            # 확인
            if check_info == '확인':
                count = st.number_input('수량을 입력해주세요', 0, 1000)
                
                if st.button('QR 생성'):
                    exp_date_num = re.sub(r'[^0-9]', '', str(exp_date))   
                    img = qrcode.make(f"{barcode}{exp_date_num}")
                    img.save(f"./qr_code/{barcode}{exp_date_num}.jpg")
                    st.image(f"./qr_code/{barcode}{exp_date_num}.jpg")


                if st.button('등록'):
                    ls_dt = datetime.now()
                    ls_dt = ls_dt.strftime('%Y/%m/%d')

                    ls_cd = datetime.today().strftime("%Y%m%d%H%M%S%f")

                    data = {
                        'ls_cd': ls_cd,
                        'ls_dt': ls_dt,
                        'barcode': barcode,
                        'ex_dt': str(exp_date),
                        'ls_ct': count
                        }

                    res = requests.post(url=STOCK, json=data)
                    print("입고 DB 전송 결과 :", res, res.text)
                    st.success(f' < 바코드번호 : {barcode} / {count} 개 > 등록되었습니다 ')
                    #pyautogui.press("f5", presses=1, interval=0.2)

            # 직접 입력
            else :
                ex1, co2 = st.columns(2)
                with ex1 :
                    exp_date = st.date_input('유통기한을 입력해주세요.')
                    exp_date = str(exp_date).replace('-', '/')
                with co2 :
                    count = st.number_input('수량을 입력해주세요', 0, 1000)
                    
                if st.button('QR 생성'):
                    exp_date_num = re.sub(r'[^0-9]', '', str(exp_date))   
                    img = qrcode.make(f"{barcode}{exp_date_num}")
                    img.save(f"./pages/qr_code/{barcode}{exp_date_num}.jpg")
                    st.image(f"./pages/qr_code/{barcode}{exp_date_num}.jpg")

                if st.button('등록'):
                    ls_dt = datetime.now()
                    ls_dt = ls_dt.strftime('%Y/%m/%d')

                    ls_cd = datetime.today().strftime("%Y%m%d%H%M%S%f")

                    data = {
                        'ls_cd': ls_cd,
                        'ls_dt': ls_dt,
                        'barcode': barcode,
                        'ex_dt': str(exp_date),
                        'ls_ct': count
                        }

                    res = requests.post(url=STOCK, json=data)
                    print("입고 DB 전송 결과 :", res, res.text)
                    st.success(f' < 바코드번호 : {barcode} / {count} 개 > 등록되었습니다 ')
                    # pyautogui.press("f5", presses=1, interval=0.2)