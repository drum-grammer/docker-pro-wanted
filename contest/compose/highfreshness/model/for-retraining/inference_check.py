# 제대로 추론되지 않은 이미지를 따로 모아두기 위함

# 0. 추론할 이미지 폴더(images), 잘못 추론한 이미지 폴더(garbages) 필요
# 1. 모델 불러오기
# 2. 모델에 이미지 넣기 (추론)
# 3. 추론 결과 확인 (imshow)
# 4. 제대로 됐으면 Enter, 제대로 안 됐으면 Esc(이미지 저장)

import torch
import cv2
import os
import shutil
import numpy as np

from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.get_boundingbox import inference


model = torch.hub.load('ultralytics/yolov5', 'custom', path='YOLOv5 Weight/custom_221117.pt')

images_dir = 'for-retraining/images' # 추론할 원본 이미지가 담긴 폴더
garbages_dir = 'for-retraining/garbages' # 잘못 추론된 원본 이미지가 담긴 폴더
file_list = os.listdir(images_dir)
file_list_len = len(file_list)

for i, file_name in enumerate(file_list):
    print(f"{i+1}/{file_list_len}")
    file_path = images_dir + '/' + file_name
    image = cv2.imread(file_path, cv2.IMREAD_COLOR) # 원본
    image = cv2.resize(image, (500, 500))

    nob, boxes = inference(model, image) # nob: num of boxes # 유통기한 부분만 크롭
    print("detection한 box 개수 :", nob)
    
    box_images = [x[1] for x in boxes]
    box_images = [cv2.resize(x, (500, 200)) for x in box_images]
    
    vertical = np.vstack([image, *box_images])
    cv2.imshow(file_name, vertical)

    key = cv2.waitKey()

    if key == 13:  # Enter를 누르면 (유통기한 부분을 잘 가져왔으면)
        print("정상적으로 디텍션된 파일입니다.")
        cv2.destroyAllWindows()

    elif key == 27: # Esc를 누르면 (유통기한 부분이 잘못 가져와졌으면)
        garbage_path = garbages_dir + '/' + file_name
        shutil.move(file_path, garbage_path)
        cv2.destroyAllWindows()
        print(f"정상적으로 디텍션되지 않았으므로 {file_name}을 garbages 폴더로 이동했습니다.")
    
    print("------------------------------")