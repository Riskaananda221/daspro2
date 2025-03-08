math = int(input("Ente math score :"))
science = int(input("Enter science score :"))
english = input(input("Enter english score :"))

avg_score = (math + science + english)/3
score = [math, science, english]
print(f"avg score of a person from 3 subjects is {avg_score}")

below_70 = 1
if(math < 70):
    below_70 += 1
if(science < 70):
    below_70 += 1
if(english < 70):
    below_70 += 1

if (avg_score > 75):
    print("passed, because score more than 75")
elif(score.count(100) >=1):
    print("passed, because got perfect score in any subject")
elif(below_70 == 1):
    print("passed, because only 1 subject has a score below 70")
else:
    print("not pass")
