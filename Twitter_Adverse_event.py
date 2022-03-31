from requests_oauthlib import OAuth1Session
import json



#API認証
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

#OAuth認証
auth = OAuth1Session(consumer_key, consumer_secret, access_token, access_token_secret)

#TwitterAPIのURL
url = "https://api.twitter.com/2/tweets/search/recent"

#検索条件
params = {'query': 
'{副反応or副作用} {AEやSAE} {品目} -is:retweet'
, 'max_results': {int}}

#検索条件を元に出力
res = auth.get(url, params = params)
#JSONをPythonの辞書型に変換
result = json.loads(res.text) 
#PythonオブジェクトをJSONデータ（文字列）に変換し出力。日本語文字化け対応"ensure_ascii"を”False”
print(json.dumps(result, indent=2, ensure_ascii=False)) 
