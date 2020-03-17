import json

def sort_scores(scores:dict):
    test = [x for k, x in scores.items()]
    test['score'].sort()
    print(test)



def submit_score(initials:str, score:int):
    scores = get_scores()
    sort_scores(scores)

def get_scores():
    with open('scores.json', 'r') as f:
        scores = json.loads(f.readlines()[0])
        return scores

submit_score('ABC', 0)