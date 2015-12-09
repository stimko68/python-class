"""
Sample program that ties together all of the concepts in the lesson.

Designed to take user input on the command line and save it to the
database. Can also be used to query the database.
"""
import atexit
import mysql.connector as mysql

# Exceptions to catch from mysql
from mysql.connector import InterfaceError

### Custom Exception classes
class MissingParameterError(Exception):
    pass

class StarWarsCharacterManager(object):
    """
    Object to perform all of the heavy lifting
    """
    def __init__(self):
        # Create the connection to the database
        self.db = mysql.connect(user='root', password='', host='localhost', database='star_wars')

        # Setup the DB cursor for running queries
        self.cursor = self.db.cursor(dictionary=True)

    def _run_query(self, sql):
        """
        Helper method to run SQL queries and return the data

        :param sql: SQL to be run against the database
        :return:    Response from the database
        """
        self.cursor.execute(sql)
        try:
            return self.cursor.fetchall()
        except InterfaceError:
            return None

    def get_pk(self, table_name, **query_params):
        """
        Query the given table using the given query parameters and return
        the primary key of the entry, if found.

        :param table_name:      Table to query
        :param query_params:    Query parameters to use
        :return:                Int pk, or None if not found
        """
        # Define the base query string
        query_sql = "SELECT id FROM {0} WHERE ".format(table_name)

        # Check to make sure that query parameters were provided
        if len(query_params) == 0:
            raise MissingParameterError('Query parameters are required!')

        # Use a list comprehension and a join to convert the dictionary object into
        # a string of key value pairs to use in the SQL query
        # NOTE: the way this code is written it only works for string values
        q_params = ' AND '.join(["{}='{}'".format(key, value) for (key, value) in query_params.items()])

        # Concatenate the query parameters to the base query string and terminate
        # with a semicolon
        query_sql += q_params + ';'

        # Get the result
        result = self._run_query(query_sql)

        # Check that results were returned
        if len(result) == 0:
            return None

        return int(result[0]['id'])

    def find_character(self, name):
        """
        Check to see if the given character exists in the DB

        :param name:    Character's name (e.g., Darth Vader)
        :return:        Boolean
        """
        find_sql = "SELECT * FROM player WHERE name = '{}';".format(name)
        result = self._run_query(find_sql)

        if len(result) == 0:
            return False
        else:
            return True

    def add_new_character(self, name, race, ship=None):
        """
        Adds a new character to the DB. If a ship name is provided, also
        adds that character to the ship's crew.

        :param name:    Character's name (e.g., Luke Skywalker)
        :param race:    The character's race (e.g., Human)
        :param ship:    Name of the ship to add the character to
        :return:        Boolean
        """
        # Get the PK of the provided race
        race_pk = self.get_pk('race', **{'race_name': race})

        # Setup the SQL query
        add_character_sql = "INSERT INTO player SET name='{0}', race_fk={1};".format(name, race_pk)

        # Execute the query
        self._run_query(add_character_sql)

        # Add the new character to the ship's crew, if a ship name is given
        if ship is not None:
            # Get the PK of the new row we just inserted
            new_character_pk = self.cursor.lastrowid

            # Get the PK of the given ship
            ship_pk = self.get_pk('ship', **{'name': ship})

            # Create a new entry in the ship_crew table
            new_ship_crew_sql = "INSERT INTO ship_crew SET ship_fk = {0}, player_fk = {1};".format(ship_pk, new_character_pk)
            self._run_query(new_ship_crew_sql)

        return True

if __name__ == '__main__':
    # Instantiate the manager object
    swdb_mgr = StarWarsCharacterManager()

    print 'Welcome to the Star Wars Character Manager!'
    print '+------------------------------------------+'
    character_name = raw_input('Enter a character name: ')

    # Check to see if the character exists
    character_exists = swdb_mgr.find_character(character_name)

    if character_exists:
        while True:
            show_character_data = raw_input('Character found in the database! '
                                            'Would you like to see the character data? ')
            if show_character_data.lower() not in ('y', 'n'):
                show_character_data = raw_input('Invalid response! Please answer y or n: ')