from flask import Flask
import pathlib


def create_app():
    app = Flask(__name__)

    script_path = pathlib.Path(__file__).parent.absolute()
    down_path = pathlib.Path(script_path, "static/imgs/User")
    back_down_path = pathlib.Path(script_path, "static/imgs/User/photos")

    app.config['USER_FRONT'] = down_path
    app.config['USER_BACK'] = back_down_path
    app.config['AV_EXTENSIONS'] = ["JPEG", "JPG", "PNG"]
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

    from server_memo.main_view import memo_game
    app.register_blueprint(memo_game)

    return app



