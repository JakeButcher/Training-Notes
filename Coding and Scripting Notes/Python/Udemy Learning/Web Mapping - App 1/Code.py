
import folium
import pandas

#Creating Map (Saved as HTML)
map = folium.Map(location=[38.386295, -118.402061], zoom_start=5, tiles="OpenStreetMap")

#Creating the Volcanoes Feature Group ,Reading CSV with Coordiantes and creating a Color Function
fgv = folium.FeatureGroup(name="Volcanoes")
df = pandas.read_csv("Volcanoes.txt")
lat = list(df["LAT"])
lon = list(df["LON"])
elev = list(df["ELEV"])
def colour_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 2000:
        return "orange"
    elif 2000 <= elevation < 3000:
        return "red"
    else:
        return "purple"

#Adding Markers for Volcanoes
for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.Marker(location=[lt, ln], popup=el, icon=folium.Icon(color=colour_producer(el))))

#Adding Country Population Regions using JSON, in a different Feature Group
fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open("world.json", encoding='utf-8-sig').read(), 
             style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
                                       else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

#Add FeatureGroup to the Map
map.add_child(fgv)
map.add_child(fgp)
#Adding Layer Toggles (Has to be after Feature Group)
map.add_child(folium.LayerControl())
#Saving Map
map.save("Map1.html")
