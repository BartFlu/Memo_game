from flask import Flask

def create_app():
    app = Flask(__name__)

    from server_memo.main_view import memo_game
    app.register_blueprint(memo_game)

    return app



