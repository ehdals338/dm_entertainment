import requests

#펭수사진 URL
url = "http://search1.kakaocdn.net/argon/600x0_65_wr/ImZk3b2X1w8"
#이미지 get 요청
img_response = requests.get(url)
#요청에 성공했으면
if img_response.status_code == 200:
    print("=====[이미지 저장]=====")
    #이미지 저장
    with open("test.jpg", "wb") as fp:
        fp.write(img_response.content)
        