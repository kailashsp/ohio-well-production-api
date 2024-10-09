# Oil and Gas Well Production API

This Flask-based API provides access to annual production data for oil and gas wells.

## Features

- Retrieve annual production data (oil, gas, and brine) for a specific well
- SQLite database backend for data storage

## Prerequisites

- Python 3.12
- pip (Python package manager)

## Installation

1. Clone the repository: 
    ```
    git clone https://github.com/yourusername/oil-gas-production-api.git
    ```

    ```
    cd oil-gas-production-api
    ```

2. Create a virtual environment: 
    ```
    python -m venv venv
    ```
    ```
    source venv/bin/activate
    ```
3. Install the required packages:
    ```
    pip install -r requirements.txt
    ```

## Usage

1. Ensure your database is set up and populated with data. If not, run:
    ```
    python db_setup.py
    ```

2. Start the Flask server:
```
python main.py
```

3. The API will be available at `http://localhost:8080`

4. To query well data, use the following endpoint:
GET /data?well=<well_number> 
Replace `<well_number>` with the API well number you want to query.

## API Endpoints

### GET /data

Retrieves the annual production data for a specific well.

Query Parameters:
- `well`: The API well number (required)

Sample Response:
  ```json
 {
 "oil": 1000.0,
 "gas": 5000.0,
 "brine": 500.0
}