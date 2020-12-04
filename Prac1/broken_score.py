"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter your marks"))
if 90<= score<100:
    print("excellent")
elif 50<= score<90:
    print("passable")
elif 0< score<50:
    print("bad")
else:
    print("invalid marks")
