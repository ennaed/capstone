import urllib2
import ast

def get_dumpsite(url = 'http://wheresmybasura.herokuapp.com/dumpsites'):
    response = urllib2.urlopen(url).read()
    parsed_data = ast.literal_eval(response)
    return parsed_data

if __name__ == '__main__':
    print get_dumpsite()
