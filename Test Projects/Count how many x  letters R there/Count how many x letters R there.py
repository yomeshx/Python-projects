Text = "abbaaCCaaajjjjNNNmmmAAAAAaaaaddddadadadaad"

counter = dict()

for letter in Text:
    if not letter in counter:
        counter[letter] = 1

    else:
        counter[letter] += 1

print(counter)
