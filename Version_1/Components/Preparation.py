import snscrape.modules
import csv

class Preparation:
    def __init__(self, username):
        self.username = username
        self.tweets = snscrape.modules.twitter.TwitterUserScraper(username=self.username)
    
    def create_id_list(self):
        all_id_list = []

        for i in self.tweets.get_items():
            tweet_id = self.get_id(str(i))
            all_id_list.append(int(tweet_id))

            with open('@' + self.username + '-id.csv', 'a', encoding='utf-8') as f:
                wr = csv.writer(f, lineterminator = '\n')
                wr.writerow([tweet_id])
        
        return self.divide_list(all_id_list)
    
    def divide_list(self, all_id_list):
        return [
            all_id_list[x:x + 100] 
            for x in range(
                0, 
                len(all_id_list), 
                100
            )
        ]
    
    def get_id(self, link):
        cut = link.find('/status/')
        newer = cut + 8
        return link[newer:]
