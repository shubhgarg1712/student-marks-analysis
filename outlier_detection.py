import pandas as pd
import numpy as np
number = int (input("Enter how many number you want to enter in a array: "))
lst=[]
subject=[]
for i in range (number):
    sub=input ("Enter the subject name for which you are entering the marks: ")
    subject.append(sub)
    num=int(input("Enter the marks obtained by you: "))
    lst.append(num)
arr=pd.DataFrame(lst)
np_arr=arr.values.flatten()

print("\n--- STATISTICS ---")
print("The number you entered are : ",np_arr)
mean = np.mean(np_arr)
std = np.std(np_arr)

print("Mean:", mean)
print("Standard Deviation:", std)

max_index = np.argmax(np_arr)
min_index = np.argmin(np_arr)

print(f"Maximum marks obtained in {subject[max_index]} is {np.max(np_arr)}")
print(f"Minimum marks obtained in {subject[min_index]} is {np.min(np_arr)}")
std=np.std(np_arr)
if (std == 0):
    print("There is no deviation in the marks so there is no outlier")
else:
    z_score = (np_arr-mean)/std

    outliers = np_arr[np.abs(z_score)>1]
    indexes = np.where(np.abs(z_score)>1)[0]
    if (len(outliers) == 0):
        print("No outlier is present in the marks:  ")
    else:
        print("The indexes of the outlier are : ", indexes)
        print("The outliers are : ", outliers)
        print("Outlier subjects:", [subject[i] for i in indexes])