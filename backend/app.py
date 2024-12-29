from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)
CORS(app)

@app.route('/render', methods=['POST'])
def render_text():
    data = request.json
    text = data.get('text')
    font_size = data.get('font_size', 20)
    font_path = "arial.ttf"  # Ensure this exists in your server

    img = Image.new('RGB', (800, 600), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, font_size)
    draw.text((100, 100), text, font=font, fill=(0, 0, 0))

    output_path = "static/uploads/output.png"
    img.save(output_path)

    return jsonify({"message": "Image created", "path": output_path})

if __name__ == "__main__":
    app.run(debug=True)
