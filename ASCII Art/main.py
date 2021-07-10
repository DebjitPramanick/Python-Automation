from PIL import Image
import sys

path = sys.argv[0]
img=Image.open('art.jpeg')
width, height = img.size
aspectRatio=height/width
newWidth = 150
newHeight=aspectRatio*newWidth
img=img.resize((newWidth, int(newHeight)))

img=img.convert('L')
pixel=img.getdata()

char = ["@","#","S","%","?","*","+",";",":",",","."]

newPixel=[char[p//25] for p in pixel]
newPixel=''.join(newPixel)

newPixelCount = len(newPixel)
finalImage=[newPixel[index:index+newWidth] for index in range(0, newPixelCount, newWidth)]
finalImage='\n'.join(finalImage)

with open("res.txt", "w") as f:
    f.write(finalImage)
