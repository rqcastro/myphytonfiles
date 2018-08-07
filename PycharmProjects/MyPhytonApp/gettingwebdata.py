import requests

url = "http://en.wikipedia.org/wiki/main_page"
response = requests.get(url)
if response.status_code == 200:
    web_page_text = response.content.decode('utf-8')
    if web_page_text.find("Did you know") > 0:
         print("Funcionou!!")
    else:
         print("Nao funcou!")
else:
    print(response.status_code)



