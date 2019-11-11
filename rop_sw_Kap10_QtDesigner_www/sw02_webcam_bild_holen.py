### JPG holen
from PIL import Image
""" fuer grosse Bilddateien notwendig"""
""" https://stackoverflow.com/questions/12984426/python-pil-ioerror-image-file-truncated-with-big-images"""
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import urllib

website = urllib.urlopen('http://www.irs-alpsee-gruenten.de/se_data/_filebank/webcam/bbm.jpg')
jpgfile = open('bild.jpg', 'wb')
webfile = website.read()
jpgfile.write(webfile)
img = Image.open('bild.jpg')
print(img.size)
print(img.format)
img.show()
website.close()
jpgfile.close()
