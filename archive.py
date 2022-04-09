# import os
# from platform import python_branch
# from socket import MSG_NOSIGNAL
# # print(os.getcwd())
# l=os.listdir()
# # print(l)
# f=open("MN_archive.xlsx")

# print(f)

from csv import excel
import email
from email.mime import image
import os
import pandas as pd


excel_file="/home/anubhaw-sharma/Documents/VS_Code/python/MN_archive.xlsx"
df= pd.read_excel(excel_file)
l=df.to_dict()

# for i in l['Name'].values():
#     print(i.upper())

# for i in range(len(l['Name'])):
#     print(l['Name'][i],l['Roll'][i],l['Email'][i])
user="ANUBHAW SHARMA"
note="keep learning"
roll="1808004"
email="anubhawapp@gmail.com"
linkedin_url="https://www.linkedin.com/in/anubhaw19/"
image_url="https://www.wrappixel.com/demos/ui-kit/wrapkit/assets/images/team/t4.jpg"




for i in range(len(l['Name'])):
    user=l["Name"][i].strip().title()
    note=l["Note"][i].strip()
    email=l["Email"][i]
    linkedin_url=l["Linkedin"][i]
    roll=l["Roll"][i]
    img_url=f"./images/{roll}.jpg/"
    


    img_url=f"./images/{roll}.jpg"
    text=f'''<div class="member-item col-md-6 col-lg-3">
              <div class="member">
                <div class="member-img">
                    <img src="{img_url}" onerror="this.onerror=null; this.src='./images/default.jpg'" class="img-fluid  img-thumbnail rounded-circle" alt="">
                </div>
                  <div class="member-info">
                      <h6>{note}</h6>
                  </div>
              <div class="content mt-2">
                <h4 >{user}</h4>
                <a href="mailto: {email}" id="share-em" class="sharer button"><i class="fa fa-2x fa-envelope-square"></i></a>
                <a href="{linkedin_url}" id="share-li" class="sharer button"><i class="fa fa-2x fa-linkedin-square"></i></a>
            </div>
            </div>
          </div>'''

    with open('output.txt', 'a') as f:
        f.write(text)
# print(type(user)) 


# with open('output.txt', 'a') as f:
#     f.write('')
# open("test.txt",'a')





# text=f'''<div class="member-item col-md-6 col-lg-3">
#               <div class="member">
#                 <div class="member-img">
#                     <img src="{image_url}" class="img-fluid  img-thumbnail rounded-circle" alt="">
#                 </div>
#                   <div class="member-info">
#                       <h6>{note}</h6>
#                   </div>
#               <div class="content mt-2">
#                 <h4 >{user}</h4>
#                 <a href="mailto: {email}" id="share-em" class="sharer button"><i class="fa fa-2x fa-envelope-square"></i></a>
#                 <a href="{linkedin_url}" id="share-li" class="sharer button"><i class="fa fa-2x fa-linkedin-square"></i></a>
#             </div>
#             </div>
#           </div>'''

# print(text)

# print(len(l['Name']))
# print(len(l['Roll']))
# print(len(l['Email']))
# print(len(l['linkedin']))
# print(len(l['note']))
# print(len(l['photo']))
# print(df.dtypes)
# print(l)
# new_dict=df.to_dict()


# print(df)
