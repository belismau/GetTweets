import csv

class RemoveReplies:
    def __init__(self, filename):
        self.filename = filename
        self.remove_replies()
    
    def remove_replies(self):
        with open('@' + self.filename + '-tweets-temp.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for row in csv_reader:
                for string in row:

                    if string == '--':
                        break
                    
                    if string[0] == "@":
                        break

                    if ' /' in string:
                        break

                    with open('@' + self.filename + '-tweets.csv', 'a', encoding='utf-8') as f1:
                        wr = csv.writer(f1, lineterminator = '\n')
                        wr.writerow([string])