import os
import requests


JOB_LINK = "http://esbaraciap02d.burberry.corp:8500/jms-prod/write_new_mq?queue=BUR.CIRRUS.YMKT.ABANDONED.CART"

def content_collector(path):
    """
    Given a path to the folder with files,
    iterate through each file and get content

    return: dict with name of files and content
    """
    content_dict = {}
    for root, dirs, files in os.walk(path):
        for filename in files:
            if filename.endswith('.txt'):
                file_path = os.path.join(root, filename)
                with open(file_path) as file:
                    content_dict[file_path.split('/')[-1]] = file.read()
    return content_dict

def post_data(file_name, content):
    """
    Send post request with given content data to the JOB_LINK

    print: file name, code status and response from server
    """
    r = requests.post(JOB_LINK, data=content)
    print "File:{0}\nStatus:{1}\nResponse:{2}\n-----------\n".format(file_name, r.status_code, r.reason)




