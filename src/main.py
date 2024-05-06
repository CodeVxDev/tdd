from flask import Flask, jsonify, request
import math

app = Flask(__name__)

def circle_area(radius):
    return math.pi * radius ** 2

@app.route('/circle-area')
def get_circle_area():
    try:
        radius = float(request.args.get('radius'))
        if radius <= 0:
            return {'error': "Radius must be a positive number."}, 400
    except ValueError:
        return {'error': "Radius must be a positive number."}, 400
    area = circle_area(radius)
    return {'area': area}

if __name__ == '__main__':
    app.run()