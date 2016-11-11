# Kyle R. Luoma
# CST 205-40 Multimedia Programming
# Module 1, lab 3
# 27-October-2016

# ---- Warmup ----
def get_picture():
#Loads picture from file
  return makePicture(pickAFile())
  
  
def halfRedWarmup():
# Reduces red level in picture by 50%
  picIn = get_picture()
  pixels = getPixels(picIn)
  for p in pixels:
    red = getRed(p)
    setRed(p, red * 0.5)
  repaint(picIn)
  

def noBlue():
# Removes all blue from an image
  picIn = get_picture()
  pixels = getPixels(picIn)
  for p in pixels:
    setBlue(p, 0)
  repaint(picIn)
    

# ---- Problem 1 ----
def lessRed(percentageReduction):
# Reduces red level of picture by percentage provided as argument
# NOTE: Provide an integer between 0 - 100 to represent a percentage
  picIn = get_picture()
  pixels = getPixels(picIn)
  for p in pixels:
    red = getRed(p)
    setRed(p, red * ((100 - percentageReduction) / float(100)))
  repaint(picIn)  

def halfRed():
  lessRed(50)


# ---- Problem 2 ----
def moreRed(percentageIncrease):
# Increases red level of picture by percentage provided as argument
# NOTE: Provide an integer between 0 - 100 to represent a percentage increase
  picIn = get_picture()
  pixels = getPixels(picIn)
  for p in pixels:
    red = getRed(p)
    # Red level can only increase to value of 255, so a percentage increase
    # must be a percentage of the difference between the current red level 
    # and the maximum possible:
    redBelowMax = 255 - red
    setRed(p, red + (redBelowMax * (percentageIncrease / float(100))))
  repaint(picIn)


# ---- Problem 3 ----
def roseColoredGlasses():
# make an image appear pink
# Pink is a combination of red and white
# This effect is achieved by adding white (makeLighter)
 #and increasing the red level by 50 percent
  picIn = get_picture()
  pixels = getPixels(picIn)
  for p in pixels:
    red = getRed(p)
    oldColor = getColor(p)
    newColor = makeLighter(oldColor)
    setColor(p, newColor)
    setRed(p, red + ((255 - red) * .8))
  repaint(picIn)


# ---- Problem 4 ----
def lightenUp():
# Makes an image lighter (or brighter)
  picIn = get_picture()
  pixels = getPixels(picIn)
  for p in pixels:
    darkerColor = getColor(p)
    lighterColor = makeLighter(darkerColor)
    setColor(p, lighterColor)
  repaint(picIn)


# ---- Problem 5 ----
def makeNegative():
# Inverts RGB values to create a negative image
  picIn = get_picture()
  pixels = getPixels(picIn)
  for p in pixels:
    posRed = getRed(p)
    setRed(p, 255 - posRed)
    posGreen = getGreen(p)
    setGreen(p, 255 - posGreen)
    posBlue = getBlue(p)
    setBlue(p, 255 - posBlue)
  repaint(picIn)
    

# ---- Problem 6 ----
def BnW():
# Converts an image to grayscale using unweighted average luminance
  picIn = get_picture()
  pixels = getPixels(picIn)
  for p in pixels:
    luminance = (getRed(p) + getGreen(p) + getBlue(p)) / 3
    shadeOfGrey = makeColor(luminance, luminance, luminance)
    setColor(p, shadeOfGrey)
  repaint(picIn)


def betterBnW():
# Converts an image to grayscale using weighted average luminance  
  picIn = get_picture()
  pixels = getPixels(picIn)
  for p in pixels:
    luminance = (float(getRed(p)) * 0.299) + (float(getGreen(p)) * 0.587) + \
                (float(getBlue(p)) * 0.114)
    shadeOfGrey = makeColor(luminance, luminance, luminance)
    setColor(p, shadeOfGrey)
  repaint(picIn)







    