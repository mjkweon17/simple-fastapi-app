from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {
        "data": [
            {
                "id": "1",
                "user_id": "1",
                "user_name": "김현채",
                "reviewContent": "23-1 컴과 전공이었던 권민재 교수님 개발학개론 전공도서였습니다. 아마 계속 이 교재로 하실 듯?",
                "createdAt": "24.07.26"
            },
            {
                "id": "1",
                "user_id": "2",
                "user_name": "현지수",
                "reviewContent": "파이썬 처음 하시는 분들께 추천! 저는 이걸로 스터디 햇어용 우하하",
                "createdAt": "24.07.26"
            }
        ]
    }