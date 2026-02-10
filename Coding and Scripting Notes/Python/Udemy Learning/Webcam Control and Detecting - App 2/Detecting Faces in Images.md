First we want to store a cascade clasifier object in a variable:

![alt text](image-7.png)

    We can use cv2.CascadeClassifer() and pass the XML Cascade


Then we want to read the image (Usually easier to detect in grayscale)

![alt text](image-8.png)


We then want to use .detectMultiScale to detect the face:

    We also pass a scale here (how python reads the image) which is more accurate if smaller
    And we pass minNeighbors (Tells python how many neighbors to search around the window)
    
![alt text](image-9.png)

Then to create the rectangle around the face:

![alt text](image-10.png)

The for loop contains an updated img variable:
Passing (image, (coord, coord), (coord +width, coord+height), (B, G, R), (width of rectangle)
