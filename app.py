from flask import Flask, request, jsonify

app = Flask(__name__)

# Variable global para almacenar las ubicaciones
locations = []

@app.route('/save-location', methods=['POST'])
def save_location():
    data = request.json
    lat = data.get('lat')
    lon = data.get('lon')
    if lat is not None and lon is not None:
        locations.append({'lat': lat, 'lon': lon})
        return jsonify({'status': 'success', 'message': 'Location saved!'}), 200
    return jsonify({'status': 'error', 'message': 'Invalid data!'}), 400

@app.route('/get-locations', methods=['GET'])
def get_locations():
    return jsonify(locations), 200

if __name__ == '__main__':
    app.run(debug=True)
