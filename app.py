from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Database configuration
#with open(r'./PASS/database.txt', 'r') as file:
#    database_key = file.read().strip()
DB_NAME = "gis5572"
DB_USER = "postgres"
DB_PASSWORD = "Passwordd"
DB_HOST = "35.188.97.184"
DB_PORT = "5432"

# Route to retrieve polygon as GeoJSON
@app.route('/get_polygon_geojson')
def get_polygon_geojson():
    # Connect to the database
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

    # Create a cursor
    cur = conn.cursor()

    # Execute SQL query to retrieve the polygon
    cur.execute("SELECT ST_AsGeoJSON(shape) AS geojson FROM arclab1 LIMIT 1;")
    row = cur.fetchone()

    # Close cursor and connection
    cur.close()
    conn.close()

    # Return the GeoJSON
    return jsonify(row)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))