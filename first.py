weight = int(input("Please Enter your weight: "))
height = float(input("Please Enter your height: "))
result = weight / (height * height)
print(result);
if result > 32:
	print("严重肥胖")
elif result >= 28:
	print("肥胖")
elif result >= 25:
	print("过重")
elif result >= 18.5:
	print("正常")
else:
	print("过轻")
