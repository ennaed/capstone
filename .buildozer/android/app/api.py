import urllib2
import ast

# to use this in another file, place this code in the same folder, then do:
# import api
# api.get_log()

# returns a list of dicts of the entries from the database
def get_log(url = 'http://wheresmybasura.herokuapp.com/trucks'):
    response = urllib2.urlopen(url).read()
    parsed_data = ast.literal_eval(response)
    return parsed_data

def get_dumpsite(url = 'http://wheresmybasura.herokuapp.com/view_dumpsites'):
    response = urllib2.urlopen(url).read()
    parsed_data = ast.literal_eval(response)
    return parsed_data

def get_message(url = 'http://wheresmybasura.herokuapp.com/view_messages'):
    response = urllib2.urlopen(url).read()
    parsed_data = ast.literal_eval(response)
    return parsed_data

if __name__ == '__main__':
    print get_log()