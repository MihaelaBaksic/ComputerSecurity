import json


def get_records():
    f = open('../pass_db.txt', 'r+')
    data = json.loads(f.read())
    f.close()
    return data


def store_records(records):
    f = open('../pass_db.txt', 'w+')
    data = json.dumps(records)
    f.write(data)
    f.close()


def rm_record(username: str):
    return 0
