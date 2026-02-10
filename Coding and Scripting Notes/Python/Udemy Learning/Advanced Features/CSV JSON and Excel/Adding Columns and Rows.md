To add a column:

![alt text](image-18.png)

We call DF["Header"]=DF.shape[0]*["DATA"]
This is because our rows are index of 0 in the tuple in df.shape

**Note this is inplace and will change data permanently

---

To add a row it is slightly harder:

![alt text](image-19.png)

We have to call df.T to swap the rows and columns

![alt text](image-20.png)

We then add a column with our data

![alt text](image-21.png)

And then swap them again using df.T


---


To change data in  a column:

![alt text](image-22.png)

Example 2:

![alt text](image-23.png)

We call  DF["Column Header"]=DF["2nd Column Header"] + "string" + "string2"

---

df.shape:

![alt text](image-24.png)

This code gives you the shape (rows / columns) of your data frame in a tuple
