#exif_data.py


from PIL import Image, ExifTags
from pprint import pprint

def get_info(path):
    img = Image.open(path)
    exif = {
    ExifTags.TAGS[k]: v
    for k , v in img._getexif().items()
    if k in ExifTags.TAGS
    }

    if exif:
        north = exif['GPSInfo'][2]
        east = exif['GPSInfo'][4]
        lat = ((((north[0]*60)+north[1])*60)+north[2])/60/60
        long =  ((((east[0]*60)+east[1])*60)+east[2])/60/60

        lat, long = (float(lat)), (float(long))
        return lat, long