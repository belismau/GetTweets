# GetTweets - Version_2
Version_2: Python script to get tweets from a Twitter account

## Installation
1. Clone this repository: ```git clone https://github.com/belismau/GetTweets.git```
2. Navigate to ```cd Version_2```
3. Install [Twint](https://github.com/twintproject/twint): ```pip3 install --user --upgrade git+https://github.com/twintproject/twint.git@origin/master#egg=twint```

## Usage
1. Open ```app.py``` in VSC or any other editors, and change variable ```username``` to whatever username you want to extract tweets from.
2. Change variable ```response``` to whatever responds you want. You can find all respond alternatives in [resp_example.json](https://github.com/belismau/GetTweets/blob/main/Version_2/resp_example.json)
3. Run the app: ```python3 app.py```

## Output
There will be **x** outputs (.csv-files), where **x** is the lenght of ```response``` list.
All outputs are without **replies**.

### Example

```username = malmotown```
```
responds = [
    'tweet',
    'date',
    'link'
]
```

Output will be three csv files (all without **replies**):

- ```username_tweet.csv```: This file contains all tweets.

- ```username_date.csv```: This file contains all dates for all tweets.

- ```username_link.csv```: This file contains all links for all tweets.