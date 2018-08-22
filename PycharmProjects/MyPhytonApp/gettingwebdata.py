import requests

import json
# url = "http://en.wikipedia.org/wiki/main_page"
# try:
#     response = requests.get(url)
#     if response.status_code == 200:
#         web_page_text = response.content.decode('utf-8')
#         if web_page_text.find("Did you know") > 0:
#              print("Funcionou!!")
#         else:
#              print("Nao funcou!")
#     else:
#         print(response.status_code)
# except:
#     print("algo deu errado com requests.get")
# #
# # in case of response in json format you can simply do for ex.
# # response = requests.get(url).json()
#
#playing w/ json
x='[[{"equity":[{"ticker":"AAPL", "value":139.78, "change": "+0.59%"}],"option":[{"ticker":"AAPLOCT17120","value":21.22,"change":"-2.4%"}]}]]'

try:
    y = json.loads(x)
    print(type(x))
    print(type(y))
    print(y)
    print(y[0])
    print(y[0][0]['option'])
    print(y[0][0]['option'][0]['value'])
except:
    print("exceção")








