
import cv2


img =cv2.imread('bat.jpeg')
img =cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
img = img[250:250]
cv2.imshow('mateus', img)
cv2.waitKey()
cv2.destroyAllWindows()

i = img[1:1]

"""greyValueImage =cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)




for index in range(len(greyValueImage)):
    xo, yo = index
    x = np.array(xo)
    y = np.array(yo)
    xmi = min(x)
    xma = max(x)
    ymi = min(y)
    yma = max(y)
    vals = greyValueImage[xo, yo]
    if vals > 0 :
        img = cv2.rectangle(img,(xmi,ymi),(xma,yma),(255,0,0),1)
             






  
cv2.imshow('mateus', img)
cv2.waitKey()
cv2.destroyAllWindows()
"""