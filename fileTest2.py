import fileTest
print("Top level in function")
fileTest.func()
if __name__ == "__main__":
	print("2 execute directly")
else:
	print("2 imported into another")