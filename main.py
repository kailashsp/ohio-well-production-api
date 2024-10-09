from flask import Flask, request, jsonify
from sqlalchemy.exc import SQLAlchemyError

from db_setup import DbProcessor

db_inst = DbProcessor()

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_well_data():
    try:
        well_number = request.args.get('well')
        if not well_number:
            app.logger.warning('Request received without well number')
            return jsonify({"error": "Well number not provided"}), 400

        well_data = db_inst.filter_annual_data(well_number)

        if well_data:
            return jsonify({
                "oil": well_data.oil,
                "gas": well_data.gas,
                "brine": well_data.brine
            })
        else:
            return jsonify({"error": "Well not found"}), 404
    except ValueError:
        return jsonify({"error": "Invalid well number format"}), 400
    except SQLAlchemyError as e:
        app.logger.error(f"Database error: {str(e)}")
        return jsonify({"error": "Database error occurred"}), 500
    except Exception as e:
        app.logger.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": "An unexpected error occurred"}), 500

if __name__ == '__main__':
    app.run(port=8080)