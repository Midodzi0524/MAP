import folium 
import pandas as pd

## create a map
map = folium.Map(location=[35, -89], zoom_start= 6)

data = pd.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data['LON'])
elev = list(data['ELEV'])

def color_producer(elevation):
    if elevation < 1000:
     return 'green'
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"
fgv = folium.FeatureGroup(name="Volcanoes")

for lt,ln,el in zip(lat,lon,elev): 
    fgv.add_child(folium.CircleMarker(location=[lt,ln],radius = 8, popup=str(el) + 'm', 
    fill_color=color_producer(el), color='grey', fill_opacity = 0.8))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open("world.json", 'r', encoding='utf-8-sig').read(), 
style_function = lambda x: {'fillcolor':'blue' if x['properties']['POP2005'] < 1000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")

