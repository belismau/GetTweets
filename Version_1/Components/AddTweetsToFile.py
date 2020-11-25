import csv

class AddTweetsToFile:
    def __init__(self, data, name):
        self.data = data
        self.name = name
        self.add_to_file_tweets()
        self.add_to_file_time()

    def add_to_file_tweets(self):
        x = 0
        for tweet in self.data:
            with open('@' + self.name + '-tweets-temp.csv', 'a', encoding='utf-8') as f1:
                wr = csv.writer(f1, lineterminator = '\n')
                wr.writerow([self.data[x]["text"]])
            x += 1
    
    def add_to_file_time(self):
        x = 0
        for tweet in self.data:
            with open('@' + self.name + '-time-temp.csv', 'a', encoding='utf-8') as f1:
                wr = csv.writer(f1, lineterminator = '\n')
                wr.writerow([self.change_format(self.data[x]["created_at"])])
            x += 1
    
    def change_format(self, mytime):
        all_months = {
            'Jan': '01',
            'Feb': '02',
            'Mar': '03',
            'Apr': '04',
            'May': '05',
            'Jun': '06',
            'Jul': '07',
            'Aug': '08',
            'Sep': '09',
            'Oct': '10',
            'Nov': '11',
            'Dec': '12',
        }

        year = mytime[-4:]
        month = all_months[mytime[4:7]]
        day = mytime[8:10]

        return (year + '-' + month + '-' + day)
