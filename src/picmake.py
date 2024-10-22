import requests
import datetime
import json
import re
from PIL import Image, ImageDraw, ImageFont

def 급식(시도교육청코드,행정표준코드,인증키): # 나이스 api를 사용함 
    지금 = datetime.datetime.now()
    API = f"https://open.neis.go.kr/hub/mealServiceDietInfo/?ATPT_OFCDC_SC_CODE={시도교육청코드}&SD_SCHUL_CODE={행정표준코드}&MLSV_YMD={지금.strftime("%Y%m%d")}&Type=json&KEY={인증키}"
    요청 = requests.get(API)
    급식데이터 = json.loads(요청.text)
    급식메뉴 = 급식데이터['mealServiceDietInfo'][1]['row'][0]['DDISH_NM'] #json에서 급식 메뉴만 추출
    급식메뉴 = re.sub(r'<br/>', '\n', 급식메뉴) #br태그 줄바꿈으로 변경
    급식메뉴 = re.sub(r'\([^)]*\)', '', 급식메뉴) #영양성분 표시 제거
    급식메뉴 = 급식메뉴.strip()
    return(급식메뉴)

def 사진(메뉴):
    지금 = datetime.datetime.now()
    이미지 = Image.open("푸른중학교2.png")
    그리기 = ImageDraw.Draw(이미지)
    폰트2 = ImageFont.truetype("Paperlogy-5Medium.ttf", 90)
    폰트 = ImageFont.truetype("Paperlogy-5Medium.ttf", 70)

    중앙 = 그리기.textbbox((0, 0), 메뉴, font=폰트2) # 글자의 중앙 정렬을 위해 만들어짐
    글자넓이, 글자높이 = 중앙[2] - 중앙[0], 중앙[3] - 중앙[1]

    spacing = 20
    position = (1080 - 글자넓이) // 2, (1080 - 글자높이) // 2 - spacing


    그리기.multiline_text(position, f"{메뉴}", fill=(0, 0, 0), font=폰트2,spacing=spacing, align="center")
    위치 = 700,90
    
    그리기.multiline_text(위치, {지금.strftime("%m월%d일")}, fill=(0, 0, 0), font=폰트, align="center")
    
    이미지.save("오늘의_급식.png")
