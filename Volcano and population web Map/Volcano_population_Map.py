import pandas
import folium

volcano_data = pandas.read_csv('Volcanoes.txt')
lat = list(volcano_data.LAT)
lon = list(volcano_data.LON)
elev = list(volcano_data.ELEV)


def color_producer(elev):
    if elev < 1000:
        return 'green'
    elif 3000 > elev >= 1000:
        return 'orange'
    else:
        return 'red'


html = """<h4>Volcano information:</h4>
Height: %s m
"""

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")
# Adding point markers
for lt, ln, el in zip(lat, lon, elev):
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location=(lt, ln), radius=6, popup=folium.Popup(iframe), fill_color=color_producer(el), color='grey', fill_opacity=0.7))

# Another feature
fgp = folium.FeatureGroup(name="population")
fgp.add_child(folium.GeoJson(data=open("world.json", 'r', encoding='utf-8-sig').read(), style_function=lambda x: {'fillColor':'green'
if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

# Creating child of class Map
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")





