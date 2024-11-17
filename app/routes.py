from flask import Blueprint, render_template, send_from_directory, abort, url_for
from app.auth import auth
import os

main = Blueprint('main', __name__)

# dir path
IMAGE_FOLDER = os.getenv('IMAGE_FOLDER')

# Get the list of image files and sort them
image_files = sorted([
    f for f in os.listdir(IMAGE_FOLDER)
    if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))
])

@main.route('/')
@auth.login_required
def index():
    return render_template('index.html', images=image_files)

@main.route('/images/<int:index>')
@auth.login_required
def view_image(index):
    if 0 <= index < len(image_files):
        image = image_files[index]
    else:
        abort(404)

    prev_index = (index - 1) % len(image_files)
    next_index = (index + 1) % len(image_files)

    return render_template('image_view.html', image=image, index=index,
                           prev_index=prev_index, next_index=next_index)

@main.route('/image-files/<filename>')
@auth.login_required
def serve_image(filename):
    return send_from_directory(IMAGE_FOLDER, filename)
