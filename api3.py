import urllib2
import ast

def get_message(url = 'http://wheresmybasura.herokuapp.com/messages'):
    response = urllib2.urlopen(url).read()
    parsed_data = ast.literal_eval(response)
    return parsed_data

if __name__ == '__main__':
    print get_message()