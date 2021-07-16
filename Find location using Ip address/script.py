import requests
import folium

res = requests.get("https://ipinfo.io/")
data = res.json()

print("ip address : "+data["ip"])

location = data["loc"].split(",")
log= float(location[1])
lat= float(location[0])

fg = folium.FeatureGroup("my app")

# To show location in India's states
# f = open("india_states.json", "r",encoding="utf-8-sig").read()
# fg.add_child(folium.GeoJson(data=f))

popupText = data["postal"] + ", " + data["city"] + ", " + data["region"]

fg.add_child(folium.Marker(location=[lat,log], popup=popupText))

map = folium.Map(location=[lat,log], zoom_start=7)
map.add_child(fg)
map.save("yourLocation.html")