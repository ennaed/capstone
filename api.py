import urllib2
import json

def compress_timestring(s):
    date, time = s.split()
    yy, mm, dd = date.split('-')
    hour, minute = time.split(':')[:2]
    return '{}/{}/{} {}:{}'.format(mm, dd, yy, hour, minute)

def get_messages(website = 'http://wheresmybasura.herokuapp.com/', endpoint = 'messages'):
    response= urllib2.urlopen(website + endpoint).read()
    data = json.loads(response)
    return data

def get_trucks(website = 'http://wheresmybasura.herokuapp.com/', endpoint = 'trucks'):
    response= urllib2.urlopen(website + endpoint).read()
    data = json.loads(response)
    return data

def get_dumpsites(website = 'http://wheresmybasura.herokuapp.com/', endpoint = 'dumpsites'):
    response= urllib2.urlopen(website + endpoint).read()
    data = json.loads(response)
    return data

def get_processed_data():
    messages_data = get_messages()
    messages = list()


    for i in messages_data:
        date = compress_timestring(i['date_created'])
        date, time = date.split()
        name = i['dumpsite_name']
        plate_number = i['plate_number']

        dumpsite = filter(lambda x: x['name'] == name, get_dumpsites())[0]
        if dumpsite['legal']:
            status = 'LEGAL'
        else:
            status = 'ILLEGAL'


        messages.append({'name': name, 'status': status, 'plate_number': plate_number, 'date': date, 'time': time})

    return messages



if __name__ == '__main__':
    d = get_processed_data()
    print type(d)
    for i in d:
        print i, type(i)