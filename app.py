from flask import Flask, jsonify
import os
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

@app.route('/')
def hello_world():
    return "hello world!"

# Route to retrieve polygon as GeoJSON
@app.route('/geojson_polygon')
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
    cur.execute("""SELECT 
            json_build_object(
                'type', 'FeatureCollection',
                'features', json_agg(
                    json_build_object(
                        'type', 'Feature',
                        'geometry', ST_AsGeoJSON(ST_SetSRID(shape, 4326))::json,
                        'properties', json_build_object()
                    )
                ),
                'crs', 
                json_build_object(
                    'type', 'name',
                    'properties', 
                    json_build_object(
                        'name', 'EPSG:4326'
                    )
                )
            ) AS geojson
        FROM arclab1""")
    row = cur.fetchone()[0]

    # Close cursor and connection
    cur.close()
    conn.close()

    # Return the GeoJSON
    return row


# Route to retrieve polygon as GeoJSON
@app.route('/elevation_interpolation')
def elevation_universalkriging_point():
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
    cur.execute("""SELECT 
                    json_build_object(
                        'type', 'FeatureCollection',
                        'features', json_agg(
                            json_build_object(
                                'type', 'Feature',
                                'geometry', ST_AsGeoJSON(ST_Transform(ST_SetSRID(shape, 26915), 4326))::json,
                                'properties', json_build_object(
                                    'objectid', objectid,
                                    'pointid', pointid,
                                    'grid_code', grid_code
                                )
                            )
                        ),
                        'crs', 
                        json_build_object(
                            'type', 'name',
                            'properties', 
                            json_build_object(
                                'name', 'EPSG:4326'
                            )
                        )
                    ) AS geojson
                FROM elevation_universalkriging_point;
                """)
    rows = cur.fetchone()[0]

    # Close cursor and connection
    cur.close()
    conn.close()

    # Return the GeoJSON
    return rows


# Route to retrieve polygon as GeoJSON
@app.route('/elevation_accuracy')
def elevation_accuracy():
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
    cur.execute("""SELECT 
                    json_build_object(
                        'type', 'FeatureCollection',
                        'features', json_agg(
                            json_build_object(
                                'type', 'Feature',
                                'geometry', ST_AsGeoJSON(ST_Transform(ST_SetSRID(shape, 26915), 4326))::json,
                                'properties', json_build_object(
                                    'objectid', objectid,
                                    'elevation', elevation,
                                    'rastervalu', rastervalu,
                                    'diff_value', diff_value
                                )
                            )
                        ),
                        'crs', 
                        json_build_object(
                            'type', 'name',
                            'properties', 
                            json_build_object(
                                'name', 'EPSG:4326'
                            )
                        )
                    ) AS geojson
                FROM elevation_accuracy;
                """)
    rows = cur.fetchone()[0]

    # Close cursor and connection
    cur.close()
    conn.close()

    # Return the GeoJSON
    return rows



# Route to retrieve polygon as GeoJSON
@app.route('/temperature_interpolation')
def temperature_universalkriging_point():
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
    cur.execute("""SELECT 
                    json_build_object(
                        'type', 'FeatureCollection',
                        'features', json_agg(
                            json_build_object(
                                'type', 'Feature',
                                'geometry', ST_AsGeoJSON(ST_SetSRID(shape, 4326))::json,
                                'properties', json_build_object(
                                    'objectid', objectid,
                                    'pointid', pointid,
                                    'grid_code', grid_code
                                )
                            )
                        ),
                        'crs', 
                        json_build_object(
                            'type', 'name',
                            'properties', 
                            json_build_object(
                                'name', 'EPSG:4326'
                            )
                        )
                    ) AS geojson
                FROM temperature_universalkriging_point;
                """)
    rows = cur.fetchone()[0]

    # Close cursor and connection
    cur.close()
    conn.close()

    # Return the GeoJSON
    return rows


# Route to retrieve polygon as GeoJSON
@app.route('/temperature_accuracy')
def temperature_accuracy():
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
    cur.execute("""SELECT 
                    json_build_object(
                        'type', 'FeatureCollection',
                        'features', json_agg(
                            json_build_object(
                                'type', 'Feature',
                                'geometry', ST_AsGeoJSON(ST_SetSRID(shape, 4326))::json,
                                'properties', json_build_object(
                                    'objectid', objectid,
                                    'tmax', tmax,
                                    'rastervalu', rastervalu,
                                    'diff_value', diff_value
                                )
                            )
                        ),
                        'crs', 
                        json_build_object(
                            'type', 'name',
                            'properties', 
                            json_build_object(
                                'name', 'EPSG:4326'
                            )
                        )
                    ) AS geojson
                FROM temperature_accuracy;
                """)
    rows = cur.fetchone()[0]

    # Close cursor and connection
    cur.close()
    conn.close()

    # Return the GeoJSON
    return rows
    
# Route to retrieve polygon as GeoJSON
@app.route('/delta_cost_map')
def delta_cost_map():
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
    cur.execute("""SELECT 
                    json_build_object(
                        'type', 'FeatureCollection',
                        'features', json_agg(
                            json_build_object(
                                'type', 'Feature',
                                'geometry', ST_AsGeoJSON(ST_Transform(ST_SetSRID(geom, 26915), 4326))::json,
                                'properties', json_build_object(
                                    'delta_cost', delta_cost
                                )
                            )
                        ),
                        'crs', 
                        json_build_object(
                            'type', 'name',
                            'properties', 
                            json_build_object(
                                'name', 'EPSG:4326'
                            )
                        )
                    ) AS geojson
                FROM delta_cost_map;
                """)
    rows = cur.fetchone()[0]

    # Close cursor and connection
    cur.close()
    conn.close()

    # Return the GeoJSON
    return rows


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
