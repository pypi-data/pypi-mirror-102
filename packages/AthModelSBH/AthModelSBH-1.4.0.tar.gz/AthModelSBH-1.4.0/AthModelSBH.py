import json
import sqlite3

def get_ath_name():
    connection = sqlite3.connect('coachdata.sqlite')
    cursor = connection.cursor()

    names = cursor.execute("SELECT name FROM athletes")
    names_list = [row[0] for row in names.fetchall()]
    names_json = json.dump(names_list)

    connection.close()

    return(names_json)


