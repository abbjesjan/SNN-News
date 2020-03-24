c_k = '0KKsFA0k2rQjvzuxQbiXwfkLj'
c_s = 'qgA1L71Yv5UQae9fHl7IGMGm5LA2FmuMC1sFpJzMCN0BZoEmTe'
a_k = '1220610275268866048-sO4AdHaY5QUgd4uazcKknemaTtX1ri'
a_s = '23NotLjOpW0QnHBby7FxlOQsT6KHILpkU7R2oNBDLlpTn'


import gpt_2_simple as gpt2
import tweepy
import time
import random
import tarfile
import requests
import os
from datetime import datetime, timedelta

filepath="checkpoint_runstart.tar"
googefileid= "1v9T87wh48XTS66zvhKi1R4IP5dKy5y6g"

def extract():
    """Copies the checkpoint folder from a mounted Google Drive."""
    with tarfile.open(filepath, 'r') as tar:
        tar.extractall()
    os.remove(filepath)
    print("File",filepath, "Removed!")


auth = tweepy.OAuthHandler(c_k,c_s)
auth.set_access_token(a_k,a_s)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
    
except:
    print("Error during authentication")



def download_file_from_google_drive(id, destination):
    def get_confirm_token(response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value

        return None

    def save_response_content(response, destination):
        CHUNK_SIZE = 32768

        with open(destination, "wb") as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)

    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)


download_file_from_google_drive(googefileid,filepath)
extract()
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name='runstart')

def createtweet(prefix):
    temp= random.randint(7,9)/10
    print(temp)
    textlength=  random.randint(35,200-len(prefix))
    print(textlength)
    text= gpt2.generate(sess,
            run_name='runstart',
            length= textlength,
            temperature=temp,
            top_k=40,
            #prefix=prefix,
            nsamples=1,
            batch_size=1,
            return_as_list = True
            )
            
    text= text[0]
    print(len(text),text)
    text= text[0:280-len(prefix)]
    text = text.splitlines()
    new_text = ""
    for line in text:
      if line != "\n":
        new_text += line
      else:
        break
    text = new_text
    return text

def post_tweet(now, prefixes):
    try:
        prefix = ""#prefixes[random.randint(0, len(prefixes))]
        text= createtweet(prefix)
        print(len(text),text)
        api.update_status(text)
        print('Completed posting tweet at ', now)
    except:
        print('tweet failed')

while True:    
    now = datetime.now()
    prefixes = [""]
    post_tweet(now, prefixes)
    sleeptime= random.randint(3000,7000)
    now_plus = now + timedelta(seconds=sleeptime)
    print("Next tweet will be in ",str(timedelta(seconds=sleeptime)), " at " ,now_plus )
    time.sleep(sleeptime)