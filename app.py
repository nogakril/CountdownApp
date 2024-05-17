from flask import Flask, request, jsonify, render_template
app = Flask(__name__, static_folder='static', template_folder='templates')

data_store = {}
next_id = 1

@app.route('/submit', methods=['POST'])
def submit_data():
    global next_id
    json_data = request.get_json()
    data_store[next_id] = json_data
    next_id += 1
    return jsonify({"success": True, "message": "Data added", "id": next_id - 1}), 201

@app.route('/latest', methods=['GET'])
def get_latest():
    if data_store:
        max_key = max(data_store.keys())
        return jsonify(data_store[max_key])
    else:
        return jsonify({"error": "No data available"}), 404

@app.route('/')
def index():
    return render_template('index.html', data_store=data_store)

if __name__ == '__main__':
    app.run(debug=True)
