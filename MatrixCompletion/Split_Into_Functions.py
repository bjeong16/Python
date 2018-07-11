# -*- coding: utf-8 -*-
import openpyxl
import requests
import json
import time
from datetime import datetime


def read_data():                         # .txt 파일에서 데이터 파싱을 진행; Movie ID 와 User ID 별로 분류

    fh = open('combined_data_1.txt')     # 파일 오픈
    movie_dict = {}                      # 영화를 사요자별로 구분한 dict
    movieID = []                         # 각 텍스트 줄의 정보를 dict 에 임시적으로 저장 (다음 루프때 갱신)
    counter = 0                          # 영화 한개당 사용자의 수; 영화 갱신시 초기화
    number_of_entries = 0
    average_dict = {}
    for line in fh:     # 라인별로 루프
        if not line.strip():             # 빈줄 제거
            continue
        if ":" in line:
            movie_list = []
            counter = 0             # 카운터 초기화
            length = line.__len__() -2
            movieID = line[:length].rstrip()            # 영화 번호만 슬라이싱
            print movieID                # 디버깅용 프린트

        else:
            counter += 1
            userid = line.partition(",")        # 자료 나누기 (인덱싱을 하기위하여)
            date = userid[2].partition(",")
            movie_data_dict = {"UserID" : userid[0], "Rating" : date[0], "Date" : date[2]}
            movie_list.append(movie_data_dict)
            movie_dict[movieID] = movie_list     # 영화에 해당하는 자료를 그 영화 키에 맞춰서 생성
    print "영화분석 완료... 유저 분석중... "
    return movie_dict

# to access rating of a certain movie in movie_dict, iterate over keys and values, and use a for loop for the value part.
# then, access by using x['Rating']

def analyze_user(movie_dict):

        userID = raw_input("Please enter the userID to look up: \n")
        index = 0
        user_dict = {}
        user_list = []
        for key, value in movie_dict.iteritems():
            index += 1
            for x in value:
                if userID == x["UserID"]:
                    print 'yes'
                    user_list.append(key)
                    user_dict[userID] = user_list
# user_dict 의 형태 : {UserID : List of movies viewed by user)
        print "유저 분석 완료... "
        return user_dict

def average_movie(movie_dict):

    average_dict = {}
    for keys, values in movie_dict.iteritems():
        total_sum = 0
        number_of_entries = 0
        for x in values:
            number_of_entries += 1
            total_sum += eval(x['Rating'])
            average = float(total_sum) / number_of_entries
            average_dict[keys] = average
# average_dict 의 형태: {movie_ID : average rating for each movie}
    print "평균값 구하는 중 ..."
    return average_dict

def baseline_rating(average, user):

    baseline = 0
    counter = 0

    for list_movie in user.values():
        for movie in list_movie:
            baseline += average[movie]
            counter += 1
            rating = baseline / counter
    print "전체의 평균값 구하는 중..."
    print rating
    return rating

# rating = 다른 사람들이 유저 x 가 본 영화들에 대해서 내린 평점

def personal_rating(user_dict, movie_dict):
    sum = 0
    counter = 0
    x = ''.join(user_dict.keys())
    for keys, values in movie_dict.iteritems():
        for y in values:
            if x == y['UserID']:
                sum += eval(y['Rating'])
                counter += 1
                user_rating = float(sum) / counter
    print "유저의 평균값 구하는 중 ..."
    print user_rating
    return user_rating

# user_rating = 유저 x 가 각 영화에 내린 평점

