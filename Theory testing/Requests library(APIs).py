#-------------------------------------NOTE-------------------------------------------------------------------------------------------------------------------------------------------------
#API s are web based services that you can use in your code. ex:apple have API called itunes which give your code access to songs and other stuff (this is my explanation)
#   ----what is Jason----
    #JSON is an open standard file format and data interchange format that uses human-readable text to store and transmit data objects consisting of attribute–value pairs and arrays.
    #It is a common data format with diverse uses in electronic data interchange, including that of web applications with servers.
    # .json() - Returns the json-encoded content of a response, if any
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#this program asks for a artist name and will access itunes and get you a list of songs he or she sing
import requests #request results(response) from the internet like a browser #you need to install this module using pip
import json #this module comes with python

while True:
    artist = input("Name of the artist: ")
    if len(artist)>1:
        break
                                                                    #you can limit how many results 
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + artist)
                                                                     #result limit    #name of the artist
# print(json.dumps(response.json(),indent =2))  #Testing     #This will show the response of the request in json format #indent makes this prints json file more readable manner by indenting

o = response.json() # '.json()' Returns the json-encoded content and we assign it to a variable called o for ease of use
for result in o["results"]:
    print(result["trackName"])