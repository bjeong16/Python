# -*- coding: utf-8 -*-


def read_data():                         # .txt 파일에서 데이터 파싱을 진행; Movie ID 와 User ID 별로 분류

    fh = open("Example")                 # 파일 오픈
    movie_dict = {}                      # 영화를 사요자별로 구분한 dict
    movieID = []                         # 각 텍스트 줄의 정보를 dict 에 임시적으로 저장 (다음 루프때 갱신)
    counter = 0                          # 영화 한개당 사용자의 수; 영화 갱신시 초기화
    movie_data_list = []
    for line in fh:     # 라인별로 루프
        if not line.strip():             # 빈줄 제거
            continue
        if ":" in line:
            counter = 0             # 카운터 초기화
            length = line.__len__() -2
            movieID = line[:length].rstrip()            # 영화 번호만 슬라이싱
            print movieID                # 디버깅용 프린트

        else:
            counter += 1
            userid = line.partition(",")        # 자료 나누기 (인덱싱을 하기위하여)
            date = userid[2].partition(",")
            movie_data_dict = {"UserID" : userid[0], "Rating" : date[0], "Date" : date[2]}
            movie_dict["MovieID" + movieID + " - " + str(counter)] = movie_data_dict     # 영화에 해당하는 자료를 그 영화 키에 맞춰서 생성
            movie_data_list.append(movie_data_dict["UserID"])

    print movie_dict
    # 영화별 분류 종료; 유저별 분류 시작

    id_dict = {}  # movie_dict 의 유저 버전. 아이디 번호가 key, 영화가 value 이다
    id_list = []  # 각 아이디당의 영화를 리스트로 정리해놓은 변수
    copy_movie_dict = movie_dict # movie_dict 에 있는 자료를 수정할수있게 만든 copy
    mult_id_list = []
    sing_id_list = []
    sing_list = []
    mult_list = []
    y = 1
    x = 1
    print movie_dict["MovieID" + str(x) + " - " + str(y)]['UserID']

    print movie_data_list.count(movie_data_list[1])
    print movie_data_list

    for x in movie_data_list:
        if movie_data_list.count(x) > 1:
            if x not in mult_id_list:
                mult_id_list.append(x)
        if movie_data_list.count(x) == 1:
            if x not in sing_id_list:
                sing_id_list.append(x)

    print "The multiple id list is " + str(mult_id_list)
    print "The short id list is" + str(sing_id_list)
    i = 1

    for key, value in movie_dict.iteritems():
        for item in sing_id_list:
            if value["UserID"] == item:
                id_dict[item] = ({"MovieID" : key, "Rating" : value['Rating'], "Date" : value['Date']})

    for item in mult_id_list:
        for key, value in movie_dict.iteritems():
            if value["UserID"] == item:
                id_dict[item + "-" + str(i)] = ({"MovieID": key, "Rating": value['Rating'], "Date": value['Date']})
                i += 1
        i = 1
    print id_dict
if __name__ == '__main__':
    read_data()