from flask import Flask, render_template
import urllib.request as request
import pandas as pd
import folium

app = Flask(__name__)

# 讀取車位資料
df_park = pd.read_csv('parking.csv')

# 新增地圖
map = folium.Map([23.5, 121], zoom_start=7, tiles='OpenStreetMap')

from folium.plugins import MarkerCluster

marker_cluster = MarkerCluster().add_to(map)

for index, row in df_park.iterrows(): 
        information = str(row['ROADNAME']) + '' + str(row['PAYCASH'])
        folium.Marker(location = [row['lat'], row['lon']], popup = information).add_to(marker_cluster)

#map.save('park.html')

# 讀取道路挖掘資料
df_dig = pd.read_csv('digging.csv')
# df_dig.head()

# 經緯度轉換
 # from shapely.geometry import Point
 # import geopandas as gpd
 # geom = [Point(xy) for xy in zip(df_earthquake.TWD97X, df_earthquake.TWD97Y)]
 # crs = {'init': 'epsg:3826'}
 # gdf = gpd.GeoDataFrame(df_earthquake, crs=crs, geometry=geom)

# 新增地圖
map = folium.Map([23.5, 121], zoom_start=7, tiles='OpenStreetMap')

from folium.plugins import MarkerCluster

marker_cluster = MarkerCluster().add_to(map)

for index, row in df_dig.iterrows(): 
        information = str(row['CaseStart']) + '~' + str(row['CaseEnd']) + '' + str(row['DigSite'])
        folium.Marker(location = [row['LAT'], row['LONG']], popup = information).add_to(marker_cluster)

#map.save('dig.html')

# 讀取加油站資料
df_gas = pd.read_csv('gas station.csv')

# 新增地圖
map = folium.Map([23.5, 121], zoom_start=7, tiles='OpenStreetMap')

from folium.plugins import MarkerCluster

marker_cluster = MarkerCluster().add_to(map)

for index, row in df_gas.iterrows():
        information = str(row['station']) + '' + str(row['address'])
        folium.Marker(location = [row['Latitude'], row['Longitude']], popup = information).add_to(marker_cluster)

#map.save('gas.html')

@app.route('/')
def park():
     return render_template('park.html')

@app.route('/dig')
def dig():
     return render_template('dig.html')

@app.route('/gas')
def gas():
    return render_template('gas.html')

if __name__ == '__main__':
    app.run()  
