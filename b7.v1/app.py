# Importing Flask and other libraries
from flask import Flask, request, render_template, send_file
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import arabic_reshaper, bidi.algorithm

# Creating a Flask app
app = Flask(__name__)

# Defining a route for the home page
@app.route('/')
def home():
    # Rendering a HTML templates for the home page
    return render_template('home.html')

# Defining a route for the image generation page
@app.route('/generate', methods=['POST'])
def generate():
    # Getting the user input from the form
    name = request.form.get('name')
    place = request.form.get('place')

    # Open an Image
    img = Image.open('t3zeh.png')

    # Call draw Method to add 2D graphics in an image
    draw = ImageDraw.Draw(img)

    # Here Custom Name

    Font_name = ImageFont.truetype('Al-Jazeera-Arabic-Bold.ttf', 140)
    text2 = arabic_reshaper.reshape(name)
    final_name = bidi.algorithm.get_display(text2)
    # Add Text to an image
    draw.text((1700, 3285), text=final_name,anchor="ma", font=Font_name, fill=(10, 12, 7) )

    # Here Custom Place
    Font_place = ImageFont.truetype('Al-Jazeera-Arabic-Bold.ttf', 110)
    place2 = arabic_reshaper.reshape(place)
    final_place = bidi.algorithm.get_display(place2)
     # Add Text to an image
    draw.text((2730, 190), text=final_place,anchor="ma", font=Font_place, fill=(10, 12, 7))

    # Saving the image in a temporary file
    img.save('static/temp.png')

    # Rendering a HTML templates for the image generation page and passing the image file name as a parameter
    return render_template('generate.html', image_file='temp.png')

# Defining a route for the image download page
@app.route('/download/<filename>')
def download(filename):
    # Sending the image file as a response with the appropriate MIME type
    return send_file('static/' + filename, mimetype='image/png')

# Running the app

