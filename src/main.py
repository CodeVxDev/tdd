from flask import Flask, jsonify, request
import math

app = Flask(__name__)

def circle_area(radius):
    return math.pi * radius ** 2

@app.route('/circle-area')
def get_circle_area():
    try:
        radius = float(request.args.get('radius'))
    except ValueError:
        return jsonify({'area': "Invalid Radius"})
    area = circle_area(radius)
    return jsonify({'area': area})

if __name__ == '__main__':
    app.run()