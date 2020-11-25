from Components.FixJSON import FixJSON
from Components.GetContent import GetContent

import twint
import os

# Choose between several responds, such as 
# 'tweet', 'date', 'created_at', 'id', 'time', 'link', etc.

username = 'goteborgcom'
responds = [
    'tweet',
    'date',
    'link'
]

# Configure
c = twint.Config()
c.Username = username
c.Store_json = True
c.Output = username + '.json'

# Run
twint.run.Search(c)

# Fixing json file and filtering out replies.
os.mkdir(username)

FixJSON(username)
GetContent(username, responds)