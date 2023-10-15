from turtle import fillcolor
import folium
import pandas 
print('done')
data=pandas.read_csv("volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])
name = list(data["NAME"])
 
html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""
def color_producer(elevation):
    if elevation<2000:
        return 'pink'
    elif 2000 <=elevation <3000:
        return 'blue'
    else:
        return 'orange'

map=folium.Map(location=[38.58,-99.89],zoom_start=6,tiles="Stamen Terrain") 



fg=folium.FeatureGroup(name="my map")
for lt,ln,el,name in zip(lat,lon,elev,name):
    iframe = folium.IFrame(html=html %(name, name, el), width=200, height=100)
    fg.add_child(folium.CircleMarker(location=[lt,ln],radius=6,
    popup=folium.Popup(iframe),fill_color=color_producer(el),color='white',fill=True
    ,fill_opacity=0.7))

    
map.add_child(fg)

map.save("map1.html")

