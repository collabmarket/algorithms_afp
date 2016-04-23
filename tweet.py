import tweepy
import time
from datetime import datetime

print "[INFO]--" + datetime.now().strftime('%Y-%M-%d %H:%M:%S') + "--" + "tweet" + "--" + "INIT"

with open('key.txt', 'rU') as f:
    token = [line.rstrip() for line in f]

consumer_key = token[0]
consumer_secret = token[1]
access_token = token[2]
access_token_secret = token[3]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
print "[CHECK]--" + "Ready: " + api.me().name

#tweet = api.update_status(status='Updating via Tweepy!')

afps = ['CUPRUM', 'HABITAT', 'MODELO']
fecha = datetime.now().strftime('%Y-%M-%d')

for afp in afps:
    msg = ('Estrategia afp %s fecha %s\n'
       'https://github.com/collabmarket/algorithms_afp'%(afp,fecha)
      )
    tweet = api.update_with_media('result/A-E_%s.png'%afp, status=msg)
    time.sleep(20)

msg = 'Riesgo Sistemico fecha %s'%(fecha)
tweet = api.update_with_media('result/SystemicRisk.png', status=msg)

print "[INFO]--" + datetime.now().strftime('%Y-%M-%d %H:%M:%S') + "--" + "tweet" + "--" + "DONE"
