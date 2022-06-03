id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

answer = [0]*len(id_list)

report = set(report)
reported = {}

for i in report:
    a, b= i.split()

    if b not in reported:
        reported.update({b:1})
    else:
        reported.update({b:reported.get(b)+1})

for i in report:
    c, d = i.split()
    if d in reported:
        if reported.get(d)>=k:
            answer[id_list.index(c)] +=1

print(answer)



