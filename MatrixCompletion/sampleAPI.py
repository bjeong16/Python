# -*-coding: utf-8 -*-
import requests
import json
import openpyxl
import string

if __name__ == '__main__':
    excel_file = openpyxl.load_workbook("sampleData.xlsx")
    movie_list = []
    sheet = excel_file['Sheet1']
    cell_range = sheet['C1':'C17770']
    counter = 0
    for row in cell_range:
        for cell in row:
            plusincluded = str(cell.value)
            plusincluded = plusincluded.replace(' ', '+')
            movie_list.append(plusincluded)
            counter += 1
    url = 'https://api.themoviedb.org/3/search/movie?api_key=5f2f74c5dad2ce53ec50300cf1633a34&query=Tin+Cup'
    r = requests.get(url)
    print r
    id = r.json()['results'][0]['id']
    urlb = 'https://api.themoviedb.org/3/movie/' + str(id) + '/credits?api_key=5f2f74c5dad2ce53ec50300cf1633a34'
    r = requests.get(urlb)
    print r.json()['cast'][0]['name']
    print r.json()['cast'][1]['name']
    print r.json()['crew'][0]['name']