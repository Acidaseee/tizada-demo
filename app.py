from flask import Flask, render_template, request, send_file
from PIL import Image, ImageDraw
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    fabric_width = int(request.form['fabric_width'])
    fabric_height = int(request.form['fabric_height'])
    pattern_width = int(request.form['pattern_width'])
    pattern_height = int(request.form['pattern_height'])

    img = Image.new("RGB", (fabric_width, fabric_height), "white")
    draw = ImageDraw.Draw(img)

    count = 0
    for y in range(0, fabric_height, pattern_height):
        for x in range(0, fabric_width, pattern_width):
            if x + pattern_width <= fabric_width and y + pattern_height <= fabric_height:
                draw.rectangle(
                    [(x, y), (x + pattern_width - 1, y + pattern_height - 1)],
                    fill=(100, 200, 255),
                    outline="black"
                )
                count += 1

    output = io.BytesIO()
    img.save(output, format='PNG')
    output.seek(0)

    return send_file(output, mimetype='image/png', as_attachment=True, download_name='tizada.png')

if __name__ == '__main__':
    app.run(debug=True)
