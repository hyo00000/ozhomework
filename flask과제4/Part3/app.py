from flask import Flask
from flask_smorest import Api
from db import db
from models import User, Board

#app 객체 불러오기
app = Flask(__name__)
#db 연결
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:water1342@localhost/oz'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db.init_app(app)
#메모리 영역에서 객체가 변경 될 때마다 트래킹 할것인지 묻는 것 웬만하면 false로 사용
#앱 객체를 전달해야함


#blurprint 설정
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

from routes.board import board_blp
from routes.user import user_blp
api.register_blueprint(board_blp)
api.register_blueprint(user_blp)

from flask import render_template
@app.route('/manage-boards')
def manage_boards():
    return render_template('boards.html')

@app.route('/manage-users')
def manage_users():
    return render_template('users.html')

# 모델을 만들어 줬을 때 데이터베이스랑 연결도 하고 모델의 테이블이 생성되어있지 않으면 생성해주는 코드
if __name__ == '__main__':
    with app.app_context():
        print("here?")
        db.create_all()
        
    app.run(debug=True)