
import requests
import datetime
import base64
import json
import os , PyPDF2

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'start of, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



def getTest(user_id):
    url = "http://ec2-52-207-31-119.compute-1.amazonaws.com/send_test"
    response = requests.post(url,
                             data={'sender': {str(user_id)},
                                   'message': "Test request"})

    open("Recived_test.pdf", 'wb').write(response.content)


def sendSolvedTest(name,id):
    test_fd = open("hw4.pdf","rb")
    test_size = os.path.getsize("hw4.pdf")
    test = test_fd.read(test_size)

    # shift it to base 64
    sent_time = datetime.datetime.now()
    print(sent_time)
    headers = {"name": name,
               "ID"  : str(id),
               "time": str(sent_time),
               "file": str(test)
               }
    #print(headers)
    url = "http://ec2-52-207-31-119.compute-1.amazonaws.com/get_solved_test"
    response = requests.post(url,json=headers)

    print(response.text)
    return
    sendSolvedTest()



def makePremission():
    makePremission()




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Test Manger app')
    sendSolvedTest("Melisha",555)

