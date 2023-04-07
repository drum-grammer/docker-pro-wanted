import torch
import cv2



def inference(model, img):
    """
    학습된 모델로 원본 이미지에서 유통기한 부분(이미지)을 추출한다.
    input: yolo model
    output: 상태 코드, 이미지 (정상적이지 않은 경우는 0, 0을 반환)
    """

    try:
        # inference 수행
        with torch.no_grad():
            result = model(img, 640)

        # Inference된 이미지에서 해당 영역만 추출
        crop = result.crop(save=False)

        # memory 초기화 및 캐시 삭제
        del result
        torch.cuda.empty_cache()
        
        value = []
        for i in range(len(crop)):
            v = [1, crop[i]['im']]
            value.append(v)
        
        return len(crop), value

    except:
        return 0, 0


def image_preprocessing(image):
    """
    유통기한 부분만 크롭된 이미지에서 글자를 더 잘 인식하도록 전처리한다.
    input: 유통기한 크롭 이미지
    output: 전처리된 유통기한 크롭 이미지
    """

    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) ## BGR 색상 이미지를 회색조 이미지로 변환
    image_binary = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1] # 임시로 이진화 추가
    image_blur = cv2.GaussianBlur(image_binary, ksize=(3,3), sigmaX=0) ## 가우시안블러 효과를 넣어준다.

    k=cv2.getStructuringElement(cv2.MORPH_RECT,(2,2))

    # 이미지의 빈 공간을 매꿔준다 (1)
    erode = cv2.erode(image_blur,k)
    for i in range(2): 
        erode = cv2.erode(erode,k)

    # 이미지의 빈 공간을 매꿔준다 (2)
    opening=cv2.morphologyEx(erode,cv2.MORPH_OPEN,k)
    for i in range(2):
        opening=cv2.morphologyEx(opening,cv2.MORPH_OPEN,k)

    output_img=opening

    return output_img