# ye Score ki manually value hai 
# Score = 90

# ye hum user se input la rahien hai score ka
Score = int(input("Enter Your Score : "))

if Score > 100:
    print("Please Verify Your Score")
    exit()
elif Score >= 90:
    print("A")
elif Score >= 80:
    print("B")
elif Score >= 70:
    print("C")
elif Score >= 60:
    print("D")
else:
    print("Fail")
