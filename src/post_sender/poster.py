import glob
import os
import requests


JOB_LINK = "http://esbaraciap02d.burberry.corp:8500/jms-prod/write_new_mq?queue=BUR.CIRRUS.YMKT.ABANDONED.CART"


def content_collector(path):

    content_dict = {}

    for filename in glob.glob(os.path.join(path, '*.txt')):
        with open(filename) as file:
            content_dict[filename.split('/')[2]] = file.read()
    return content_dict

def post_data(file_name, content):
    r = requests.post(JOB_LINK, data=content)
    print "File:{0}\nStatus:{1}\nResponse:{2}\n-----------\n".format(file_name, r.status_code, r.reason)




