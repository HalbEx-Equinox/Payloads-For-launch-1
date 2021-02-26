#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pynmea2
import folium


# In[2]:


file = open('examples/data.log', encoding='utf-8')
blr = folium.Map(location = [12.9716, 77.5946],zoom_start=7)

for line in file.readlines():
    try:
        msg = pynmea2.parse(line)
        folium.CircleMarker(location = [msg.latitude,msg.longitude],
                       radius = 5,
                       color='red',
                       fill = True,
                       fill_color="red").add_to(blr)
        folium.Marker(location = [msg.latitude,msg.longitude],
                  popup=folium.Popup(('<strong><font color= blue>Last Updated: '+str(msg.timestamp)+'</font></striong><br>' +
                    '<strong><b>Altitude: '+str(msg.altitude)+str(msg.geo_sep_units)+'</strong> <br>'),max_width=200)).add_to(blr)
    except pynmea2.ParseError as e:
        print('Parse error: {}'.format(e))
        continue


# In[3]:


blr

