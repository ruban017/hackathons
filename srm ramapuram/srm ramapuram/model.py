#model.py


from gmplot import gmplot
import uuid


def locatee(lat, long):
    gmap = gmplot.GoogleMapPlotter(lat, long, 12)

    gmap.marker(lat, long, 'cornflowerblue')
    

    gmap.draw('location.html')