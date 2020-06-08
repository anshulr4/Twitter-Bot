import tweepy as tp
import time
import os

consumer_key = 'w7eCB6f7oJV4VTkIWom8W7y4b'
consumer_secret = 'xzXsuxhQ4teEVYKWw5Srdw2OA1nxcOpXs73yCT5xvOPJtayqiu'
access_token = '1203865049187504128-s6y3qR6HFXdcBIYg6xJQQKFpJw45Ku'
access_secret = 'd4iTBIjL9VetiJEQiye7spJjf5YZH2KvjcQNZAcmdrlKU'
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

os.chdir('burritos')
for pic in os.listdir('.'):
	api.update_with_media(pic, '#Yum!')
	time.sleep(5)