import requests
import csv

from Components.BearerAuth import BearerAuth

class GetData:
    def __init__(self, bearer_token, twitter_ids):
        self.bearer_token = bearer_token
        self.twitter_ids = self.create_id_search_string(twitter_ids)
    
    def get_response(self):
        return requests.get(
            'https://api.twitter.com/1.1/statuses/lookup.json?id=' + self.twitter_ids,
            auth = BearerAuth(self.bearer_token)
        )
    
    def create_id_search_string(self, part_list):
        string = ''
        count = 1
        for i in part_list:
            if count != 100:
                string = string + str(i) + ','
            else:
                string = string + str(i)
            count += 1
        return string
