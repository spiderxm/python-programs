#used pastebin for providing key and url to create a post request
import requests
key="04058209096f308ca6fe463ebf14491c"
url="https://pastebin.com/api/api_post.php"
data={

    "api_dev_key":key,
    "api_option":"paste",
    "api_paste_code":"hello world "
}
response=requests.post(url,data=data)
response.content