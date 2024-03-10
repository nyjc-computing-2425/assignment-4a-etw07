nric = input('Enter an NRIC number: ')

# Type your code below
flag = 0
valid = ["S","T","G","S"]
if nric[0] not in valid:
  flag += 1
nric2 = nric[1:-1]
if nric2.isdigit() == False:
  flag += 1
elif len(nric2) != 7:
  flag += 1
if flag >= 1:
  print("NRIC is invalid.")
else:
  sum = 0
  weights = [2,7,6,5,4,3,2]
  for i in range(7):
    sum += weights[i]*int(nric2[i])
  if nric[0] == "T" or nric[0] == "G":
    sum += 4
  checkdigit = sum%11
  if nric[0] == "S" or nric[0] == "T":
    ST = "JZIHGFEDCBA"
    alpha = ST[checkdigit]
  else:
    FG = "XWUTRQPNMLK"
    alpha = FG[checkdigit]
  if alpha == nric[8]:
    print("NRIC is valid.")
  else:
    print("NRIC is invalid.")