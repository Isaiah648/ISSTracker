import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
file = open("iss.txt", "w")
file.write("There are currently " + str(result["number"]) + " astronauts on the ISS: \n\n")
people = result["people"]

# print people on ISS
for person in people:
    file.write(person['name'] + " - on board" + "\n")

# print longitude and latitude
location = geocoder.ip('me')
file.write("\n The current lat/long is: " + str(location.latlng))
file.close()
webbrowser.open("iss.txt")

# setup the world map
screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)

# load map image
screen.bgpic("world.gif")
screen.register_shape("newsat.gif")
iss = turtle.Turtle()
iss.shape("newsat.gif")
iss.setheading(45)
iss.penup()

pen = turtle.Turtle()
pen.pensize(3)
pen.pencolor("red")
pen.penup()

while True:
    # load updated iss location
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    # extract location
    location = result["iss_position"]
    lat = location["latitude"]
    long = location["longitude"]

    # output
    lat = float(lat)
    long = float(long)
    print("Latitude: " + str(lat))
    print("Longitude: " + str(long))

    # update location and refresh
    iss.goto(long, lat)
    pen.setposition(float(long), float(lat))
    pen.pd()
    time.sleep(5)