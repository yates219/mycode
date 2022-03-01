#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
import time 

URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()
    timestamp = resp['timestamp']
    realtime = time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime(timestamp))
    location = resp['iss_position']

    print("CURRENT LOCATION OF THE ISS:")
    print(f"Timestamp: {realtime}")
    print(f"Lon: {location['longitude']}")
    print(f"Lat: {location['latitude']}")
    

if __name__ == "__main__":
    main()
