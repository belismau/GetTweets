import csv

class AddTweetsToFile:
    def __init__(self, data, name):
        self.data = data
        self.name = name
        self.add_to_file()

    def add_to_file(self):
        x = 0
        for tweet in self.data:
            with open('@' + self.name + '-tweets-temp.csv', 'a', encoding='utf-8') as f1:
                wr = csv.writer(f1, lineterminator = '\n\n--\n\n')
                wr.writerow([self.data[x]["text"]])
            x += 1