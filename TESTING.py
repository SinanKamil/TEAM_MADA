from time import sleep
x = 8
y = 9

def run():
    for runs in range(x):
        g = runs + y
        print("Run: ", g)
        sleep(.3)
