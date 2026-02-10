# Note that if you want to have stylized text (bold, different fonts, etc) in the popup window you can use HTML. Here's an example:

1. import folium
2. import pandas
3.  
4. data = pandas.read_csv("Volcanoes.txt")
5. lat = list(data["LAT"])
6. lon = list(data["LON"])
7. elev = list(data["ELEV"])
8.  
9. html = """<h4>Volcano information:</h4>
10. Height: %s m
11. """
12.  
13. map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Mapbox Bright")
14. fg = folium.FeatureGroup(name = "My Map")
15.  
16. for lt, ln, el in zip(lat, lon, elev):
17.     iframe = folium.IFrame(html=html % str(el), width=200, height=100)
18.     fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = "green")))
19.  
20.  
21. map.add_child(fg)
22. map.save("Map_html_popup_simple.html")




# You can even put links in the popup window. For example, the code below will produce a popup window with the name of the volcano as a link which does a Google search for that particular volcano when clicked:

1. import folium
2. import pandas
3.  
4. data = pandas.read_csv("Volcanoes.txt")
5. lat = list(data["LAT"])
6. lon = list(data["LON"])
7. elev = list(data["ELEV"])
8. name = list(data["NAME"])
9.  
10. html = """
11. Volcano name:<br>
12. <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
13. Height: %s m
14. """
15.  
16. map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Mapbox Bright")
17. fg = folium.FeatureGroup(name = "My Map")
18.  
19. for lt, ln, el, name in zip(lat, lon, elev, name):
20.     iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
21.     fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = "green")))
22.  
23. map.add_child(fg)
24. map.save("Map_html_popup_advanced.html")


