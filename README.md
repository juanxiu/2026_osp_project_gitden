# 깃든 마켓 Flask 실습

상품 정보를 입력하면 Flask 서버에서 POST 요청을 받아 등록 결과를 보여 준다.
이번 실습에서는 데이터베이스 저장 없이 전달받은 정보와 사진을 확인한다.

## 실행

Python 3.10 이상에서 다음 명령을 실행한다.

```bash
python -m venv venv
source venv/bin/activate
# Windows에서는 venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

브라우저에서 http://127.0.0.1:5000 에 접속한다.

## 파일 구성

- `app.py`: 페이지 라우팅과 상품 등록 POST 처리
- `templates/index.html`: 홈 화면과 공통 내비게이션
- `templates/register.html`: 상품 등록 폼
- `templates/result.html`: 입력값과 사진 출력
- `templates/simple.html`: 상품 목록, 리뷰 등록, 리뷰 목록 설명
- `static/style.css`: 화면 스타일
- `static/images/sample-product.jpg`: 실습 입력용 사진
- `screenshots/`: 입력 화면과 결과 화면 캡처

상품 사진은 PNG, JPG, WEBP를 받으며 전송 크기는 최대 5MB이다.
사진은 결과 페이지에 포함해 표시하고 서버 디스크에는 저장하지 않는다.
입력 예시의 판매자 ID, 거래 장소, 이메일은 시연용 값이다.
