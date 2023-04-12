import requests
import json
import time
import numpy as np
import uuid
import cv2

from app.config import OCR_API_URL, OCR_SECRET_KEY


def ocr_api(image):
    """
    CLOVA OCR API를 사용하여 유통기한 크롭 이미지에서 텍스트를 추출한다.
    input: 유통기한 크롭 이미지
    output: 추출된 텍스트를 공백으로 이은 한 줄의 텍스트
    """
    
    cv2.imwrite("source.jpg", image)

    path = 'source.jpg'
    files = [('file', open(path,'rb'))] # return [('file', <_io.BufferedReader name='image.jpg'>)]

    request_json = {'images': [{'format': 'jpg',
                                    'name': 'demo'
                                }],
                        'requestId': str(uuid.uuid4()),
                        'version': 'V2',
                        'timestamp': int(round(time.time() * 1000))
                    }
    
    payload = {'message': json.dumps(request_json).encode('UTF-8')}
    
    headers = {
    'X-OCR-SECRET': OCR_SECRET_KEY,
    }
    
    response = requests.request("POST", OCR_API_URL, headers=headers, data=payload, files=files)
    result = response.json()

    text = []
    for field in result['images'][0]['fields']:
        text.append(field['inferText'])

    return text


