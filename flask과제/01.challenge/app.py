from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    data = {
        'title' : '사용자 목록',
    }
    users = [
        {"username": "traveler", "name": "Alex"},
        {"username": "photographer", "name": "Sam"},
        {"username": "gourmet", "name": "Chris"}
    ]
# (1) rendering 할 html 파일명 입력
# (2) html 로 넘겨줄 데이터 입력
    return render_template("index.html", data=data, users=users)

if __name__ == "__main__":
    app.run(debug = True)

