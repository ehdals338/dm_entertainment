import requests

url = "http://search1.kakaocdn.net/argon/600x0_65_wr/ImZk3b2X1w8"

img_response = requests.get(url)

if img_response.status_code == 200:
    print("=====[이미지 저장]=====")
    with open("test.jpg", "wb") as fp:
        fp.write(img_response.content)