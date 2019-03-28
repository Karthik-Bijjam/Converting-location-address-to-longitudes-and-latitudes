# -*- coding: utf-8 -*-

import pandas as pd
import pickle
from geopy.geocoders import GoogleV3
geolocator = GoogleV3(api_key='Google API Key')


with open('geolocations.pkl', 'rb') as f:
    data = pickle.load(f)
    print(data)

    users_with_countries = {
        "data": []
    }
    tweets = 0
    

    
    for itemdata in data['data']:
        print (itemdata['features']['location'])
        tweets = tweets + 1
        try:
            location = itemdata['features']['location']
            
            if location != None:  
                location = geolocator.geocode(location)
                print((location.latitude, location.longitude))
                print(tweets)
                user_data = {
                    "user_id" : tweets,
                    "features" : {
                        "latitude" : location.latitude,
                        "longitude": location.longitude, 
                    }
                }
                users_with_countries['data'].append(user_data)
                tweets +=1
            else:
                print ("NO Location!", location)
        except:
                pass
            
with open('geo_location_details.pkl', 'wb') as f:
    pickle.dump(users_with_countries,f,protocol=pickle.HIGHEST_PROTOCOL) 
 
                