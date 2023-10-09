from flask import Flask, request, jsonify, send_file
import os
from util import Sonify
import logging
from PIL import Image

app = Flask(__name__, static_folder='jwst', static_url_path='')


@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('app.html')


@app.route('/api/generate', methods=['POST'])
def generate():
    logging.warning("Reached here")

    # logging.warn(request.files)
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    image_file = request.files['image']

    # Check if the file has a valid file name
    if image_file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    image_file = image_file.stream
    img = Image.open(image_file)
    logging.warning(img)
    sonify = Sonify(
        image=img, soundfont_path='/workspaces/space-2023/Levi_s_Violin.sf2')

    sonify.run()
    # result = sonify.output_video_path
    # os.remove(result)
    # return send_file(result, as_attachment=True, mimetype='video/mp4')
    result = sonify.output_video_path
    # os.remove(result)
    return send_file(result, as_attachment=True, mimetype='video/mp4')

    # return "done"
    # You can save the image file to a specific location if needed
    # image_file.save('path/to/save/image.png')
    # Alternatively, you can process the image directly
    # For example, you can use a library like Pillow to work with the image
    # from PIL import Image
    # img = Image.open(image_file)

    # return jsonify({"message": "Image uploaded successfully"})

    # except Exception as e:
    #     return jsonify({"error": str(e)}), 500

    sonify = Sonify(image=image_file)
    sonify.run()
    result = sonify.output_video_path
    os.remove(result)
    return sendfile(result, as_attachment=True, mimetype='video/mp4')


if __name__ == '__main__':
    app.run(debug=True)
