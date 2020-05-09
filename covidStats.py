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
values = []
stats = []

def statedata(name):

    # print('Tamil nadu:', info["Tamil Nadu"]["districtData"])
    # print(len(info[name]["districtData"]))
    # chosen = ['Visakhapatnam', 'Bengaluru Urban',] -- if any specific district data needed, uncomment this anf the code in the for loop
    active = confirmed = deceased = recovered = 0

    print ('Stats of ', name)

    for x in info[name]['districtData']:
        # if x in chosen:
            # print (x)
            active += int(info[name]['districtData'][x]['active'])
            confirmed += int(info[name]['districtData'][x]['confirmed'])
            deceased += int(info[name]['districtData'][x]['deceased'])
            recovered += int(info[name]['districtData'][x]['recovered'])

    print(active)
    print(confirmed)
    print(deceased)
    print(recovered)
    print()
    stats = [active, confirmed, deceased, recovered]
    # values[name] = [active, confirmed, deceased, recovered]
    # values = [active, confirmed, deceased, recovered]
    values.append(stats)
    # index += 1


statedata("Tamil Nadu")
statedata("Kerala")
statedata("Karnataka")
statedata("Telangana")
statedata('Andhra Pradesh')
print(values)

with open('covidTable.csv',mode='w') as database:
        fieldnames = ['Tamil Nadu', 'Kerala', 'Karnataka', 'Telangana', 'Andhra Pradesh'] 
        writer = csv.DictWriter(database, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({
                        'Tamil Nadu':values[0],
                        'Kerala':values[1],
                        'Karnataka':values[2],
                        'Telangana':values[3],
                        'Andhra Pradesh':values[4]
                     })
        print('Table Created!')
