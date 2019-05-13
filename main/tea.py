from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
import dash_html_components as html
filename = "my1.png"
parser = createParser(filename)
metadata = extractMetadata(parser)
l=[]
for line in metadata.exportPlaintext():
    l.append(html.P(line))
print(l)
from GPSPhoto import gpsphoto
# Get the data from image file and return a dictionary
data = gpsphoto.getGPSData('two.jpg')
print(data['Latitude'], data['Longitude'])
