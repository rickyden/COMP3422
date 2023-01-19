import cv2
im = cv2.imread('example_image.jpeg')
im_border = cv2.copyMakeBorder(im, 30,30,30,30,cv2.BORDER_CONSTANT,None,value=0)
cv2.imwrite('example_image_with_border.jpeg', im_border)