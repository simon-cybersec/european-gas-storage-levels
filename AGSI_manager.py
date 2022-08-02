import requests
import os
import json
from dotenv import load_dotenv
from utils import gaslevel_bar


def getGasLevels():

    # The AGSI API key is deposited in the .env file. Never hard code an API key and never include it as source code.
    # Always make sure you don't upload an API key into a public repository! I.e. write '.env' into your .gitignore-file.
    load_dotenv()

    # API URL
    api_url = 'https://agsi.gie.eu/api'

    # Countries to be read
    countries = ["AT", "BE", "BG", "CZ", "DE", "DK", "ES", "FR", "HR", "HU", "IE", "IT", "LV", "NL", "PL", "PT", "RO", "SE", "SK", "UA"]
    
    print()
    print("+-----------------------------------------------------------------------+")
    print("|                      European Gas Storage Levels                      |")
    print("+-----------------------------------------------------------------------+")

    # Get the data for each country
    for i in range(len(countries)):

        parameters = {
            "country": countries[i],
            "size": 1
        }

        header = {
            "x-key" : os.environ.get("API_KEY")
        }

        # Get AGSI data
        agsi_data = requests.get(url=api_url, params=parameters, headers=header).json()

        # At the first request extract the date of the readings
        if i == 0:
            print("last available readings: ", end="")
            if not agsi_data['gas_day']:
                print("?", end="")
            else:
                print(agsi_data['gas_day'], end="")
            
            print("\t\t (see also agsi.gie.eu)\n")
            print("Country:")

        # Check for bad API response
        if not agsi_data['data']:
            print(f"   - {countries[i]}: Error in API response. Wrong API key or more than 60 req/hr?\n")
            # Write data into an error.json file
            with open("outputs/error.json", 'a') as out:
                out.write(json.dumps(agsi_data, indent = 4, sort_keys=False) + '\n')
            continue

        else:
            # If you want to output all data into a .json file
            # with open("outputs/agsi_data.json", 'a') as out:
            #    out.write(json.dumps(agsi_data, indent = 4, sort_keys=True) + '\n')

            # Extract and output the gas level
            try:
                gas_level = float(agsi_data['data'][0]['full'])
                print(f"   - {countries[i]}: ", end="")
                gaslevel_bar(gas_level)
            except:
                print(f"   - {countries[i]}: no data")

            print()

    print()
    print()
