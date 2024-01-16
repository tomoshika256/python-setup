import requests
import pprint

def api_post():
    # Post-URL => {JSON}placeholderを利用する
    POST_URL = "http://tk2-242-30965.vs.sakura.ne.jp:8080/02/hello"

# リクエストボディを定義
    request_body = {
    "name": "AAAA"
    }

    # postメソッドで、リクエストボディ付きでPost通信 => レスポンス・オブジェクトを受け取る
    response = requests.post(POST_URL, json=request_body)
    print(response.text)
