def func():
	print("testRunning")
print("top level printing")

if __name__=="__main__":
	print("1 run directly")
else:
	print("1 run imported to another one")