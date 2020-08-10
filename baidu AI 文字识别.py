from aip import AipOcr
import re

filePath = input("文件：")

APP_ID='1883946'
API_KEY='KrttEr98svFlLusVMM9RHZiM'
SECRET_KEY='LdS8zSdPEoAyV3MX34omZAMR2Gk4y0Ny'
client=AipOcr(APP_ID,API_KEY,SECRET_KEY)
i=open(r''+filePath+'','rb')
img=i.read()
msg=client.basicGeneral(img)
# msg是一个字典，其中words_result中包含了文字信息
for i in msg.get('words_result'):
  print(i.get('words'))

ticketNo = input("")