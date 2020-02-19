
import csv
import re
bidic = {} # bigram dictioary
count = 0
candidates = []
song_dictionary = list()
def read_csv():
    global song_dictionary
    with open('./gitignored_files/taiwanese_song_info.csv', 'r') as data:
    # with open('./gitignored_files/song_info.csv', 'r') as data:
        reader = csv.reader(data)
        song_dictionary = list(reader)
        # print(song_dictionary)
    return

def create_dict():
    global song_dictionary, count
    with open('./gitignored_files/taiwanese_song_bigram_2.csv', 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for i in range(1, len(song_dictionary)) :
            to_be_replaced = "().?!,-…（）'【】．。"
            alphebat = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            word = song_dictionary[i][2]
            for symbol in to_be_replaced :
                word = word.replace(symbol, " ")
            for alpha in alphebat :
                word = word.replace(alpha, "")
            word = word.replace("  ", " ")
            word = "@"+word+"@"
            for j in range(0,len(word)-1):
                bi = word[j:j+2]
                if bi in bidic : # existed in bidic
                    bidic[bi][0].append(i)
                else : # does not exist in bidic
                    bidic[bi] = [[i],0]
                    # print(bidic[bi])
                count+=1

        # write bigram dictionary into file
        writer.writerow(["bigram","counts","chance"])
        # {'bigram' = [[list of id], chance]}
        for key,value in bidic.items() :
            # print(len(value[0]))
            writer.writerow([key, len(value[0]), len(value[0])/count])
    return

def search(input):
    global song_dictionary
    input = "@"+input+"@"
    input_bidic = []
    result = "no result"
    for i in range(0,len(input)-1):
        input_bidic.append(input[i:i+2])
    for i in range(0,len(input_bidic)):
        if bidic[input_bidic[i]] :
            for j in range(0,len(bidic[input_bidic[i]][0])):
                candidates.append(bidic[input_bidic[i]][0][j])
    most_possible_results = most_frequent(candidates)
    # print(most_possible_results)
    return most_possible_results

def most_frequent(List) :
    count = 0
    id = List[0]
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency > count):
            count = curr_frequency
            id = i
    candidate_list = []
    for i in List:
        if List.count(i) == List.count(id) and i not in candidate_list :
            candidate_list.append(i)
    print("Most possible songs are : ")
    for i in range(0,len(candidate_list)):
        print(song_dictionary[candidate_list[i]][2])
    return candidate_list

def init():
    read_csv()
    create_dict()

if __name__ == '__main__' :
    init()
    search("春秋大")
