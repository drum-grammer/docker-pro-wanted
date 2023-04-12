from streamlit.runtime.uploaded_file_manager import UploadedFile
from PIL import Image
from datetime import datetime
from pytz import timezone
import os
import re


class ImageFile():
    def __init__(self):
        pass


    def make_filepath(self):
        self.time = str(datetime.now(timezone("Asia/Seoul")))
        self.time = re.sub(r'[.|:]', '', self.time) # 파일명에 사용할 수 없는 문자열 제거
        directory = 'temp_images/'
        
        return directory + f'{self.time}.jpg'


    def image_to_buffer(self, img): # img에 captured_image
        self.path = self.make_filepath()

        if type(img) == UploadedFile:
            image = Image.open(img)
        elif type(img) == Image.Image:
            image = img.convert("RGB")
        else: # 파일이 내장캠이나 외장캠 모두 아닌 경우 파일을 저장하지 않고 중단
            return
        
        image.save(self.path)
        buffer = open(self.path, 'rb')
        
        return buffer
    

    def drop_image(self, buffer):
        buffer.close()
        os.remove(self.path)