from base64 import b64encode
from io import BytesIO

from flask import Flask, render_template, request
from PIL import Image, UnidentifiedImageError

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/reg_items")
def reg_items():
    return render_template("register.html")


@app.route("/list")
def product_list():
    return render_template("simple.html", title="상품 목록", description="작가들이 등록한 핸드메이드 상품을 모아 보는 페이지입니다.")


@app.route("/reg_reviews")
def reg_reviews():
    return render_template("simple.html", title="리뷰 등록", description="구매한 상품의 사진과 사용 후기를 남기는 페이지입니다.")


@app.route("/reviews")
def reviews():
    return render_template("simple.html", title="리뷰 목록", description="구매자들이 남긴 상품 후기를 확인하는 페이지입니다.")


@app.route("/result", methods=["POST"])
def result():
    fields = ("product_name", "seller_id", "price", "address", "status", "email")
    data = {field: request.form.get(field, "").strip() for field in fields}
    picture = request.files.get("picture")
    if not all(data.values()) or not picture or not picture.filename:
        return render_template("simple.html", title="입력 확인", description="모든 항목을 입력하고 상품 사진을 선택해 주세요."), 400
    if not data["price"].isdigit() or data["status"] not in ("새 상품", "거의 새 상품", "사용감 있음"):
        return render_template("simple.html", title="입력 확인", description="가격과 상품 상태를 확인해 주세요."), 400
    content = picture.read()
    try:
        with Image.open(BytesIO(content)) as image:
            image.verify()
            mime = {"PNG": "image/png", "JPEG": "image/jpeg", "WEBP": "image/webp"}.get(image.format)
        if mime is None:
            raise ValueError("Unsupported image")
    except (UnidentifiedImageError, OSError, ValueError):
        return render_template("simple.html", title="사진 확인", description="PNG, JPG, WEBP 형식의 사진을 선택해 주세요."), 400
    image_url = "data:" + mime + ";base64," + b64encode(content).decode("ascii")
    return render_template("result.html", data=data, image_url=image_url, filename=picture.filename)


@app.errorhandler(413)
def too_large(error):
    return render_template("simple.html", title="사진 확인", description="사진을 포함한 전송 크기는 5MB 이하여야 합니다."), 413


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
