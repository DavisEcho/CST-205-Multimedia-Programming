

def lineDrawing(picIn):
  picIn = betterBnW(picIn)
  scanWidth = getWidth(picIn) - 1
  scanHeight = getHeight(picIn) - 1
  tolerance = 3
  
  for x in range (0, scanWidth):
    for y in range (0, scanHeight):
      pixel = getPixel(picIn, x, y)
      if abs(getRed(pixel) - getRed(getPixel(picIn, x + 1, y))) > tolerance and abs(getRed(pixel) - getRed(getPixel(picIn, x, y + 1))) > tolerance:
        setColor(pixel, black)
      else:
        setColor(pixel, white)
  writePictureTo(picIn, "C://Users//Desktop//Google Drive//CS Classes//CST 205 Multimedia Programming//Module 3//lineDrawingOutput.jpg")
  show(picIn)

# ----- Imported Functions -----

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
