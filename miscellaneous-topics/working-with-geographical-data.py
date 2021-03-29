"""
Many applications involve working with geographical data. For example, when
tracking global weather, we might want to plot the temperature as measured by
various sensors around the world at their position on a map. For this, we can
use the GeoPandas package and the Geoplot package, both of which allow us to
manipulate, analyze, and visualize geographical data.

This module illustrates how to use GeoPandas and Geoplot packages to load and
visualize some sample geographical data.
"""
import geoplot
import geopandas
import matplotlib.pyplot as plt

world = geopandas.read_file(
        geopandas.datasets.get_path("naturalearth_lowres"))

cities = geopandas.read_file(
        geopandas.datasets.get_path("naturalearth_cities"))

fig, ax = plt.subplots()
geoplot.polyplot(world, ax=ax)
geoplot.pointplot(cities, ax=ax, fc="r", marker="2")
ax.axis((-180, 180, -90, 90))

plt.show()
