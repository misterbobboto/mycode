#!/usr/bin/python3

import requests

NASAAPI = "https://api.nasa.gov/mars-photos/api/v1/"

# this function grabs our credentials
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    roverslist = ['curiosity', 'opportunity', 'spirit']

    print("Rovers List: \n")
    for rover in roverslist:
        print(rover)

    roverPick = '';

   # while roverPick not in roverslist
    roverPick = input("Select rover from list: ")
    baseURL = 'https://api.nasa.gov/mars-photos/api/v1/rovers/'
    cameraURL = baseURL + roverPick + '?' + nasacreds

    cameras = requests.get(cameraURL).json()['rover']['cameras']

    print("\nCamera List: \n")
    for camera in cameras:
        print(camera['name'])

    cameraPick = input("Select camera from list: ")
    ## make a call to NASAAPI

    finalURL = baseURL + roverPick + "/" + '/photos?camera=' + cameraPick + '&' + nasacreds

    pics = requests.get(finalURL).json()

    print(pics)

if __name__ == "__main__":
    main()

