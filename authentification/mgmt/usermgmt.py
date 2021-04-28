from mgmt_args import args
from add import add
from passwd import passwd
from _del_ import delete
from forcepass import forcepass


if __name__ == '__main__':
    if args.action == 'add':
        add(args.username)
    elif args.action == 'passwd':
        passwd(args.username)
    elif args.action == 'del':
        delete(args.username)
    elif args.action == 'forcepass':
        forcepass(args.username)
    else:
        print("Invalid action for user manager. Valid actions are: add, passwd and del.")
