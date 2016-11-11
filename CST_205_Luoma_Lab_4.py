# Kyle Luoma
# CSUMB CST 205 Multimedia programming module 2
# Lab # 4: Modifying pictures pixel by pixel

# ----- Warm up exercise -----

def halfBetter():
# Reduces red on half of an image
  file = pickAFile()
  pic = makePicture(file)
  for x in range(getWidth(pic) / 2, getWidth(pic)):
    for y in range(0, getHeight(pic)):
      p = getPixel(pic, x, y)
      r = getRed(p)
      setRed(p, r * 0.5)
  repaint(pic)
  writePictureTo(pic, "C://Users//Desktop//Google Drive//CS Classes//CST 205 Multimedia Programming//Module 2//hanifHalfBetter.jpg")
  

# ----- Problem 1 -----

def verticalMirror():
  # Mirrors the left half of an image onto the right half
  file = pickAFile()
  pic = makePicture(file)
  for x in range(0, getWidth(pic) / 2):
    for y in range(0, getHeight(pic)):
      readPixel = getPixel(pic, x, y)
      writePixel = getPixel(pic, getWidth(pic) - (x + 1), y)
      readColor = getColor(readPixel)
      setColor(writePixel, readColor)
  repaint(pic)
  writePictureTo(pic, "C://Users//Desktop//Google Drive//CS Classes//CST 205 Multimedia Programming//Module 2//verticalMirrorOutput.jpg")
  
def topToBottomMirror():
  # Mirrors the top half of an image onto the bottom half
  file = pickAFile()
  pic = makePicture(file)
  for x in range(0, getWidth(pic)):
    for y in range(0, getHeight(pic) / 2):
      readPixel = getPixel(pic, x, y)
      writePixel = getPixel(pic, x, getHeight(pic) - (y + 1))
      readColor = getColor(readPixel)
      setColor(writePixel, readColor)
  repaint(pic)
  writePictureTo(pic, "C://Users//Desktop//Google Drive//CS Classes//CST 205 Multimedia Programming//Module 2//topToBottomMirrorOutput.jpg")
  
def bottomToTopMirror():
  # Mirrors the bottom half of an image onto the top half
  file = pickAFile()
  pic = makePicture(file)
  for x in range(0, getWidth(pic)):
    for y in range(getHeight(pic) / 2, getHeight(pic)):
      readPixel = getPixel(pic, x, y)
      writePixel = getPixel(pic, x, getHeight(pic) - (y + 1))
      readColor = getColor(readPixel)
      setColor(writePixel, readColor)
  repaint(pic)
  writePictureTo(pic, "C://Users//Desktop//Google Drive//CS Classes//CST 205 Multimedia Programming//Module 2//bottomToTopMirrorOutput.jpg")
  
def quadMirror():
  # Mirrors the upper left quadrant of an image onto the three remaining quadrants
  file = pickAFile()
  pic = makePicture(file)
  for x in range(0, getWidth(pic) / 2):
    for y in range(0, getHeight(pic) / 2):
      # Get data of pixel to copy:
      readPixel = getPixel(pic, x, y)
      readColor = getColor(readPixel)
      
      # Get pixels to overwrite:
      writeUpperRightPixel = getPixel(pic, getWidth(pic) - (x + 1), y)
      writeLowerLeftPixel = getPixel(pic, x, getHeight(pic) - (y + 1))
      writeLowerRightPixel = getPixel(pic, getWidth(pic) - (x + 1), \
                             getHeight(pic) - (y + 1))
      
      # Set destination pixels to value of read pixel:
      setColor(writeUpperRightPixel, readColor)
      setColor(writeLowerLeftPixel,  readColor)
      setColor(writeLowerRightPixel, readColor)
  
  repaint(pic)
  writePictureTo(pic, "C://Users//Desktop//Google Drive//CS Classes//CST 205 Multimedia Programming//Module 2//quadMirrorOutput.jpg")
      

# ----- Problem 2 -----

def simpleCopy(pictureToCopy):
  # Copies a picture passed as argument and returns copy
  copiedPicture = makeEmptyPicture(getWidth(pictureToCopy), getHeight(pictureToCopy))
  for x in range (0, getWidth(pictureToCopy)):
    for y in range (0, getHeight(pictureToCopy)):
      readPixel = getPixel(pictureToCopy, x, y)
      readColor = getColor(readPixel)
      writePixel = getPixel(copiedPicture, x, y)
      setColor(writePixel, readColor)
  show(copiedPicture)
  writePictureTo(copiedPicture, "C://Users//Desktop//Google Drive//CS Classes//CST 205 Multimedia Programming//Module 2//simpleCopyOutput.jpg")
  return copiedPicture


# ----- Problem 3 -----

def rotatePic():
  # Rotates image 90 deg left
  file = pickAFile()
  pic = makePicture(file)
  rotatedPic = makeEmptyPicture(getHeight(pic), getWidth(pic))
  for x in range (0, getWidth(pic)):
    for y in range (0, getHeight(pic)):  
      readPixel = getPixel(pic, x, y)
      readColor = getColor(readPixel)
      writePixel = getPixel(rotatedPic, y, getHeight(rotatedPic) - (x + 1))
      setColor(writePixel, readColor)
  show(rotatedPic)
  writePictureTo(rotatedPic, "C://Users//Desktop//Google Drive//CS Classes//CST 205 Multimedia Programming//Module 2//rotatePicOutput.jpg")
  return rotatedPic


# ----- Problem 4 -----

def shrink():
  file = pickAFile()
  pictureToShrink = makePicture(file)
  shrunkenPicture = makeEmptyPicture((getWidth(pictureToShrink) / 2), (getHeight(pictureToShrink) / 2))
  for x in range (0, getWidth(pictureToShrink), 2):
    for y in range (0, getHeight(pictureToShrink), 2):
      readPixel = getPixel(pictureToShrink, x, y)
      readColor = getColor(readPixel)
      writePixel = getPixel(shrunkenPicture, (x // 2), (y // 2))
      setColor(writePixel, readColor)
  show(shrunkenPicture)
  writePictureTo(shrunkenPicture, "C://Users//Desktop//Google Drive//CS Classes//CST 205 Multimedia Programming//Module 2//shrinkOutput.jpg")
  return shrunkenPicture



  