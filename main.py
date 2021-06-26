import requests
import datetime
import base64
import json
import os
import psutil

from subprocess import Popen, PIPE
"""
global variable section
"""
user_unique_id = 0

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'start of, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def getTest(user_id):
    url = "http://ec2-52-207-31-119.compute-1.amazonaws.com/send_test" ## TBD
    response = requests.post(url,
                             data={'sender': {str(user_id)},
                                   'message': "Test request"})

    open("Recived_test.pdf", 'wb').write(response.content)


def sendSolvedTest(name,ID):
    test_fd = open("hw4.pdf", "rb")
    test_size = os.path.getsize("hw4.pdf")
    test = test_fd.read(test_size)

    # shift it to base 64
    encoded_bytes = base64.b64encode(str(test).encode("utf-8"))
    encoded_test = str(encoded_bytes, "utf-8")


    sent_time = datetime.datetime.now()
    print(sent_time)
    headers = {"name": name,
               "ID": str(ID),
               "time": str(sent_time),
               "user_unique_id":str(user_unique_id),
               "file": encoded_test
               }
    # print(headers)
    url = "http://ec2-52-207-31-119.compute-1.amazonaws.com/get_solved_test"
    response = requests.post(url, json=headers)

    print(response.text)
    return



def userLogin():
    usr_details_fd = open("user_details.txt","r")

    ## reading user details
    name     = usr_details_fd.readline().replace("\n","")
    ID       = usr_details_fd.readline().replace("\n","")
    password = usr_details_fd.readline().replace("\n","")

    sent_time = datetime.datetime.now()
    print(name + ID + password)
    headers = {"name": str(name),
               "ID": str(ID),
               "password": str(password),
               "time":  str(sent_time)}

    url = "http://ec2-52-207-31-119.compute-1.amazonaws.com/student_login"
    response = requests.post(url, json=headers)
    print(response.text) #debug
    if (response.text == "AUTHENTICATION FAILED") :
        print("AUTHENTICATION FAILED")
        return 1
    server_response = response.json()
    #server_response = {'unique_id': "unique_id",'permission':"Approved"} --debug

    if (server_response['permission'] == "Approved") :
        user_permission_fd = open("user_permission",'w')
        student_uniqu_id   = server_response['unique_id']
        user_unique_id     = server_response['unique_id']
        print("unique ID is : " + student_uniqu_id)
        user_permission_fd.write(student_uniqu_id + "\n")
        user_permission_fd.close()
        #print(response.json())
        #return("student permission aproved")
        return 0
    else:
        print("student permission denied")
        return (1)



def pingToServer():
    tcp_connection = psutil.net_connections()
    url = "" #TBD
    ping_tcp_connection = str({"user_unique_id":user_unique_id})
    counter = 0
    for connection in (tcp_connection):
        laddr = str(connection[3])[str(connection[3]).find("=")+ 2:str(connection[3]).find(",") - 1]
        raddr = str(connection[4])[str(connection[4]).find("=")+2:str(connection[4]).find(",")-1]
        if (connection[4] == () or laddr.__eq__(raddr) or connection[5] != "ESTABLISHED"):
            continue # passes not relevant connections
        line_append = str({"laddr": laddr, "raddr": raddr, "status": str(connection[5])}) ## TBD status is need ?
        counter = counter + 1
        ping_tcp_connection = ping_tcp_connection + line_append
    print(ping_tcp_connection)
    print(counter)

    #response = requests.post(url, json=ping_tcp_connection)





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Test Manger app')
    #pingToServer()

    pingToServer()
    #userLogin()
    #sendSolvedTest("Melisha", 555)

