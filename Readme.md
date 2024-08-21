# Real-Time Data Processing API

This RESTful API is designed to handle high-frequency incoming sensor data and process each request concurrently using multithreading. It provides an endpoint to receive and process sensor readings and logs all relevant details for tracking and debugging.

## Features

- **Concurrent Processing**: Handles sensor data processing concurrently using Python's threading.
- **High Throughput**: Capable of managing multiple requests simultaneously with minimal response time.
- **Logging**: Logs the receipt and processing of each request, including timestamps and errors.
- **Scalability**: Optimized to handle increasing loads effectively.

## Setup and Usage

### **1. Install Dependencies**

Ensure you have the required Python packages installed. You can use `pip` to install them:

```bash
pip install Flask
