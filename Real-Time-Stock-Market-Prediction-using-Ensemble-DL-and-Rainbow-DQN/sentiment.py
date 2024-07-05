""" install required packages """
!pip install requests beautifulsoup4 vaderSentiment


""" import the libraries """
import requests
from bs4 import BeautifulSoup
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import matplotlib.pyplot as plt

""" Setting up inline plotting for Jupyter notebooks """
%matplotlib inline


"""This function, get_headers, returns a dictionary containing HTTP headers
that can be used to make a web request, particularly when interacting with
a website that requires specific headers for the request to be accepted and processed correctly """

def get_headers():
    return {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-IN,en-US;q=0.9,en;q=0.8",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://inshorts.com",
        "referer": "https://inshorts.com/en/read/",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }


""" scrap news from inshorts """

ef print_headlines(response_text):
    news_headlines = []
    soup = BeautifulSoup(response_text, 'lxml')
    headlines = soup.find_all(attrs={"itemprop": "headline"})
    for headline in headlines:
        news_headlines.append(headline.text)
    return news_headlines

def news2sentiment():
    url = 'https://inshorts.com/en/read'
    response = requests.get(url)
    news_headlines = print_headlines(response.text)

    # get more news
    url = 'https://inshorts.com/en/ajax/more_news'
    news_offset = "apwuhnrm-1"

    for i in range(0, 3):
        response = requests.post(url, data={"category": "", "news_offset": news_offset}, headers=get_headers())
        
        # Check if the response is valid and contains data
        if response.status_code == 200 and response.text: 
            try:
                response_json = json.loads(response.text)
                more_headlines = print_headlines(response_json["html"])
                news_headlines.extend(more_headlines)
                news_offset = response_json["min_news_id"]
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Error processing response for iteration {i}: {e}")
                # Handle the error, e.g., skip this iteration or break the loop
        else:
            print(f"Request failed for iteration {i} with status code: {response.status_code}")
            # Handle the failed request, e.g., retry or break the loop

    news_headlines = news_headlines[:100]  # Get the top 100 headlines
    news_headlines = news_headlines[::-1]  # Reverse the order to get the latest headlines first
    return news_headlines

news_headlines = news2sentiment()
print(news_headlines)

""" perform sentiment analysis """ 

# Assuming 'news_headlines' is the list you provided
news_headlines = ["LS Speaker Birla amends oath-taking rules after 'Jai Palestine', 'Jai Hindu Rashtra' slogans", 
                 'PM Modi meets T20 World Cup 2024-winning Team India, poses with trophy', 
                 '10 bridges collapse in 15 days in Bihar', 
                 "Team India's open-top bus stuck in traffic before victory parade in Mumbai", 
                 "Team India's open-top bus victory parade in Mumbai begins, first visuals surface"]

# Create a SentimentIntensityAnalyzer object. 
sid_obj = SentimentIntensityAnalyzer() 
scores = []  # Initialize scores list
for i in news_headlines:
    # polarity_scores method of SentimentIntensityAnalyzer 
    # object gives a sentiment dictionary. 
    # which contains pos, neg, neu, and compound scores. 
    sentiment_dict = sid_obj.polarity_scores(i)
    scores.append(sentiment_dict['compound'])

print(scores)  # Print the calculated sentiment scores


# Create a DataFrame
df = pd.DataFrame({'Headline': news_headlines, 'Sentiment Score': scores})

print(df)
