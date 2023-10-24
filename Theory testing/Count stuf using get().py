count = dict()

names = ["Daniel","Anderson","Michel","Anderson","John","Mike","Anderson","Daniel","John","Daniel","Anderson","John","Mike","Michel","Daniel","Mike","Michel","Daniel"]

for name in names:
    count[name] = count.get(name,0) + 1

print(count)