def getAPI(user_dict):
    print "API 에 접속중 . . ."
    movie_info = {}
    userID = "".join(user_dict.keys())
    excel_file = openpyxl.load_workbook("sampleData.xlsx")  # 6485
    sheet = excel_file['Sheet1']
    for x in user_dict[userID]:
        if eval(x) > 6485:
            x -= 1

        plusincluded = sheet['C' + str(x)].value
        if " " in plusincluded:
            plusincluded = plusincluded.replace(' ', '+')
        print str(plusincluded)
        movie_info[x] = {}
        url = 'https://api.themoviedb.org/3/search/movie?api_key=5f2f74c5dad2ce53ec50300cf1633a34&query=' + str(
            plusincluded)
        r = requests.get(url)

        genre_dict = {'28': 'Action', '12': 'Adventure', '16': 'Animation', '35': 'Comedy', '80': 'Crime',
                      '99': 'Documentary', '18': 'Drama', '10751': 'Family', '14': 'Fantasy', '36': 'History',
                      '27': 'Horror', '10402': 'Music', '9648': 'Mystery', '10749': 'Romance', '878': 'ScienceFiction',
                      '10770': 'TV Movie', '53': 'Thriller', '10752': 'War', '37': 'Western'}

        # genre_dict 는 api 에서 지칭한 장르별 ID 를 각 장르의 실제 이름으로 변환한 Dictionary 다.

        try:
            genre = r.json()['results'][0]["genre_ids"]
            genre = str(genre[0])
            genre = genre_dict[genre]
            movie_info[x]['genre'] = str(genre)
        except:
            movie_info[x]['genre'] = 'N/A'
            pass

        try:
            id = r.json()['results'][0]['id']
        except:
            pass
        urlb = 'https://api.themoviedb.org/3/movie/' + str(id) + '/credits?api_key=5f2f74c5dad2ce53ec50300cf1633a34'
        r = requests.get(urlb)

        try:
            movie_info[x]['Actor1'] = str(r.json()['cast'][0]['name'])
        except:
            movie_info[x]['Actor1'] = 'N/A'
            pass

        try:
            movie_info[x]['Actor2'] = str(r.json()['cast'][1]['name'])
        except:
            movie_info[x]['Actor2'] = 'N/A'
            pass

        try:
            movie_info[x]['Director'] = str(r.json()['crew'][0]['name'])
        except:
            movie_info[x]['Director'] = 'N/A'
            pass

        print 'done'
        print "-------------------New-Movie------------------------"
        i = 0

    return movie_info

def rating_of_movie_peraspect(user_dict, movie_info, movie_dict, aspect):

    aspect_list = []
    aspect_dict = {}
    aspect_dict_rating = {}
    user_id = "".join(user_dict.keys())

# access particular movie info with movie_info[movieID][aspect]

    for key, value in user_dict.iteritems():
        for y in value:
            i = movie_info[y][aspect]
            aspect_dict[y] = i
            # 영화마다 장르가 value 로 있는 dict, key 는 그 영화의 아이디

    movie_rating_dict = movie_rating(user_dict, movie_dict)

    for key, value in aspect_dict.iteritems():
        key_aspect = value
        sum = 0
        number = 0
        average = 0
        for x, y in aspect_dict.iteritems():
            if y == key_aspect:
                sum += eval(movie_rating_dict[x])
                number += 1
                average = float(sum) / number
                aspect_dict_rating[y] = average

    print aspect_dict_rating
    return aspect_dict_rating

#   function that generates a dictionary with the movie ID as the key and the rating of that movie as the value for a particular user
#   Parameter : List of movie IDs, movie_dict (dict that contains the rating and IDs of all movies)
#   Return Value: A dict with the movie ID as the key and the rating of the movie evaluated by the user as the value

def movie_rating(user_dict, movie_dict):
    movie_rating_dict = {}
    for keys, values in movie_dict.iteritems():
        for j in user_dict.values():
            for i in j:
                if keys == i:
                    for x in values:
                        if x['UserID'] == "".join(user_dict.keys()):
                            movie_rating_dict[keys] = x['Rating']
    print "This worked"
    print movie_rating_dict
    return movie_rating_dict


def sortPositiveReview(rating_dict):

    for keys, values in rating_dict.iteritems():
        if values == 5.0:
            print "This movie earned a 5.0 rating" + keys
        if values == 1.0:
            print "This movie earned a 1.0 rating" + keys

if __name__ == '__main__':
    clock = str(datetime.now())
    print clock
    time.sleep(2)
    print time.clock()
    movie_dict = read_data()
    average_dict = average_movie(movie_dict)
    user_dict = analyze_user(movie_dict)
    rating = baseline_rating(average_dict, user_dict)
    user_rating = personal_rating(user_dict, movie_dict)
    rating_diff = rating - user_rating

    movie_info = getAPI(user_dict)
    aspect = 'genre'
    rating_dict_genre = rating_of_movie_peraspect(user_dict, movie_info, movie_dict, aspect)
    sortPositiveReview(rating_dict_genre)
    aspect = 'Actor1'
    rating_dict_actor = rating_of_movie_peraspect(user_dict, movie_info, movie_dict, aspect)
    sortPositiveReview(rating_dict_actor)
    aspect = 'Director'
    rating_dict_director = rating_of_movie_peraspect(user_dict, movie_info, movie_dict, aspect)
    sortPositiveReview(rating_dict_director)

    # 오늘 할일: MD 파일 만들기
    # 한 영화의 평균 찾기
    # 필요한 것: 영화별의 스코어, 사람별의 스코어, 영화-사람 상성 스코어
    print clock
    print str(datetime.now())
