
import requests
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def sendTest():
    test = open("test_to_send.pdf","rb")
    #sender_details = name + " " + str(id);
    url = "http://ec2-52-207-31-119.compute-1.amazonaws.com/get_solved_test"
    response = requests.post(url, files={'attachment': test})
    print(response)
    #return requests.post(
    #    "http://ec2-52-207-31-119.compute-1.amazonaws.com/get_solved_test",
        #auth=("api", API_KEY),
        #files=[("attachment", ("test.pdf", test))],
        #data={"from": "User " + sender_details,
        #      "to": "main test server",
        #      "subject": "test attachment",
        #      "text": "sending test",
        #      "html": "<html>HTML version of the body</html>"})
    sendTest()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    sendTest()

