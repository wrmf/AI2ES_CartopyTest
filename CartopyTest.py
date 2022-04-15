import cartopy as ccrs
import matplotlib.pyplot as plt

plt.figure(figsize=(9.4248, 3))
ax = plt.axes(projection=ccrs.crs.LambertCylindrical())
ax.stock_img()

plt.show()
plt.savefig('testPlot.png', transparent=True, dpi=100)
print('Saved plot')