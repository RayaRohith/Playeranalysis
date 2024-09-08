from datetime import datetime

from bson import ObjectId
from flask import Flask, render_template, request, redirect, url_for, jsonify, flash, session
from pymongo import MongoClient
from bson.json_util import dumps
import secrets
import json
from werkzeug.security import check_password_hash, generate_password_hash



app = Flask(__name__)
secret_key = secrets.token_urlsafe(16)
app.config['SECRET_KEY'] = secret_key
#
 #Setup MongoDB client
client = MongoClient("mongodb://localhost:27017/")
db = client["playershealth"]  # Use your database name
#the record of the team member and their position in their team
players = db["team_members"]  # collection name for detailed team members
user = db["users"] # collection name to store user info
# collections that store each players health measurements
players_health = db["health_data"]



@app.route('/')
def home():  # put application's code here
    return render_template("login.html")

#routes for the player analysis buttom on the player/manager dashboard
@app.route('/player_analysis', methods=['GET'])
def player_analysis():
    all_player = players.find()
    player_list = list(all_player)
    return render_template('player_analysis.html', player_list=player_list)

@app.route("/players_details/<name>", methods=['GET'])
def player_data(name):
    #print(name)
    playerdata = None
    health_data = players_health.find_one({"name": name})
    #print(health_data['heart_rate'])
    if health_data:
        return render_template("players_details.html", player=health_data)
    else:
        return render_template("home.html")


#route for log in page, also the feature of creating new account in MongoDB
@app.route('/log_in', methods=['GET', 'POST'])
def log_in():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Assuming there's a 'users' collection in your MongoDB
        user = db.users.find_one({'username': username})

        if user and check_password_hash(user['password'], password):
            # Successfully authenticated
            # Here, you would manage sessions and perhaps set the user role in the session
            return redirect(url_for('home_page'))
        else:
            flash('Invalid username, password, or role')
            return redirect(url_for('log_in'))

    # Render the login form for GET requests
    return render_template('home.html')

# route for log out
@app.route('/logout')
def logout():
    return render_template('login.html')


@app.route('/home', methods=['GET','POST'])
def home_page():
    return render_template('home.html')






# route that should be used when click the bottom for a players detail
# route return a json massage with headers(headers represent different measurements)
@app.route('/single_player_details', methods=['GET', 'POST'])
def display_single_players():
    if request.method == 'POST':
        search_term = request.form.get('name')
        document = players_health.find_one({'name':search_term})

        if document:
            return dumps(document)
        else:
            return jsonify({"error": "Document not found"}), 404



# route that allow user to input their measurements, data are stored in the
# player_health_record collection in MongoDB
@app.route('/add_health_record', methods=['GET', 'POST'])
def add_health_record():
    if request.method == 'POST':
        # Extract the form data
        health_data = {
            'player_id': ObjectId(request.form.get('player_id')),
            'heart_rate': int(request.form.get('heart_rate')),
            'heart_rate_variability': int(request.form.get('heart_rate_variability')),
            'steps_taken': int(request.form.get('steps_taken')),
            'distance_covered': float(request.form.get('distance_covered')),
            'calories_burned': int(request.form.get('calories_burned')),
            'calories_consumed': int(request.form.get('calories_consumed')),
            'training_intensity': request.form.get('training_intensity'),
            'sleep_duration': int(request.form.get('sleep_duration')),
            'rem_sleep': request.form.get('rem_sleep'),
            'deep_sleep': request.form.get('deep_sleep'),
            'resting_heart_rate': int(request.form.get('resting_heart_rate')),
            'blood_oxygen_level': int(request.form.get('blood_oxygen_level')),
            'estimated_fluid_intake': int(request.form.get('estimated_fluid_intake')),
            'estimated_sweat_loss': int(request.form.get('estimated_sweat_loss')),
            'cycling_power_output': int(request.form.get('cycling_power_output')),
            'running_speed': float(request.form.get('running_speed')),
            'recorded_at': datetime.datetime.now(),  # Current time for the record
            'last_updated': datetime.datetime.now()  # Current time for the update
        }

        # Insert the health record into the 'player_health_record' collection
        result = players_health.insert_one(health_data)

        if result.inserted_id:
            flash('Health record added successfully!')
            return redirect(url_for('home'))  # Redirect to home or any other page
        else:
            flash('An error occurred while adding the health record.')
            return redirect(url_for('add_health_record'))  # Stay on the same page for correction

    # Render the form for GET requests
    return render_template('add_health_record.html')




# return a player's health measurements when given the player's name
@app.route('/get_health_record', methods=['GET', 'POST'])
def get_health_record():
    if request.method == 'POST':
        player_name = request.form.get('player_name')

        # First, find the player_id from the 'team_members' collection using the player's name
        player = db.team_members.find_one({'name': player_name})
        if player:
            # Use the player_id to fetch the health record from 'player_health_record' collection
            health_records = players_health.find({'name': player_name})
            health_records_list = list(health_records)

            # Convert MongoDB Cursor to a list of dictionaries
            health_records_dicts = [record for record in health_records_list]

            # If health records found, return them as JSON
            return jsonify(health_records_dicts)
        else:
            return jsonify({"error": "No player found with that name."}), 404

    # Render the search form for GET requests or if no player name is submitted
    return jsonify({"error": "This endpoint expects a POST request with a player's name."}), 400



#route for team analysis, return all info mation


@app.route('/submission_success')
def submission_success():
    return render_template('submission_success.html')

@app.route('/input_page')
def input_page():
    return render_template("post.html")



# route for registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        name = request.form['name']
        positions = request.form['positions']
        age = request.form['age']
        team = request.form['team']
        games_played = request.form['games_played']
        average_score = request.form['average_score']


        # Check if the username already exists
        user = db.users.find_one({'username': username})
        if user:
            flash('Username already exists')
            return redirect(url_for('register'))

        # Hash the password before storing it
        hashed_password = generate_password_hash(password)

        # Insert new user into the database
        db.users.insert_one({
            'username': username,
            'password': hashed_password,
        })

        db.team_members.insert_one({
            'name' : name,
            'age' : age,
            'positions' : positions,
            'team' : team,
            'games_played': games_played,
            'average_score' : average_score,
            'user_name': username
        })

        flash('Registration successful')
        return redirect(url_for('log_in'))  # Redirect to login page after successful registration

    return render_template('register.html')

# routes for template rendering for support page
@app.route('/support', methods=['Get'])
def support():
    # Check if the role is stored in the session and if it is 'manager'
    return render_template('support.html')



if __name__ == '__main__':
    app.run(debug=True)
