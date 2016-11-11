# Kyle Luoma and Shannon Davis
# CSUMB CST 205 Multimedia programming module 2
# Lab # 6: Changing regions of pictures


#----- Warm up -----
# Driver: Shannon Davis
# Navigator: Kyle Luoma

def removeRedEye(pic):
# Simple algorithm to remove red eye error from a picture
  for x in range(0, getWidth(pic)):
    for y in range(0, getHeight(pic)):
      px = getPixel(pic, x, y)
      r = getRed(px)
      b = getBlue(px)
      g = getGreen(px)
      # Reduce the red level based upon proportion of red to blue and green:
      if r >= (b + g) * 0.85:
        avg = (b + g) / 2
        setRed(px, avg)
  repaint(pic)
  writePictureTo(pic, "C://Users//DESKTOP//Google Drive//CS Classes//CST 205 Multimedia Programming//Module 2//LAB6//removeRedEyeOutput.jpg")
  
#----- Problem 1 -----
# Driver: Shannon Davis
# Navigator: Kyle Luoma

def makeSepia(pic):
# Converts an image to sepiatone
  pic = betterBnW(pic)
  pixels = getPixels(pic)
  for px in pixels:
    r = getRed(px)
    if r < 63:
      setRed(px, r * 1.1)
      setBlue(px, getBlue(px) * 0.9)
    elif r < 192:
      setRed(px, r * 1.15)
      setBlue(px, getBlue(px) * 0.85)
    else:
      if r * 1.08 > 255:
        setRed(px, 255)
        setBlue(px, getBlue(px) * 0.93)
      else:
        setRed(px, r * 1.08)
        setBlue(px, getBlue(px) * 0.93)
  repaint(pic)
  writePictureTo(pic, "C://Users//KYLE//Google Drive//CS Classes//CST 205 Multimedia Programming//Module 2//LAB6//makeSepiaOutput.jpg")
  return pic



#----- Problem 2 -----
# Driver: Kyle Luoma
# Navigator: Shannon Davis

def artify(picIn):
# Modifies an image (picIn) and makes it "artsy"
  for x in range (0, getWidth(picIn)):
    for y in range (0, getHeight(picIn) - 1):
      pixel = getPixel(picIn, x, y)
      redLevel = getRed(pixel)
      greenLevel = getGreen(pixel)
      blueLevel = getBlue(pixel)
      
      if redLevel < 64:
        setRed(pixel, 31)
      if redLevel > 63 and redLevel < 128:
        setRed(pixel, 95)
      if redLevel > 127 and redLevel < 192:
        setRed(pixel, 159)
      if redLevel > 191 and redLevel < 256:
        setRed(pixel, 223)
      
      if greenLevel < 64:
        setGreen(pixel, 31)
      if greenLevel > 63 and greenLevel < 128:
        setGreen(pixel, 95)
      if greenLevel > 127 and greenLevel < 192:
        setGreen(pixel, 159)
      if greenLevel > 191 and greenLevel < 256:
        setGreen(pixel, 223)

      if blueLevel < 64:
        setBlue(pixel, 31)
      if blueLevel > 63 and blueLevel < 128:
        setBlue(pixel, 95)
      if blueLevel > 127 and blueLevel < 192:
        setBlue(pixel, 159)
      if blueLevel > 191 and blueLevel < 256:
        setBlue(pixel, 223)    
  repaint(picIn)
  writePictureTo(picIn, "C://Users//KYLE//Google Drive//CS Classes//CST 205 Multimedia Programming//Module 2//LAB6//artifyOutput.jpg")
  return picIn

#----- Problem 3 -----
# Driver: Kyle Luoma
# Navigator: Shannon Davis

def chromakey(foreground, background, sampleX, sampleY, tolerance):
# Replaces pixels with color value within tolerance range of color at sampleX sampleY coordinates
# in forground image with pixels from background image
  samplePixel = getPixel(foreground, sampleX, sampleY) 
  sampleColor = getColor(samplePixel)
  
  # match width dimensions of both images by shrinking larger image to size of smaller image:
  if getWidth(foreground) > getWidth(background):
    foreground = shrinkToSize(foreground, getWidth(background))
  elif getWidth(foreground) < getWidth(background):
    background = shrinkToSize(background, getWidth(foreground))  

  for x in range (0, getWidth(foreground)):
    for y in range (0, getHeight(foreground)):
      forePixel = getPixel(foreground, x, y)
      foreColor = getColor(forePixel)
      backPixel = getPixel(background, x, y)
      backColor = getColor(backPixel)
      if distance(sampleColor, foreColor) < tolerance:
        setColor(forePixel, backColor)

  repaint(foreground)
  writePictureTo(foreground, "C://Users//KYLE//Google Drive//CS Classes//CST 205 Multimedia Programming//Module 2//LAB6//chromakeyOutput.jpg")
  return foreground

def chromakeyTest():
  # Tests chromakey function with known parameters
  # Foreground should be the green screen picture
  foreground = makePicture(pickAFile())
  # Background should be your scene
  background = makePicture(pickAFile())
  # Provide pixel x and y coordinates for a point on foreground where the pixel is green
  x = 1
  y = 1
  
  # Select a tolerance for green pixel elimination (tolerance represents distance)
  tolerance = 100
  
  chromakey(foreground, background, x, y, tolerance)
  
#----- Useful non-homework assignment functions -----

def shrinkToSize(sourcePicture, newWidth = None, newHeight = None):
  # Shrinks an image to a selected size
  # Shrinks to either provided width and height, or if only width or
  # height is provided then maintains proportion and shrinks to 
  # provided dimension
  # Written by Kyle Luoma
  
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


def betterBnW(pic):
  #Written by Shannon Davis
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p) * 0.299
    g = getGreen(p) * 0.587
    b = getBlue(p) * 0.114
    luminance = r + g + b
    setRed(p, luminance)
    setGreen(p, luminance)
    setBlue(p, luminance)
  repaint(pic)
  return pic

