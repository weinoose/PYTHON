questions = ["What is the most used software language as of 2020?\n", "\nIf you use Unreal Engine in game production, which software language's Blueprints do you need to know?\n", "\nWhich of the following is a full scripting software language?\n"]
selections = ["A) Python\nB) C\nC) C++\nD) JAVA\nE) Ruby\n", "A) Python\nB) C\nC) C++\nD) JAVA\nE) Ruby\n", "A) Python\nB) C\nC) C++\nD) C#\nE) JAVA\n"]
correct = ["A", "C", "A"]

n = 0
point = 0
true = 0
false = 0
qpp = int(100/len(questions))

if qpp*questions != 100:
    extra = 100 - (qpp*len(questions))
else:
    extra = 0

point += extra

while n < len(questions):
    print()
    print(questions[n])
    print()
    print(selections[n])
    z = input("What is your answer?: ")
    if z == correct[n]:
        point += qpp
        true += 1
        n += 1
    else:
        false += 1
        n += 1

print(f"Your exam result : {point} POINT | {true} T | {false} F")