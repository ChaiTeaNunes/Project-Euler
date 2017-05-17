# Names Scores

def parse(file):
    output = open(file).read().replace('\"', '').split(",")
    return sorted(output)

def get_name_score(name):
    score = 0
    for c in name.upper():
        score += (ord(c) - 64)
    return score

def scores(names):
    output = list()
    for i, name in enumerate(names):
        output.append(get_name_score(name) * (i + 1))
    return output

print(sum(scores(parse("22.txt"))))
