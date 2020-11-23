from flask import Blueprint, render_template
import pathlib
import os
import random

memo_game = Blueprint('memo', __name__)


@memo_game.route('/')
def game():
    imgs = {}.fromkeys(range(1, 13), "")
    possible_places = list(range(1, 13))
    script_path = pathlib.Path(__file__).parent.absolute()
    file_path = pathlib.Path(script_path, "static/imgs")
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




