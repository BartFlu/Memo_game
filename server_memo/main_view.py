from flask import Blueprint, render_template, request, redirect
import pathlib
import os
import random

memo_game = Blueprint('memo', __name__)


@memo_game.route('/')
def main_view():

    script_path = pathlib.Path(__file__).parent.absolute()
    file_path = pathlib.Path(script_path, "static/imgs")

    img_collections = os.listdir(file_path)
    img_collections.remove('photos')

    return render_template('main_view.html', img_collections=img_collections)


@memo_game.route("/upload-image", methods=["GET", "POST"])
def upload_image():

    if request.method == "POST":

        if request.files:

            image = request.files["image"]

            print(image)

            return redirect(request.url)

    return redirect('memo_game.main_view')  # check if correct syntax


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




