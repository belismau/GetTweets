from Components.GetData import GetData
from Components.AddTweetsToFile import AddTweetsToFile
from Components.Preparation import Preparation
from Components.RemoveReplies import RemoveReplies
from Components.get_bearer import get_bearer

import json

# Getting my bearer token from codes.txt
bearer_token = get_bearer()
username = 'malmotown'

# Preparing for the request
tweets = Preparation(username)
tweets_list = tweets.create_id_list()

# Go through every list in our nested list
# Every list has 100 elements, that's the max limit of id:s per requests
for list_part in tweets_list:
    response = GetData(bearer_token, list_part).get_response()
    data = json.loads(response.text)
    AddTweetsToFile(data, username)

RemoveReplies(username)
