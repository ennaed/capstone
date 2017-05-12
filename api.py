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
    dumpsite_data = get_dumpsites()
    trucks_data = get_trucks()
    messages_data = get_messages()

    dumpsites = dict()
    trucks = dict()
    messages = list()

    for i in dumpsite_data:
        dumpsites[int(i['id'])] = {'lat': i['lat'], 'lon': i['lon'], 'legal': i['legal']}

    for i in trucks_data:
        trucks[int(i['id'])] = {'plate_number': i['plate_number']}

    for i in messages_data:
        dumpsite_id = int(i['dumpsite_id'])
        truck_id = int(i['truck_id'])

        date = compress_timestring(i['date_created'])
        date, time = date.split()
        lat = dumpsites[dumpsite_id]['lat']
        lon = dumpsites[dumpsite_id]['lon']

        if dumpsites[dumpsite_id]['legal']:
            status = 'LEGAL'
        else:
            status = 'ILLEGAL'

        plate_number = trucks[truck_id]['plate_number']

        messages.append({'lat': lat, 'lon': lon, 'status': status, 'plate_number': plate_number, 'date': date, 'time': time})

    return messages



if __name__ == '__main__':

    #print type(d)
    # for i in get_processed_data():
    #      print i['plate_number'], i['time']

    print get_processed_data()