import tweepy
import os 
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the variables
consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")



client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)


client.create_tweet(text="Hello from the API")
print("Tweet posted successfully!")


