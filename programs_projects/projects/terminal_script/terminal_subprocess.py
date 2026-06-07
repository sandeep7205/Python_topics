import subprocess
# subprocess.run("clear", shell=True)
# res = subprocess.run("ping google.com", shell=True)


# Let's ping Google 10 times  
# For Windows use "-n" & For Mac/Linux use "-c"
# res = subprocess.run("ping -n 10 google.com", shell=True, capture_output=True,text=True) 
# capture_output=True: Tells Python to intercept the text instead of just printing it to the screen.
# text=True: Tells Python to return the output as a normal readable string, rather than raw computer bytes.
# print(res.stdout)

# Tell Python to call 'powershell' and pass the  -Command to it
subprocess.run("powershell -Command Get-Random", shell=True)