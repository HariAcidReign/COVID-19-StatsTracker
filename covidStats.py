import requests
import json
import csv

url = 'https://api.covid19india.org/state_district_wise.json'

payload = {}
headers = {}

response = requests.request('GET', url, headers=headers, data=payload)

data = response.text.encode('utf8')
info = json.loads(data)

# index = 0

def statedata(name):

    stats = {}

    # print('Tamil nadu:', info["Tamil Nadu"]["districtData"])
    # print(len(info[name]["districtData"]))
    # chosen = ['Visakhapatnam', 'Bengaluru Urban',] -- if any specific district data needed, uncomment this anf the code in the for loop
    active = confirmed = deceased = recovered = 0



    for x in info[name]['districtData']:
        # if x in chosen:
            # print (x)
            active += int(info[name]['districtData'][x]['active'])
            confirmed += int(info[name]['districtData'][x]['confirmed'])
            deceased += int(info[name]['districtData'][x]['deceased'])
            recovered += int(info[name]['districtData'][x]['recovered'])


    stats['state'] = name
    stats['active'] = active
    stats['confirmed'] = confirmed
    stats['deceased'] = deceased
    stats['recovered']= recovered
    # values[name] = [active, confirmed, deceased, recovered]
    # values = [active, confirmed, deceased, recovered]

    # index += 1
    return stats



def totdata():
        values = []
        values.append(statedata("Tamil Nadu"))
        values.append(statedata("Kerala"))
        values.append(statedata("Karnataka"))
        values.append(statedata("Telangana"))
        values.append(statedata('Andhra Pradesh'))
        return values

print(totdata())
