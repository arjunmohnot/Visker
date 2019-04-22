from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
filename = "some_image.png"
parser = createParser(filename)
metadata = extractMetadata(parser)
linestring=''
for line in metadata.exportPlaintext():
    linestring+=line+'\n'
print(linestring)
