# app.py
from flask import Flask, request, jsonify, render_template
from beambending import Beam, DistributedLoadV, PointLoadV, x
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    print(data)

    # Extract beam and support data
    beam_length = data['beam_length']
    pinned_support = data['pinned_support']
    rolling_support = data['rolling_support']

    # Define the beam and supports
    beam = Beam(beam_length)
    beam.pinned_support = pinned_support
    beam.rolling_support = rolling_support

    # Apply point loads
    for load in data['point_loads']:
        point_load = PointLoadV(load['value'], load['position'])
        beam.add_loads((point_load,))

    # Apply distributed loads
    for load in data['distributed_loads']:
        start_value = load['startValue']
        end_value = load['endValue']
        start_position = load['startPosition']
        end_position = load['endPosition']
        slope = (end_value - start_value) / (end_position - start_position)
        distributed_load = DistributedLoadV(start_value + (x - start_position) * slope, (start_position, end_position))
        beam.add_loads((distributed_load,))

    # Generate beam plots
    img = io.BytesIO()
    fig = beam.plot_bending_moment()
    fig.savefig(img, format='png')
    img.seek(0)
    moment_plot_url = base64.b64encode(img.getvalue()).decode()

    img = io.BytesIO()
    fig = beam.plot_shear_force()
    fig.savefig(img, format='png')
    img.seek(0)
    shear_plot_url = base64.b64encode(img.getvalue()).decode()

    return jsonify({
        'moment_plot': f'data:image/png;base64,{moment_plot_url}',
        'shear_plot': f'data:image/png;base64,{shear_plot_url}'
    })

if __name__ == '__main__':
    app.run(debug=True)
