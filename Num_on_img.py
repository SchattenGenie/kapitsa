import cv2
def place_num_on_img(img = 'test.png', num = 0.5):
    font = cv2.FONT_HERSHEY_COMPLEX
    img = cv2.imread(img)
    cv2.putText(img,"{:.2f}".format(num)+"%",(600,370), font, 4, (56,121,126), 7, cv2.LINE_AA);
    return img
