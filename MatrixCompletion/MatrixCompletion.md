Matrix Completion for the Netflix Data Set

프로젝트 목표:

	Netflix db 를 자료로 해서 영화 평점 Predictor Algorithm 을 구현하면서 Matrix Completion Algorithm

	에 대해서 이해하고 코딩하기.



바탕:

	2009 년에 Netflix 라는 미국 소재의 드라마 및 영화 스트리밍 기업은 방대한 양의 데이터를 제공하면서 

	본인들의 Predictor Algorithm 보다 10% 향상된 성능의 알고리즘을 개발하는 팀에게 100만 달러를 상금

	으로 약속하였다. 이 Predictor Algorithm 의 목표는 특정 유저가 몇몇의 영화에대한 평점을 분석하여 그 유저

	들이다른 영화에 매긴 평점을 예측하는 것이다. 



Matrix Completion 의 기본:

	Matrix Completion 은 Big Data Optimization 의 한 종류이다. 기본적으로 각 항목 (Netflix 의 경우 소비자 

	항목, 영화 항목) 을 각각 행과 열로 분류한후, 그 행과 열에 해당하는 자리에 데이터값을 넣는다. 

	예) "지민" 이 "Inception" 이라는 영화에 대해서 4점 이라는 평점을 매기면 "지민" 에 해당되는 행에서 

	"Inception" 이라는 열을 찾아서 그 자리에 "4" 를 넣는다. 

	

	주어진 모든 데이터를 이와 같이 채운후에 Data Optimization 이 진행된다. 



프로그램 구성

.txt 파일에서 parsing 으로 데이터 수집

	Netflix 에서 제공된 데이타는 .txt 파일로 정리되어있다.  형태는 

		MOVIEID1:

		CUSTOMERID1, RATING, DATE-OF-RATING 

		CUSTOMERIDX, RATING, DATE-OF-RATING

		...

		MOVIEID2:

		CUSTOMERID1, RATING, DATE-OF-RATING

		CUSTOMERIDX, RATING, DATE-OF-RATING

		... 

	식 으로 되어있다.



1) 모든 데이터를 영화별로 분류.

		예) 영화 한개당 한개의 리스트를 생성. 영화 ID 는 순차적으로 나열되있으므로 마지막 CUSTOMERID 

		      에서 새로운 리스트 생성.

	

	모든 데이터는 .txt 파일에 나열되있으므로 open() 함수를 써야한다. open('파일명') 은 '파일명' 안에 

	들어있는 모든 데이터를 문자열 형태로 변환시켜서 지정된 변수안에 대입시킨다. 그 후에 for 루프로 

	모든 줄을 분석하여 movie_dict 라는 dictionary 형태의 변수에 자료를 정리한다. 

		 

		**movie_dict 의 구조   :           [{movieID : {"UserID" : x, "Rating" : y, "Date" : z}} , {movieID2 : {..}} ..]**

	

	movie_dict 는 Netflix 에서 제공하는 모든 데이터를 보유하고 있다. 앞으로 이 프로그램에서 데이터를 접근

	해야 할때에는 Netlix 의 .txt 파일이 아닌 movie_dict 에서 가지고 오면 된다.

	

	프로그램에서 movie_dict 를 생성, 작업, 그리고 반환하는 함수는 read_data() 명의 함수이다. 



	

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

	

	read_data() 함수는 인자값이 없고, movie_dict 를 리턴한다. 



유저 데이터 수집



	.txt 파일에서의 데이터가 나열되있는 형식상 movie_dict 와 비슷한 형태로 유저마다 데이터를 정리하기

	에는 효율적이지 않다. 영화의 수가 유저의 수보다 훨씬 적기 때문이다. 또한, .txt 파일의 데이터 형식상 

	한 영화에 대한 데이터는 중복되지 않는다. 하지만 한 유저에 대한 정보는 .txt 파일 어디에서 등장할지

	모르기 때문에 모든 유저의 정보를 프로그램 내 변수에 저장하기에는 효율적이지 않다. 그러므로 유저는

	user ID 를 console 창에서 지정하면 그 유저에 대한 정보만 dict 에 구축하는 형태로 데이터 수집을 했다. 



	이 작업을 위하여 analyze_user 이라는 함수를 썼다. analyze_user 은 movie_dict 를 인자값으로 받은후, 

	movie_dict 의 "UserID" key 와 console 창에서 입력 받은 userID 를 비교한 후, 그 값이 일치하면 user_dict 

	라는 dictionary 에 ID 를 key 로, 영화 ID 를 value 로 저장한다. 



		**user_dict 의 구조        :            {userID :  [movie ID1, movieID2 .... ]}**

	

	analyze_user 의 코드는 

	

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

	위 코드가 실행된 뒤에 analyze_user 은 user_dict 를 리턴한다. 



영화의 평균 평점 찾기

	average_movie() 함수는 각 영화의 평균 평점을 찾는 함수이다. 모든 데이터가 들어가 있는 movie_dict{} 

	dictionary 를 인자값으로 가져온후, 영화당 각 사용자의 평점을 가지고 온 후, 평균값을 낸다. 그 후,

	영화의 아이디를 key, 그리고 영화의 평균 평점을 value 로한 average_dict{} 딕셔너리를 생성한다. 



			**average_dict 의 구조      :              {movieID : 해당 movieID 의 평균 평점}**



	average_movie 의 코드

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
    

	main() 으로 average_dict 를 리턴한다. 



