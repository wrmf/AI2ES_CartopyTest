import cartopy as ccrs
import matplotlib.pyplot as plt
import numpy as np
import cartopy.io.shapereader as shpreader

central_lat = 37.5
central_lon = -96
extent = [-120, -70, 24, 50.5]
central_lon = np.mean(extent[:2])
central_lat = np.mean(extent[2:])

plt.figure(figsize=(12, 6))
ax = plt.axes(projection=ccrs.crs.AlbersEqualArea(central_lon, central_lat))
ax.set_extent(extent)

ax.add_feature(ccrs.feature.OCEAN)
ax.add_feature(ccrs.feature.LAND, edgecolor='black')
ax.add_feature(ccrs.feature.LAKES, edgecolor='black')
ax.add_feature(ccrs.feature.RIVERS)
ax.add_feature(ccrs.feature.STATES)
ax.gridlines()

plt.savefig('testPlot.png')
plt.show()
print('Saved plot')
