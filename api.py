from flask import Flask, request, jsonify
import threading
import logging
import time
import json

# Task 1: Initialize Flask application
app = Flask(__name__)

# Arnav's message - Configure logging to capture processing details
logging.basicConfig(filename='api_processing.log', level=logging.INFO)

# Task 2: Define the endpoint to receive sensor data
@app.route('/process_data', methods=['POST'])
def process_data():
    # Arnav's message - Get JSON data from the request
    data = request.json
    
    # Arnav's message - Log the receipt of data with timestamp
    timestamp_received = time.time()
    logging.info(f"Data received at {timestamp_received}: {data}")
    
    # Arnav's message - Create and start threads for concurrent processing
    threads = []
    for reading in data.get('sensor_readings', []):
        thread = threading.Thread(target=process_reading, args=(reading, timestamp_received))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Arnav's message - Respond to the client after processing
    return jsonify({"status": "success", "message": "Data processed"}), 200

def process_reading(reading, timestamp_received):
    try:
        # Arnav's message - Simulate processing of each reading
        time.sleep(1)  # Simulate processing time
        
        # Arnav's message - Log the processing of each reading
        timestamp_processed = time.time()
        logging.info(f"Reading processed at {timestamp_processed}: {reading} (Received at {timestamp_received})")
    
    except Exception as e:
        # Arnav's message - Log any exceptions encountered during processing
        logging.error(f"Error processing reading {reading}: {str(e)}")

# Task 3: Start the Flask server
if __name__ == '__main__':
    # Arnav's message - Run the server with high performance settings
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)
