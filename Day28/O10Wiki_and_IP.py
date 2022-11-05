
import requests as rq
import wikipedia as wk

def getIP():
    myAddress = rq.get("https://api64.ipify.org?format=json").json()
    return myAddress['ip']

print(getIP())

def search_on_wikipedia(query):
    results = wk.summary(query, sentences=2)
    return results

# print(search_on_wikipedia("Sachin Tendulkar"))
# print(results)
print("-" * 40)

def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }

    res = rq.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res['joke']

print(get_random_joke())
