# -*- coding: utf-8 -*-


def read_movie_data():
    print "영화 데이터 읽는중 ... "
    item_counter = 0
    sum_counter = 0
    print_counter = 0
    movie_dict = {}
    movie_file = open("combined_data_1.txt")
    for line in movie_file:
        if not line.strip():
            continue
        if ":" in line:
            if item_counter != 0:
                movie_dict[movieID] = average
            length = line.__len__() - 2
            movieID = line[:length].rstrip()
            item_counter = 0
            sum_counter = 0
            print_counter += 1
            print "현재 진행 상황: 영화 " + str(print_counter) + " 분석중 . . ."
        else:
            item_counter += 1
            userID = line.partition(",")
            rating = userID[2].partition(",")[0]
            sum_counter += eval(rating)
            average = float(sum_counter) / item_counter
    movie_dict[movieID] = average
    return movie_dict


def init_vector(dict):
    print "벡터 생성중 ..."
    big_list = []
    vector_list = []
    vector_list = [0.1 for x in range(20)]

    for keys in dict.iterkeys():
        big_list.append(vector_list)

    return big_list


def read_user_data():
    print("유저 데이터 분석중 . . .")
    print_counter = 0
    user_list = []
    user_dict = {}
    user_file = open("combined_data_1.txt")
    for line in user_file:
        if not line.strip():
            continue

        if ":" in line:
            print_counter += 1
            print "영화 " + str(print_counter) + " 분석중 . . ."
            length = line.__len__() - 2
            movieID = line[:length].rstrip()

        else:
            temp_dict = {}
            userID = line.partition(",")
            rating = userID[2].partition(",")[0]
            temp_dict["userID"] = userID[0]
            temp_dict["rating"] = rating
            temp_dict["movieID"] = movieID
            user_list.append(temp_dict)
    return user_list


def user_init_vector(user_ID, vector_list):
    individual_dict = {}
    individual_list = [0.1] * 30
    individual_dict[user_ID] = individual_list
    vector_list.append(individual_dict)
    return vector_list


def getOffset(movie_dict, x, user_dict):

    sum = 0
    count = 0

    for y in user_dict:
        if x["userID"] == y["userID"]:
            sum = eval(y['rating']) - movie_dict[y["movieID"]]
            count += 1
    offset = float(sum) / count
    return offset

def trainFeature(movieID, userID, rating, avgRating, offsetRating, userVector, movieVector, index):
    for epoch in range(120):
        lrate = 0.001
        err = lrate * (eval(rating) - (avgRating - offsetRating))
        for x in userVector:
            if x.keys() == userID:
                break
        uv = x[userID][index]
        x[userID][index] += err * movieVector[eval(movieID) -1][index]
        movieVector[eval(movieID) -1][index] += uv * err
        print "The value of aspect " + str(index) + " for student " + str(userID) + ' is ' + str(x[userID][index])
        print "Currently evaluating movie " + str(movieID) + " " + str(movieVector[eval(movieID) -1][index])

if __name__ == '__main__':

    movie_dict = read_movie_data()
    movie_vector = init_vector(movie_dict)
    user_dict = read_user_data()
    already_used = []
    user_vector_list = []

    for y in range(20):
        for x in user_dict:
            if x["userID"] not in already_used:
                already_used.append(x["userID"])
                offset = getOffset(movie_dict, x, user_dict)
                user_vector_list = user_init_vector(x["userID"], user_vector_list)
                trainFeature(x["movieID"], x["userID"], x["rating"], movie_dict[x["movieID"]], offset, user_vector_list, movie_vector, y)
        already_used = []

    print "작업 완료..."
    print movie_dict
    print movie_vector
    print user_vector_list

cd