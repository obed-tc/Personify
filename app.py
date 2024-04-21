from flask import Flask, send_from_directory,render_template
import hashlib
import os

app = Flask(__name__)

avatar_directory = "assets/"

avatar_directory_male = os.path.join(avatar_directory, "male")
avatar_directory_female = os.path.join(avatar_directory, "female")

avatar_files_male = os.listdir(avatar_directory_male)
avatar_files_female = os.listdir(avatar_directory_female)

def generate_avatar_for_name_and_gender(name, gender):
    identifier = f"{name}_{gender}"
    hash_object = hashlib.sha256(identifier.encode())
    hash_hex = hash_object.hexdigest()
    avatar_index = int(hash_hex, 16) % len(avatar_files_male if gender == "male" else avatar_files_female)
    avatar_files = avatar_files_male if gender == "male" else avatar_files_female
    return avatar_files[avatar_index]

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/generate_avatar/<gender>/<name>')
def generate_avatar(gender, name):
    avatar_filename = generate_avatar_for_name_and_gender(name, gender)
    avatar_directory = avatar_directory_male if gender == "male" else avatar_directory_female
    return send_from_directory(avatar_directory, avatar_filename)

if __name__ == '__main__':
    app.run(debug=True)
