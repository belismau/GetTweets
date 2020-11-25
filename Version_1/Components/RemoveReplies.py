import csv

class RemoveReplies:
    def __init__(self, filename):
        self.filename = filename
        self.remove_replies_tweets()

    def remove_replies_time(self, temp_list):
        with open('@' + self.filename + '-time-temp.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            
            nr = -1
            for row in csv_reader:
                for string in row:
                    nr += 1

                    if nr in temp_list:
                        with open('@' + self.filename + '-time.csv', 'a', encoding='utf-8') as f1:
                            wr = csv.writer(f1, lineterminator = '\n')
                            wr.writerow([string])
    
    def remove_replies_tweets(self):
        with open('@' + self.filename + '-tweets-temp.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            temp_list = []

            nr = -1
            for row in csv_reader:
                for string in row:
                    nr += 1

                    if string == '--':
                        break
                    
                    if string[0] == "@":
                        break

                    if ' /' in string:
                        break

                    with open('@' + self.filename + '-tweets.csv', 'a', encoding='utf-8') as f1:
                        wr = csv.writer(f1, lineterminator = '\n')
                        wr.writerow([string])

                    temp_list.append(nr)

        self.remove_replies_time(temp_list)