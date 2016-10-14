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

chatidList=[]
#--------------------------------------------------------------------------------
global_access_details=[]
used_msg_id=[]

#SENDING A PHOTO
def serve(text):
    if(text!="\/start"):
        file_name =text+".jpeg"
        print file_name
        url = "https://api.telegram.org/bot288155679:AAFCqedILCT3rvcz8kqeAF5G3PLJ3XYL8e4/sendphoto?chat_id=89525104"
        files={'photo':open(file_name,'rb')}
        response2=requests.post(url,files=files)
        time.sleep(5)


while(True):
    response3= requests.get("https://api.telegram.org/bot288155679:AAFCqedILCT3rvcz8kqeAF5G3PLJ3XYL8e4/getupdates")
    data=response3.content
    data='{'+data[11:]
    data=ast.literal_eval(data)
    result= data['result']

    #result is an array of dictionaries where each dict is a message that an user has sent and
    #this dict contains information about the user
    for i in result:
        #from_details={}
        print "Test"
        chat_id=i['message']['message_id']
        time.sleep(5)
        print chat_id
        #chat_id=i['message']['from']['id']
        if chat_id not in chatidList:
            text=i['message']['text']
            print text
            serve(text)
            print " served with file: "+text
            chatidList.append(chat_id)
