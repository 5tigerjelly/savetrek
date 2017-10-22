import json
import sys
import time
from firebase import firebase
firebase = firebase.FirebaseApplication('https://savetrek.firebaseio.com/', None)

data = {
    "name": "Mexican Red Cross",
    "townName": "Mexico City",
    "lat" : 19.4326077,
    "lng" : -99.133207997,
    "resource": {
        "water": 0,
        "food": 20000,
        "shelter": 5000,
        "volenteer": 250,
        "flashlight": 2500,
        "firstAid": 10000
    },
    "description": "Supplies provided by Mexican Red Cross. Contact us for help.",
    "comments" : []
}


firebase.put('supplier/' , data)

# firebase.patch('demander/' , {"test":data})