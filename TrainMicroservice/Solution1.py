from flask import Flask, request, jsonify
import requests,json

app = Flask(__name__)

AUTH_TOKEN = "TzEfMS"
API_BASE_URL = "http://20.244.56.144"

# Registration endpoint
@app.route('/train/register', methods=['POST'])
def register():
    try:
        data = {
            "companyName": "Your Company Name",
            "ownerName": "Owner Name",
            "rollNo": "Your Roll Number",
            "ownerEmail": "owner@example.com",
            "accessCode": "Your Access Code"
        }
        response = requests.post(f"{API_BASE_URL}/train/register", json=data)
        response_data = response.json()  # This line might raise JSONDecodeError
        return jsonify(response_data), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "API request error"}), 500
    except json.JSONDecodeError as e:
        return jsonify({"error": "Invalid JSON response"}), 500


# Authorization endpoint
@app.route('/train/auth', methods=['POST'])
def get_auth_token():
    try:
        data = {
            "companyName": "Your Company Name",
            "clientID": "Your Client ID",
            "clientSecret": "Your Client Secret"
        }
        response = requests.post(f"{API_BASE_URL}/train/auth", json=data)
        response_data = response.json()  
        return jsonify(response_data), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "API request error"}), 500
    except json.JSONDecodeError as e:
        return jsonify({"error": "Invalid JSON response"}), 500

# Train schedules endpoint
@app.route('/train/trains', methods=['GET'])
def get_train_schedule():
    try:
        response = requests.get(f"{API_BASE_URL}/train/trains")
        response_data = response.json()  
        return jsonify(response_data), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "API request error"}), 500
    except json.JSONDecodeError as e:
        return jsonify({"error": "Invalid JSON response"}), 500

# Specific train details endpoint
@app.route('/train/trains/<train_id>', methods=['GET'])
def get_train_details(train_id):
    response = requests.get(f'{API_BASE_URL}/train/trains/{train_id}')

    if response.status_code == 200:
        train_details = response.json()
        return jsonify(train_details), 200
    else:
        return jsonify({"message": "An error occurred while fetching train details"}), response.status_code

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5000)
