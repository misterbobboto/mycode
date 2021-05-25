#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        pprint.pprint(got_dj)

        houseURL = got_dj["allegiances"]
        
        print("Houses: ")
        for house in houseURL:
            houseResp = requests.get(house)
            house_dj = houseResp.json()
            pprint.pprint(house_dj["name"])


        booksURL = got_dj["books"]

        print("Books: ")
        for book in booksURL:
            bookResp = requests.get(book)
            book_dj = bookResp.json()
            pprint.pprint(book_dj["name"])

if __name__ == "__main__":
        main()

