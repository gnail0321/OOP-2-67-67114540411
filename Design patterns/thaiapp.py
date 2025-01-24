from thai import Thaicitizen
import requests

url = "https://dummyjson.com/user"
data = requests.get(url).json()
#print(data['users'][0])
#for i in range(30):
  #print(data['users'][i]['firstName'])
users = data['users']
thai=[]
for user in users:
  u = Thaicitizen(
      first_name=user['firstName'],
      last_name=user['lastName'],
      image=user['image'],
      country=user['address']['country']
  )
  thai.append(u)
for t in thai:

    print(t.first_Name)
    print(t.last_Name)
    print(t.image)
    print(t.country)
