from flask import Flask, render_template, request, jsonify, send_from_directory
import requests

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Change this in production

# Route for serving static files
@app.route('/static/<path:filename>')
def custom_static(filename):
    return send_from_directory('static', filename)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for the search IP page
@app.route('/search_ip')
def search_ip():
    return render_template('search_ip.html')

# Route for the map view page
@app.route('/map')
def map_view():
    return render_template('map.html')

# Route for the terminal page
@app.route('/terminal')
def terminal():
    return render_template('terminal.html')

# Route for the network scanner page
@app.route('/network_scanner')
def network_scanner():
    return render_template('network_scanner.html')

# Route for the vulnerability scanner page
@app.route('/vulnerability_scanner')
def vulnerability_scanner():
    return render_template('vulnerability_scanner.html')

# Route for the password cracker page
@app.route('/password_cracker')
def password_cracker():
    return render_template('password_cracker.html')

# Route for the forensics tools page
@app.route('/forensics_tools')
def forensics_tools():
    return render_template('forensics_tools.html')

# Route for fetching IP information
@app.route('/host_info', methods=['GET'])
def host_info():
    ip = request.args.get('ip')
    if not ip:
        return jsonify({"error": "IP address is required"}), 400

    try:
        response = requests.get(f'https://ipinfo.io/{ip}/json')
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()

        return jsonify({
            "ip": data.get('ip', 'N/A'),
            "hostname": data.get('hostname', 'N/A'),
            "city": data.get('city', 'N/A'),
            "region": data.get('region', 'N/A'),
            "country": data.get('country', 'N/A'),
            "loc": data.get('loc', 'N/A')
        })
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Request error: {str(e)}"}), 500
    except ValueError as e:
        return jsonify({"error": f"Error parsing response: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
