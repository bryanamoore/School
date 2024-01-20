print("Enter a three-digit number: ", end = " ")
threeDigitNumber = int(input())
hundreds = threeDigitNumber // 100       # // is DIV, integer division
tens = (threeDigitNumber % 100)//10      # % is MOD 
units = (threeDigitNumber % 100) % 10
print (hundreds,"hundreds ")
print(tens,"tens")
print("and",units,"units")



# ALternative...
print(threeDigitNumber//100, "Hundreds", 
      (threeDigitNumber%100)//10, "tens and ",
      threeDigitNumber%10, "units")