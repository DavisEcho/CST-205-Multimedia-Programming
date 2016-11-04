# Kyle Luoma and Shannon Davis
# CSUMB CST 205 Multimedia programming module 2
# Lab # 6: Changing regions of pictures


#----- Warm up -----

def removeRedEye():
# Removes red eye error from a specific image downloaded from google images


#----- Problem 1 -----

def makeSepia(picIn):
# Creates a sepia tone image


#----- Problem 2 -----

def artify(picIn):
# Modifies an image (picIn) and makes it "artsy"


#----- Problem 3 -----

def chromakey(foreground, background, sampleX, sampleY, tolerance):
# Replaces pixels with color value within tolerance range of color at sampleX sampleY coordinates
# in forground image with pixels from background image









#----- Useful non-homework assignment functions -----

def shrinkToSize(sourcePicture, newWidth = None, newHeight = None):
  # Shrinks an image to a selected size
  # Shrinks to either provided width and height, or if only width or
  # height is provided then maintains proportion and shrinks to 
  # provided dimension
  
  sourceHeight = getHeight(sourcePicture)
  sourceWidth = getWidth(sourcePicture)
  
  if newWidth > sourceWidth or newHeight > sourceHeight:
    print("Provided argument as new dimension that was greater than source dimension")
    return sourcePicture
  
  if newWidth == None and newHeight > 0:
    newWidth = sourceWidth * (newHeight / float(sourceHeight))
    newWidth = int(newWidth) + 1
    
  if newHeight == None and newWidth > 0:
    newHeight = sourceHeight * (newWidth / float(sourceWidth))
    newHeight = int(newHeight) + 1
    
  if newWidth == None and newWidth == None:
    return sourcePicture
        
  widthRatio = sourceWidth / newWidth
  heightRatio = sourceHeight / newHeight
        
  targetPicture = makeEmptyPicture(newWidth, newHeight)
  
  for y in range (0, newHeight * heightRatio, int(heightRatio)):
    for x in range (0, newWidth * widthRatio, int(widthRatio)):
      readPixel = getPixel(sourcePicture, x, y)
      readColor = getColor(readPixel)
      writePixel = getPixel(targetPicture, (x // widthRatio), (y // heightRatio))
      setColor(writePixel, readColor)
  #show(targetPicture)
  writePictureTo(targetPicture, "C://Users//Desktop//Google Drive//CS Classes//CST 205 Multimedia Programming//Module 2//LAB5//shrinkToSizeOutput.jpg")
  return targetPicture


def betterBnW(picIn):
# Converts an image to grayscale using weighted average luminance  
# Imported from previous lab:
  pixels = getPixels(picIn)
  for p in pixels:
    luminance = (float(getRed(p)) * 0.299) + (float(getGreen(p)) * 0.587) + \
                (float(getBlue(p)) * 0.114)
    shadeOfGrey = makeColor(luminance, luminance, luminance)
    setColor(p, shadeOfGrey)
  return picIn
