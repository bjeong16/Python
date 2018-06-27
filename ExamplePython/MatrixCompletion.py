# -*- Coding: UTF-8 -*-
import re

def ReadData():
    fh = open("combined_data_2.txt")
    user_list = []
    movie_list = []
    movie_dict = {}
    user_movie_list = []
    user_movie_dict = dict()
    comp_list = []
    x = 0
    y = 0
    z = 0
    repeat = 1
    smallest_id = 5000000
    largest_id = 0
    mark = 0
    index = 0
    a = 0
    movieID = []
    for line in fh:
        if z > 100000:
            break
        if not line.strip():
            continue
        for word in line:
            if word == ':':
                mark = 1
                movieID = str(line[:index].rstrip())

            else:
                index += 1

        if mark == 1:
            y += 1
            x = 1
            movie_list.append(movie_dict)
            mark = 0
                                                # my_dict = {MovieID : Value, {PersonID1 : Value, Rating: Value, Date: Value} , {...}}
        else:
            repeat = 1
            ID_line = line.partition(",")
            Date_line = ID_line[2].partition(",")
            ID_dict = {"PersonID" : ID_line[0], "Rating" : Date_line[0], "Date" : Date_line[2]}
            user_list.append([ID_line[0], movieID])
            for s in user_list:
                s = list()
                s.append(movieID)

                if ID_line[0] in user_movie_dict.keys():
                    if repeat == 1:
                        marker = 1
                        user_movie_dict[ID_line[0]].append(s)
                        repeat = 0
                else:
                    marker = 0
                    a += 1
            if marker == 0:
                user_movie_dict[ID_line[0]] = s




            movie_dict["MovieID" + str(y) + "-" + str(x)] = ID_dict
            x += 1

            z += 1
            print z
    print user_movie_dict





if __name__ == '__main__':

    ReadData()
    print "end"