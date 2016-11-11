# Kyle Luoma
# CSUMB CST 205 Multimedia programming module 2
# Lab # 5: Advanced Image Manipulation

# ----- Warm up exercise -----

def copyToLarger(pictureToCopy):
  # Copies a picture passed as argument and returns copy on a larger canvas
  copiedPicture = makeEmptyPicture(getWidth(pictureToCopy) * 2, getHeight(pictureToCopy) * 2)
  xPad = getWidth(pictureToCopy) / 2
  yPad = getHeight(pictureToCopy) / 2
  for x in range (0, getWidth(pictureToCopy)):
    for y in range (0, getHeight(pictureToCopy)):
      readPixel = getPixel(pictureToCopy, x, y)
      readColor = getColor(readPixel)
      writePixel = getPixel(copiedPicture, x + xPad, y + yPad)
      setColor(writePixel, readColor)
  show(copiedPicture)
  writePictureTo(copiedPicture, "C://Users//Desktop//Google Drive//CS Classes//CST 205 Multimedia Programming//Module 2//LAB5//copyToLargerOutput.jpg")
  return copiedPicture

    
# ----- Problem 1 -----

def pyCopy(source, target, targetX, targetY):
  # Copies a picture passed as argument and returns copy on a larger canvas
  # where targetX and targetY represent the upper left point at which the
  # image is copied to the target canvas
  for x in range (0, getWidth(source)):
    for y in range (0, getHeight(source)):
      readPixel = getPixel(source, x, y)
      readColor = getColor(readPixel)
      writePixel = getPixel(target, x + targetX, y + targetY)
      setColor(writePixel, readColor)
  #Show and write picture -- recommend commenting out next 2 lines if running makeCollage() function
  show(target)
  writePictureTo(target, "C://Users//Desktop//Google Drive//CS Classes//CST 205 Multimedia Programming//Module 2//LAB5//pyCopyOutput.jpg")
  return target
  
def pyCopyTestDriver():
  sourcePicture = makePicture(pickAFile())
  targetPicture = makeEmptyPicture(getWidth(sourcePicture) * 2, getHeight(sourcePicture) * 2)
  pyCopy(sourcePicture, targetPicture, 100, 20)

  
# ----- Problem 2 -----  
  
  
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
    
  if newWidth == None and newHeight == None:
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

def shrinkToSizeTestDriver():
  sourcePicture = makePicture(pickAFile())
  shrinkToSize(sourcePicture, 311, 500)
  
def roseColoredGlasses(picIn):
# make an image appear pink
# Pink is a combination of red and white
# This effect is achieved by adding white (makeLighter)
 #and increasing the red level by 50 percent
  #picIn = get_picture()
  pixels = getPixels(picIn)
  for p in pixels:
    red = getRed(p)
    oldColor = getColor(p)
    newColor = makeLighter(oldColor)
    setColor(p, newColor)
    setRed(p, red + ((255 - red) * .8))
  return picIn


def betterBnW(picIn):
# Converts an image to grayscale using weighted average luminance  
  #picIn = get_picture()
  pixels = getPixels(picIn)
  for p in pixels:
    luminance = (float(getRed(p)) * 0.299) + (float(getGreen(p)) * 0.587) + \
                (float(getBlue(p)) * 0.114)
    shadeOfGrey = makeColor(luminance, luminance, luminance)
    setColor(p, shadeOfGrey)
  return picIn


def makeCollage():
  # Takes 8 pictures and distributes them on an 11 by 8.5 inch canvas
  collage = makeEmptyPicture(3300, 2550)
  addWidth = getWidth(collage) / 4
  addHeight = getHeight(collage) / 2
  effectSelect = 0
  
  for y in range (0, getHeight(collage), int(addHeight)):
    for x in range (0, getWidth(collage), int(addWidth)):    
      addPicture = makePicture(pickAFile())
      if effectSelect % 2 == 0:
        addPicture = roseColoredGlasses(addPicture)
      if effectSelect % 2 == 1:
        addPicture = betterBnW(addPicture)
      
      if getWidth(addPicture) > addWidth and getHeight(addPicture) > addHeight:
        addPicture = shrinkToSize(addPicture, addWidth, addHeight)
      elif getWidth(addPicture) <= addWidth and getHeight(addPicture) > addHeight:
        addPicture = shrinkToSize(addPicture, newHeight = addHeight)
      elif getWidth(addPicture) > addWidth and getHeight(addPicture) <= addHeight:
        addPicture = shrinkToSize(addPicture, newWidth = addWidth)
        
      pyCopy(addPicture, collage, x, y)
      effectSelect = effectSelect + 1
        
  show(collage)                                       
  writePictureTo(collage, "C://Users//Desktop//Google Drive//CS Classes//CST 205 Multimedia Programming//Module 2//LAB5//makeCollageOutput.jpg")
  return collage





