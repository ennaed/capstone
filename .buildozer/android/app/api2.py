import urllib2
import json

# to use this in another file, place this code in the same folder, then do:
# import api
# api.get_log()

# returns a list of dicts of the entries from the database
def fetch(endpoint):
    response = urllib2.urlopen('http://wheresmybasura.herokuapp.com/' + endpoint).read()
    data = json.loads(response)
    return data

if __name__ == '__main__':
    #print get_log()
    for i in fetch('/trucks'):
    	print i['plate_number']