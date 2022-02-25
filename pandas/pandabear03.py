#!/usr/bin/env python3

import pandas as pd

def main ():

    df = pd.read_json("5movies.json")

    df.to_excel("5moves-translated-from-json.xlsx")

if __name__ == "__main__":

    main()