유저의 평점 취향 (vs 다른 유저의 평점)

	baseline_rating() 함수는 한 유저의 평점 기준을 알기 위해서 만든 함수다. 장르, 주연배우 등 을 고려하지

	않고 이 유저가 전체적으로 평점을 후하게 주는 편인지, 전체적으로 평점을 낮게 주는지를 분석해준다. 

	

	인자값으로는 average_dict 와 user_dict 를 가지고온다. user_dict 는 해당 유저가 평점을 내린 모든 영화의 

	아이디가 나와 있고, average_dict 는 모든 영화에 대한 평균 평점이 value 값으로 있다. baseline_rating 함수

	는 이 user_dict 에 나열되있는 영화 아이디를 average_dict 의 key 로 사용하여 유저 x 가 본 영화들의

	전체 평균 평점을 리턴한다. 



	

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

	

	baseline_rating() 이 실행된후 personal_rating() 함수가 실행된다. 이 personal_rating() 함수는 유저가 

	본 영화마다 유저가 내린 평점의 평균값을 리턴한다. 인자값으로는 user_dict 와 movie_dict 값을 받고, 

	user_dict 에 나열되어 있는 영화를 movie_dict 의 큰 key 로, userID 를 작은 key 로 써서 평점을 가져온다. 



				참고: movie_dict 는 dictionary in dictionary 이다.여기서 "큰" key 는 전체 dictionary 의 

					 "key" 를 말하는것이고, "작은" key 는 큰 dict 에 속해있는 dict 의 key 를 명시한다. 

	

	personal_rating() 의 코드: 

		

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

	

	baseline_rating() 하고 personal_rating() 가 모두 진행된 후에 두 값의 차이를 비교하면 유저 x 의 

	평점 성향이 나온다. 이 값이 음수이면 유저는 후하게 평점을 내리는 성향이고, 양수이면 유저는 

	평점을 낮게 주는 성향인 것이다. 최종적으로 유저 x 가 영화 y 에 대하여 어떤 평점을 내릴지 

	예상 하기 위해서는 이 조건을 고려해야한다. main() 에는 이 값을 rating_diff 라는 변수에 저장했다. 



API 접속



	Netflix 에서는 영화의 아이디, 작품명, 날짜 밖에 제공하지 않는다. 텍스트 파일에서는 영화의 아이디

	만을 제공하고, .csv 파일에서 아이디별로 작품명과 개봉 날짜에 대한 정보를 준다. 하지만 recommender 

	system 을 구축하기 위해서는 모자른 자료이다. 기본적으로 영화의 장르, 주연배우, 감독 등 정보를 알아야지

	각 유저의 취향을 정확하게 분석할 수 있다. Netflix API 는 서비스가 중단된 상태라 imdb 

	(International movie DataBase) 의 API 를 썼다. 



	imdb API 를 접속 하는데 필요한 URL 은 

	'https://api.themoviedb.org/3/search/movie?api_key=5f2f74c5dad2ce53ec50300cf1633a34&query='

	이다. 링크의 마지막 부분인 &query= 에 영화 이름을 추가로 붙이면 그 영화에 대한 정보가 json 파일의 형태

	로 변수에 입력된다. 

	

	예) 제임스 카메론의 "Titanic" 에대한 정보를 가지고 오기 위해서는 

	'https://api.themoviedb.org/3/search/movie?api_key=5f2f74c5dad2ce53ec50300cf1633a34&query=Titanic

	로 URL 을 저장하면 된다. 

	

		*참고 : 영화 제목에 빈칸이 있으면 빈칸을 "+" 로 바꿔야 한다*



영화별 장르, 감독, 주연배우 정보 가져오기



	getAPI() 함수는 "API 접속" 부분의 내용을 함수로 실현시키고, 각 영화의 정보가 들어있는 dict{} 형태의

	의 변수를 생성한다. 인자값으로는 user_dict 를 가지고 온다. 

	

	API 에 접속하기 이전에 user_dict 에 있는 영화 ID 를 통해서 각 영화의 실제 작품명을 알아야한다. 

	Netflix 에서 주어진 .csv 파일을 통해서 영화ID 별 작품명을 가지고 온후에 API 에 접속한다. 

	Python 프로그램에서 API 에 접속하기 위해서는 requests.get() 함수를 사용한다. 

	requests.get 함수를 사용하여 imdb API 에 접속한 후, json file 의 형태로 데이터가

	돌아오면 인덱싱을 통해서 원하는 값을 추출한다. 



	API 가 리턴하는 .json 파일의 구조

    {"page":1,"total_results":101,"total_pages":6,"results":[{"vote_count":10695,"id":597,"video":false,"vote_average":7.7,"title":"Titanic","popularity":24.547,"poster_path":"\/kHXEpyfl6zqn8a6YuozZUujufXf.jpg","original_language":"en","original_title":"Titanic","genre_ids":[18,10749,53],"backdrop_path":"\/vFUI5obFtx4IdhP6k8Om5ezHTrk.jpg","adult":false,"overview":"84 years later, a 101-year-old woman named Rose DeWitt Bukater tells the story to her granddaughter Lizzy Calvert, Brock Lovett, Lewis Bodine, Bobby Buell and Anatoly Mikailavich on the Keldysh about her life set in April 10th 1912, on a ship called Titanic when young Rose boards the departing ship with the upper-class passengers and her mother, Ruth DeWitt Bukater, and her fiancé, Caledon Hockley. Meanwhile, a drifter and artist named Jack Dawson and his best friend Fabrizio De Rossi win third-class tickets to the ship in a game. And she explains the whole story from departure until the death of Titanic on its first and last voyage April 15th, 1912 at 2:20 in the morning.","release_date":"1997-11-18"},

	... 

	...

	...
