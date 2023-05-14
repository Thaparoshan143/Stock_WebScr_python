import random

# if you want to get randomly generated tol price for quick check
# number below is the number of script tol to generate
number=220
# File where the tol value is to be generate
tolFile="Scripts_Tol.txt"

with open(tolFile,"w") as scriptTolFile:
    for num in range(number):
        scriptTolFile.write(str(random.randint(100,500))+"\n")
    
print("== > Tol generated < ==")
