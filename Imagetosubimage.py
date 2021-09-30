import cv2
 
# Read the main image
img_rgb = cv2.imread('C:/Users/Admin/Desktop/VAI/full_image.png')
img_gray=cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
cv2.imshow("image",img_rgb) 

#subimage loading/template
template = cv2.imread("C:/Users/Admin/Desktop/VAI/sub_image.png")
tmp_gray=cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)
h,w = tmp_gray.shape
cv2.imshow("template",template)
img = img_gray.copy()
result = cv2.matchTemplate(img,tmp_gray,cv2.TM_CCOEFF)
min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(result)

bottom_right = (max_loc[0] + w , max_loc[1] + h )
cv2.rectangle(img_rgb,max_loc,bottom_right,0,2)
cv2.imshow("Match",img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Cordinates are:",max_loc,(max_loc[0]+w,max_loc[1]),(bottom_right[0]-w,bottom_right[1]),bottom_right)


