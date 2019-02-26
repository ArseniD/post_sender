import csv
import os
import requests


def content_collector(path):
    """
    Iterate through each file and get a content

    args:
        path: path to the folder with files

    return: dict with a name of files and content
    """

    content_dict = {}
    line = 0

    for root, dirs, files in os.walk(path):
        for filename in files:
            f_path = os.path.join(root, filename)

            with open(f_path) as f:
                if filename.endswith('.txt'):
                    content_dict[f_path.split('/')[-1]] = f.read()
                if filename.endswith('.csv'):
                    data = csv.reader(f)
                    for row in data:
                        line += 1
                        content_dict[f_path.split('/')[-1] + str(line)] = ''.join(row)
                else:
                    raise ValueError('File should be in txt or csv format')
    return content_dict


def post_data(file_name, content, job_link):
    """
    Send post request with given content data to the JOB_LINK

    args:
        file_name:  name of the file
        content:    file content
        job_link:   link to the job where we send our data

    print: file name, code status and response from server
    """
    r = requests.post(job_link, data=content)
    print("File:{0}\nStatus:{1}\nResponse:{2}\n-----------\n".format(file_name, r.status_code, r.reason))
