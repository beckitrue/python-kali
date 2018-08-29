# Project B: Compute MPG and Compute test scores of students

def mpg():
# computes miles per gallon
    print ("\nWe're going to compute your miles per gallon")
    miles = float (input ("Enter miles driven: "))
    gallons = float (input ("Enter the number of gallons used: "))
    mpg = miles / gallons
    print ("Your MPG is: "+"{:.2f}\n".format(mpg))
    return 

def test_avg():
# computes the averages of test scores
    scores = ['']
    subtotal = 0
    i = 0
    print ("This will compute the average test scores")
    numofscores = int(input("How many scores do you want to enter: "))
    while i < numofscores:
        score = int(input ("Enter test score: "))
        subtotal += score
        scores.insert(i, score)
        i += 1
    avg_score = subtotal / numofscores
    
    print ("The average score is: "+"{:.1f}".format(avg_score))
    print ("The scores you entered are: ")
    i = 0
    while i < numofscores:
        scores_string = f"score {i}: {scores[i]}"
        print(scores_string)
        i += 1
    return
    
mpg()
test_avg()




