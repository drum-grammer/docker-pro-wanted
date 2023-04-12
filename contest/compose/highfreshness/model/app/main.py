from fastapi import FastAPI, File
import torch
import cv2
import numpy as np

# custom file
from app.get_boundingbox import inference, image_preprocessing
from app.get_text import ocr_api


def run(image):

    # load YOLOv5 with custom weight
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='./yolov5_weight/custom_221117.pt')
    nob, boxes = inference(model, image) # nob: num of boxes # 유통기한 부분만 크롭
    # box_images = [x[1] for x in boxes]
    texts = []
    for i in range(nob): # 각 박스마다 전처리 후 OCR 하여 texts에 추가
        s, img = boxes[i]
        # texts = []
        
        if s: # bounding box 찾은 경우
            pre_img = image_preprocessing(img) # 글자 잘 인식하도록 전처리
            text = ocr_api(pre_img) # 이미지에서 텍스트 추출
            texts.append(text)

        else: # bounding box 찾지 못한 경우
            print("인식하지 못했습니다")
    

    return texts # [['box1', 'ocr', '결과'], ['box2', ' ocr', '결과'], ...]


app = FastAPI()


@app.post("/exp_date")
def predict_ExpDate(file: bytes = File()):
    decoded = cv2.imdecode(np.frombuffer(file, np.uint8), cv2.IMREAD_COLOR)
    result = run(decoded) # box 개수만큼의 ocr 결과 리스트
    return {'exp_date': result}