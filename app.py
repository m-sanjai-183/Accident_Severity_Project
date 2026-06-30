from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="#sanjai8248",
    database="accident_prediction"
)

cursor = db.cursor()

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Prediction Page
@app.route('/predict', methods=['POST'])
def predict():

    speed = int(request.form['speed'])
    weather = request.form['weather']
    road_condition = request.form['road_condition']
    vehicles = int(request.form['vehicles'])

    # Prediction Logic
    if speed > 80 or (weather == "Rain" and road_condition == "Wet"):
        prediction = "Fatal"
    elif speed > 50:
        prediction = "Serious"
    else:
        prediction = "Minor"

    # Save Prediction to MySQL
    sql = """
    INSERT INTO accident_records
    (speed, weather, road_condition, vehicles, severity)
    VALUES (%s, %s, %s, %s, %s)
    """

    values = (
        speed,
        weather,
        road_condition,
        vehicles,
        prediction
    )

    cursor.execute(sql, values)
    db.commit()

    return render_template(
        'index.html',
        prediction_text=prediction
    )

# History Page
@app.route('/history')
def history():

    cursor.execute("SELECT * FROM accident_records")
    records = cursor.fetchall()

    return render_template(
        'history.html',
        records=records
    )

# Dashboard Page
@app.route('/dashboard')
def dashboard():

    cursor.execute("SELECT COUNT(*) FROM accident_records")
    total = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM accident_records WHERE severity='Fatal'"
    )
    fatal = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM accident_records WHERE severity='Serious'"
    )
    serious = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM accident_records WHERE severity='Minor'"
    )
    minor = cursor.fetchone()[0]

    return render_template(
        'dashboard.html',
        total=total,
        fatal=fatal,
        serious=serious,
        minor=minor
    )

if __name__ == '__main__':
    app.run(debug=True)