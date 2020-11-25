from flask import Blueprint, render_template, request, redirect, current_app, flash, url_for
from werkzeug.utils import secure_filename
import pathlib
import os
import random

memo_game = Blueprint('memo', __name__)


@memo_game.route('/')
def main_view():

    return render_template('main_view.html')

@memo_game.route('/choose_own')
def create_uploads():

    return render_template('upload.html')

@memo_game.route("/upload-image", methods=["GET", "POST"])
def upload_image():

    if request.method == "POST":

        if 'files[]' not in request.files:
            print('no files detected')
            return redirect(request.url)

        files = request.files.getlist('files[]')
        print(files)

        for file in files:
            if file.filename == "":  # esuring that file has a file name.
                print("No filename")
                return redirect(url_for('memo.main_view'))

            if allowed_image_filename(file.filename):
                filename = secure_filename(file.filename)

                file.save(os.path.join(current_app.config['USER_IMG'], filename))
                print('image saved')

            else:
                flash('That file extension is not allowed')
                redirect(url_for('memo_game.main_view'))

    return redirect(url_for('memo.main_view'))  # check if correct syntax


def allowed_image_filename(filename):

    # We only want files with a . in the filename
    if "." not in filename:
        return False

    # Split the extension from the filename - dot is a separator, only one split will be made
    ext = filename.rsplit(".", 1)[1]

    # Check if the extension is in AV_EXTENSIONS
    if ext.upper() in current_app.config["AV_EXTENSIONS"]:
        return True
    else:
        return False


@memo_game.route('/game')
def game():
    imgs = {}.fromkeys(range(1, 13), "")
    possible_places = list(range(1, 13))
    script_path = pathlib.Path(__file__).parent.absolute()
    file_path = pathlib.Path(script_path, "static/imgs/Default")
    files = os.listdir(file_path)
    files.remove('photos')
    for i in range(1, 7):
        place = random.choice(possible_places)
        possible_places.remove(place)
        file = random.choice(files)
        files.remove(file)
        imgs[place] = file
        place = random.choice(possible_places)
        possible_places.remove(place)
        imgs[place] = file
    return render_template('template.html', images=imgs)




