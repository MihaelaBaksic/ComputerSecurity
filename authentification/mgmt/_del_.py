import db_manip


def delete(username: str):
    try:
        data = db_manip.get_records()
        del data[username]
        db_manip.store_records(data)
        print("Record for username {} successfully removed".format(username))
    except KeyError:
        print("Username {} doesn't exists in the database.".format(username))

