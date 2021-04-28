import db_manip


def forcepass(username: str):

    data = db_manip.get_records()

    try:
        data[username][0] = False
        db_manip.store_records(data)
        print("Password for username {} successfully invalidated.\n The user will need to update it on the next login".format(username))
    except KeyError:
        print("Username {} doesn't exists in the database.".format(username))


