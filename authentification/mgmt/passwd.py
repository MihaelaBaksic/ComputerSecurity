import db_manip


def passwd(username: str):
    data = db_manip.get_records()

    try:
        data[username][1:] = ('new_salt', 'new_hashed_pass')
        db_manip.store_records(data)
        print("Password for username {} successfully updated.".format(username))
    except KeyError:
        print("Username {} doesn't exists in the database. If you wish to add it use action add.".format(username))

