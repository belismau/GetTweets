import json
import csv

class GetContent:
    def __init__(self, filename, responds):
        self.filename = filename
        self.responds = responds
        self.get_content()
    
    def get_data_from_json(self):
        f = open(self.filename + '.json')
        return json.load(f)

    def get_content(self):
        data = self.get_data_from_json()

        for line in data:
            cur_tweet = str(line['tweet'])
            if cur_tweet[0] != '@': # and ' /' not in cur_tweet:
                filepath = self.filename + '/'
                for resp in self.responds:
                    with open(filepath + self.filename + '_' + resp + '.csv', 'a', encoding='utf-8') as f1:
                        wr = csv.writer(f1, lineterminator = '\n')
                        wr.writerow([line[resp]])