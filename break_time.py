import webbrowser
import time
# Write a program that prompts the user to take a break
# once every two hours, a maximum of three times.
total_break = 3
count = 0
print ("this program started on: " + time.ctime())
while count < total_break:
    webbrowser.open("https://youtu.be/0ZBV0Co6PNc")
    time.sleep(2 * 60 * 60)
    count+=1
