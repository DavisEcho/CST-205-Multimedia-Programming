
# ----- Warm up -----

# ----- Problem 1 -----

class ColorSeed:
  pixelDist = 0
  weight = 0
  def __init__(self, xCoord, yCoord, redVal, greenVal, blueVal, intensity):
    self.xCoord = xCoord
    self.yCoord = yCoord
    self.redVal = redVal
    self.greenVal = greenVal
    self.blueVal = blueVal
    self.intensity = intensity

def buildCard():
# Makes a 7 x 5 canvas (A7 greeting card)
  card = makeEmptyPicture(2100, 1500)
  card = makeCardBackground(card)
  #card = makePicture(pickAFile())
  for i in range (0, 10):
    card = makeCardBorder(card, 100 + i)
  card = makeCardBorder(card, 130)
  card = addWords(card)
  card = addPicture(card)
  
  show(card)
  writePictureTo(card, "C://Users//Desktop//Google Drive//CS Classes//CST 205 Multimedia Programming//Module 3//buildCardOutput.jpg")

def addPicture(card):
  pictureToAdd = makePicture(pickAFile())
  if getWidth(pictureToAdd) < getWidth(card):
    pictureToAdd = copyToLarger(pictureToAdd, getWidth(card), getHeight(card))
  card = chromakey(pictureToAdd, card, 1, 1, 30)
  return card

def addWords(card):
# Adds a nice thanksgiving greeting to the card
  import java.awt.Font as Font
  topWords = "HAPPY"
  bottomWords = "THANKSGIVING!"
  fontSize = 96
  myFont = makeStyle("Comic Sans", Font.BOLD, fontSize)
  yMargin = 250
  
  addTextWithStyle(card, (getWidth(card) / 2) - (fontSize * (len(topWords)/2)), yMargin, topWords, myFont, black)
  addTextWithStyle(card, 180 + (getWidth(card) / 2) - (fontSize * (len(bottomWords)/2)), \
                   getHeight(card) - (yMargin - fontSize), bottomWords, myFont, black)
  return card

def makeCardBorder(card, margin):
# Draws a black border with inverted corner arches
  arcSpace = margin
  # Top horizontal:
  addLine(card, margin + arcSpace, margin, getWidth(card) - (margin + arcSpace), margin, black)
  # Bottom horizontal:
  addLine(card, margin + arcSpace, getHeight(card) - margin, getWidth(card) - (margin + arcSpace), getHeight(card) - margin, black)
  # Left vertical:
  addLine(card, margin, margin + arcSpace, margin, getHeight(card) - (margin + arcSpace), black)
  # Right vertical:
  addLine(card, getWidth(card) - margin, margin + arcSpace, getWidth(card) - margin, getHeight(card) - (margin + arcSpace), black)
  # Top left arc:
  addArc(card, 0, 0, (margin * 2), (margin * 2), 0, -90, black)
  # Top right arc:
  addArc(card, getWidth(card) - (margin * 2), 0, (margin * 2), (margin * 2), 180, 90, black)
  # Bottom left arc:
  addArc(card, 0, getHeight(card) - (margin * 2), (margin * 2), (margin * 2), 0, 90)
  # Bottom right arc:
  addArc(card, getWidth(card) - (margin * 2), getHeight(card) - (margin * 2), (margin * 2), (margin * 2), 90, 90, black)
  
  repaint(card)
  return card

def makeCardBackground(card):
# Creates a background based on "seeds" that radiate colors with a given 
# intensity. Creates a gradient effect.
  # Create color seeds:
  greenSeed  = ColorSeed(100 , 100 , 202, 255,  50, .3)
  brownSeed  = ColorSeed(2000, 1400, 129, 113,  25, .7)
  tanSeed    = ColorSeed(1050, 750 , 255, 169,  25, .2)
  orangeSeed = ColorSeed(600 , 1300, 232,  97,  34, .8)
  creamSeed  = ColorSeed(1500, 200 , 255,  99, 102, .3)
  blackSeed  = ColorSeed(400 , 400 ,   1,   1,   1, .9)
  
  # "Plant" color seeds:
  seedArray = [ greenSeed,  \
                brownSeed,  \
                tanSeed,    \
                orangeSeed, \
                creamSeed ]             
  
  # "Grow" color seeds:
  card = growSeeds(seedArray, card)
  
  show(card)
  writePictureTo(card, "C://Users//Desktop//Google Drive//CS Classes//CST 205 Multimedia Programming//Module 3//backgroundOutput.jpg")
  return card


def growSeeds(seedArray, card):
# Sets value of pixels in an image based on color, proximity and intensity of each seed in seedArray
  totalIntensity = 0
  for seed in seedArray:
    totalIntensity = totalIntensity + seed.intensity

  for x in range (0, getWidth(card)):
    for y in range (0, getHeight(card)):
      pixel = getPixel(card, x, y)
      setColor(pixel, black)
      totalDist = 0
      totalWeight = 0
      for seed in seedArray:
        xDist = abs(x - seed.xCoord)
        yDist = abs(y - seed.yCoord)
        seed.pixelDist = sqrt((xDist**2) + (yDist**2))
        if seed.pixelDist == 0:
          seed.pixelDist = 1
        totalDist = totalDist + seed.pixelDist
      for seed in seedArray:
        seed.weight = (totalDist / seed.pixelDist) * (seed.intensity / totalIntensity)
        totalWeight = totalWeight + seed.weight
      for seed in seedArray:
        setRed(pixel, getRed(pixel) + (seed.redVal) * (seed.weight / totalWeight))
        setGreen(pixel, getGreen(pixel) + (seed.greenVal) * (seed.weight / totalWeight))
        setBlue(pixel, getBlue(pixel) + (seed.blueVal) * (seed.weight / totalWeight))      
  return card
        

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
  return foreground


def copyToLarger(pictureToCopy, width, height):
  # Copies a picture passed as argument and returns copy on a larger canvas with provided dimensions
  copiedPicture = makeEmptyPicture(width, height)
  xPad = (width - getWidth(pictureToCopy)) / 2
  yPad = (height - getHeight(pictureToCopy)) / 2
  for x in range (0, getWidth(pictureToCopy)):
    for y in range (0, getHeight(pictureToCopy)):
      readPixel = getPixel(pictureToCopy, x, y)
      readColor = getColor(readPixel)
      writePixel = getPixel(copiedPicture, x + xPad, y + yPad)
      setColor(writePixel, readColor)
  return copiedPicture  
      
        

    
    