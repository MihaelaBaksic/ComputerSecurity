import sys
sys.path.append('../')
import db_manip


# Forcing user to change password after next login
def forcepass(username: str):

    data = db_manip.get_records()

    try:
        # Set valid flag to false for given username
        data[username][0] = False
        db_manip.store_records(data)
        print("Password for username {} successfully invalidated.\nThe user will need to update it on the next login".format(username))
    except KeyError:
        print("Username {} doesn't exists in the database.".format(username))


