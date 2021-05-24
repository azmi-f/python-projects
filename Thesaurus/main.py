import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def meaning(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("did you mean %s instead? Enter Y if yes N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]  
        elif yn == "N":
            return "The word doesn't match"
        else:
            return "we didnt get your query"
    else:
        return "your query doesnt exist"
word = input("enter your word:")

output = meaning(word)
print(output)
