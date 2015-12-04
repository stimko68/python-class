"""
Database connection and query examples using the mysql-connector-python library
provided by Oracle
"""

##############################################################################################
# - Setup ---------------------------------------------------------------------------------- #
##############################################################################################
# Import the MySQL Connector library
import mysql.connector as mysql

# Setup the database connection
db = mysql.connect(user='root', password='', host='localhost', database='star_wars')
db.close()

# Example database connection using a dictionary as the configuration
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'star_wars'
}
db = mysql.connect(**config)

##############################################################################################
# - Querying data -------------------------------------------------------------------------- #
##############################################################################################
# Setup a simple cursor object
# This will return a list of tuples
cursor = db.cursor()

# Execute a simple SELECT query
select_sql = 'SELECT * FROM player;'
cursor.execute(select_sql)

# Get the results
print cursor.fetchall()

# Setup a cursor object that returns the result as a list of dictionaries
# NOTE: This requires mysql-connector-python v2.0+
cursor = db.cursor(dictionary=True)

# Rerun the above query
cursor.execute(select_sql)
print cursor.fetchall()

# Query with joins
select_join_sql = "SELECT ship.name AS ship_name, " \
                  "player.name AS player " \
                  "FROM ship_crew " \
                  "INNER JOIN ship ON ship_crew.ship_fk = ship.id " \
                  "INNER JOIN player ON ship_crew.player_fk = player.id;"
cursor.execute(select_join_sql)
print cursor.fetchall()

##############################################################################################
# - Inserting new data --------------------------------------------------------------------- #
##############################################################################################
# Add a new player
# Setup the SQL query string
new_player_sql = "INSERT INTO player SET name = '{name}', race_fk = {race_fk};"

# Find the PK for the 'Human' race type
human_race_sql = "SELECT id FROM race WHERE race_name = 'Human';"
cursor.execute(human_race_sql)
race_fk = cursor.fetchone()['id']

# Insert the new player into the player table
cursor.execute(new_player_sql.format(name='Luke Skywalker', race_fk=race_fk))

# Get the PK of the row we just inserted
print cursor.getlastrowid()