# GetTweets - Version_1
Version_1: Python script to get tweets from a Twitter account

## Installation
1. Clone this repository: ```git clone https://github.com/belismau/GetTweets.git```
2. Navigate to ```cd Version_1```
3. Install [Snscrape](https://github.com/JustAnotherArchivist/snscrape): ```pip3 install snscrape```

## Usage
1. Open ```app.py``` in VSC or any other editors, and change variable ```username``` to whatever username you want to extract tweets from.
2. Change variable ```bearer_token``` to your own bearer token. Make sure it's a string.
3. Run the app: ```python3 app.py```

## Output
There will be 5 outputs (.csv-files), with and without **replies**:

- ```@username-id```: This file contains ID:s of all tweets **(with replies)**.

- ```@username-time-temp.csv```: This file contains date of all tweets **(with replies)**.

- ```@username-time.csv```: This file contains date of all tweets **(without replies)**.

- ```@username-tweets-temp.csv```: This file contains all tweets **(with replies)**.

- ```@username-tweets.csv```: This file contains all tweets **(without replies)**.