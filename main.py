
import argparse
import actions




def init_args():
    arg_parser = argparse.ArgumentParser(prog="PyDataBridge",
                                     description="programm that help you to conenct to your number of databases and intract with them.")
    arg_parser.add_argument('--action', '-a', help='action to perform')
    arg_parser.add_argument('--table' , '-t', '--source', help='target source table')
    return arg_parser.parse_args()




if __name__ == "__main__":
    args = init_args()
    table = args.table
    action = args.action
    if(action == 'select-all'):
        migrated = actions.migrate(source=table, destinatin=table)
        print(migrated)


