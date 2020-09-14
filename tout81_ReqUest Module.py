import requests
import bs4

x = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
print(x.text)
