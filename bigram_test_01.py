import csv

bidic = {} # bigram dictioary
count = 0
with open('./gitignored_files/taiwanese_song_info.csv', 'r') as data:
# with open('./gitignored_files/song_info.csv', 'r') as data:
    reader = csv.reader(data)
    song_dictionary = list(reader)


with open('./gitignored_files/taiwanese_song_bigram.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    # print(song_dictionary[row][0])
    for i in range(1, len(song_dictionary)) :
        word = song_dictionary[i][2].replace(" ", "")
        for j in range(0,len(word)-1):
            bi = word[j:j+2]
            # print(bi)
            if bi in bidic : # existed in bidic
                bidic[bi][0] = bidic[bi][0] + 1
            else : # does not exist in bidic
                bidic[bi] = [1,0]
            count+=1

    # write bigram dictionary into file
    writer.writerow(["vocabulary","counts","chance"])
    for key,value in bidic.items() :
        value[1] = value[0] / count
        writer.writerow([key, value[0], value[1]])
