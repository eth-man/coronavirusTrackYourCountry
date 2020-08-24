#!/usr/bin/env python3
from optparse import OptionParser
from bs4 import BeautifulSoup
import requests
import time
import argparse

data_check= []
worldmetersLink = "https://www.worldometers.info/coronavirus/"

parser = argparse.ArgumentParser(
    description='Example with nonoptional arguments',
)

parser.add_argument('country', action="store", type=str)
parser.add_argument('label', action="store")

args=parser.parse_args()
country=args.country
def data_cleanup(array):
    L = []
    for i in array:
        i = i.replace("+","")
        i = i.replace("-","")
        i = i.replace("N/A","")
        i = i.replace(",",".")
        if i == "":
            i = "0"
        L.append(i.strip())
    return L

while True:
    try:
        html_page = requests.get(worldmetersLink)
    except requests.exceptions.RequestException as e:
        print (e)
        continue
    bs = BeautifulSoup(html_page.content, 'html.parser')

    search = bs.select("div tbody tr td")
    start = -1
    for i in range(len(search)):
        if search[i].get_text().find(country) !=-1:
            start = i
            break
    data = []
    for i in range(1,9):
        try:
            data = data + [search[start+i].get_text()]
        except:
            data = data + ["0"]

    data= data_cleanup(data)


    message = "T {}(+{}), D {}(+{}), R {}, A (+{}){}, S {}".format(*data)

    print (label, message)
    quit()
