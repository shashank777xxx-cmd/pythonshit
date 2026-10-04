
a=input("enter your date of birth: ")
b=input("enter your partner's date of birth: ")
sum= int(a)+int(b)
love = (sum%100) +38
print("your love percentage is:",love,"%")
if love>=45:
    print("You have a strong chance of success!")
else:
    print("You may face some challenges in your relationship.")
print()
print("imp.note:")
print ( "love is just not about numbers and dates, its about \nunderstanding your partner not using some stupid love calc. ".center(5))