#!/usr/bin/python3
"""tracking the iss using
   api.open-notify.org/astros.json | Alta3 Research"""

# notice we no longer need to import urllib.request or json
import requests

## Define URL
MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
    """runtime code"""

    ## Call the webservice
    groundctrl = requests.get(MAJORTOM)
    
    # Convert into dictionary
    #astronauts = groundctrl.json()

    for x in groundctrl.json()['people']:
        print(f"{x['name']} is on the {x['craft']}")

if __name__ == "__main__":
    main()

