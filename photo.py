import os
import PIL
from PIL import Image

from csv import excel
import email
from email.mime import image
from numpy import source
import pandas as pd


# excel_file="/home/anubhaw-sharma/Documents/VS_Code/python/MN_archive.xlsx"
# df= pd.read_excel(excel_file)
# l=df.to_dict()

f=r'/home/anubhaw-sharma/Documents/VS_Code'
f_resize=r'/home/anubhaw-sharma/Documents/VS_Code/resized_img'
# print(os.listdir(f))

# for renaming images>>>
# for i in os.listdir(f):
#     for j in range(len(l['Name'])):
#         if l['Name'][j].strip().lower() in i.strip().lower():
#             os.rename(f+"/"+i,f+"/"+str(l['Roll'][j])+".jpg")
#             break
        

# for resizing images>>>
# for i in os.listdir(f):
#     f_img=f+"/"+i
#     f_reimg=f_resize+"/"+i
#     img=Image.open(f_img)
#     img = img.resize((360, 345))
#     img.save(f_reimg)
    
f_img=f+"/"+"1808004.jpg"
f_reimg=f_resize+"/"+"1808004.jpg"
img=Image.open(f_img)
img = img.resize((360, 345))
img.save(f_reimg)


# print(l)
# if "pic" in img.filename:
#     print("Exists")
# else:
#     print("Does not exist")

