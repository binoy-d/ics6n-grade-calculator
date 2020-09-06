'''
ICS6N SSII Grade Calculator
by: Daniel Binoy
Notes:
- I have no idea if this actually works lol
- Change the arrays below with your scores
- participation is below that
- @Instructor if you're reading this, please bless us
  with a nice final and a thick curve :)
'''

#each set of grades is an array
#where each element is a tuple 
#of the form (score, total)

#homework grades
h = [(10.5, 11), (10, 10), (5, 5.5), (10, 10.75), (4.75, 9), (6.5,6.75), (3.25,4.75), (7,10)]

#lab grades
l = [(5, 5), (7.25, 7.75), (5, 5)]

#quiz grades
q = [(15.91, 25), (25, 28), (25, 28), (37.32, 40)]

def calculate_percent(arr):
    return sum([i[0] for i in arr])/sum([i[1] for i in arr])

#each portion of the grade is calculated with weights
homework = calculate_percent(h)*20
lab = calculate_percent(l)*15
quiz = calculate_percent(q)*20
participation = 1.0*10 #100% participation lol
final = (0.95)*35 #hypothetical final grade = 95%

#self explanatory
nofinal = (homework+lab+quiz+participation)/(20+15+20+10)
withfinal = (homework+lab+quiz+participation+final)

print("Grade without final: ", nofinal)
print("Grade with final: ", withfinal)
