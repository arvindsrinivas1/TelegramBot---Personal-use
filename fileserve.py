import urllib
import ast
import requests
import time

token="288155679:AAFCqedILCT3rvcz8kqeAF5G3PLJ3XYL8e4"

#------------------------------------------------------------------------------
response1 = requests.get("https://api.telegram.org/bot288155679:AAFCqedILCT3rvcz8kqeAF5G3PLJ3XYL8e4/getme")

#print response3
print response1
data2 = response1.content
data2="{"+data2[11:]
data2 = ast.literal_eval(data2)
result =data2['result']

print "My  Name is : %s" %(result['username'])
print "My  ID  is : %d" %(result['id'])
print "Call me %s" %(result['first_name'])

print " "
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
response3= requests.get("https://api.telegram.org/bot288155679:AAFCqedILCT3rvcz8kqeAF5G3PLJ3XYL8e4/getupdates")
data=response3.content
data='{'+data[11:]
data=ast.literal_eval(data)
result= data['result']

#result is an array of dictionaries where each dict is a message that an user has sent and
#this dict contains information about the user

global_access_details=[]

for i in result:
    from_details={}
    from_details['chat_id']=i['message']['from']['id']
    from_details['username']=i['message']['from']['username']
    from_details['served']=0
    from_details['text']=i['message']['text']
    global_access_details.append(from_details)

print global_access_details

#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
#SENDING A PHOTO
file_name = raw_input("Enter the name of the file you want to fetch:")+".jpeg"
url = "https://api.telegram.org/bot288155679:AAFCqedILCT3rvcz8kqeAF5G3PLJ3XYL8e4/sendphoto?chat_id=89525104"
files={'photo':open(file_name,'rb')}
response2=requests.post(url,files=files)

print response2.text
#--------------------------------------------------------------------------------
