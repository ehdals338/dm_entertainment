import requests
import json

def save_image(image_url, file_name):
    img_response = requests.get(image_url)
    #요청 성공
    if img_response.status_code == 200:
        #파일 저장
        with open(file_name, "wb") as fp:
            fp.write(img_response.content)

#이미지 검색
url = "https://dapi.kakao.com/v2/search/image"
headers = {
    "Authorization" : "KakaoAK b75ebadf43687ac5c1b5be98f59673c4"
}
#쿼리 바꾸고싶은거 바꾸면 될 듯
data = {
    "query" : "에스파 윈터"
}

#이미지 검색 요청
response = requests.post(url, headers=headers, data=data)
#요청 실패 시
if response.status_code != 200:
    print("error! because ", response.json())
    
#요청 성공 시
else:
    count = 0
    for image_info in response.json()['documents']:
        print(f"[{count}th] image_url =", image_info['image_url'])
        #저장될 이미지 파일명
        count += 1
        file_name = "test_%d.jpg" %(count)
        #이미지 저장
        save_image(image_info['image_url'], file_name) 