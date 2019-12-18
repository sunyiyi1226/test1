import random
import sys

startNum = 1
endNum =100

count = 1

x = random.randint(1,101)

print("欢迎采集猜数字游戏，输入你猜测的数字，退出请输入：0")
try:
    guessX = int(input("输入数字：1-100\n"))
except ValueError:
    print("输入的不是整数，我退出了!拜拜")
    sys.exit()


while guessX != x and guessX != 0:

    if guessX>x:
        endNum=guessX
    else:
        startNum=guessX

    try:
        guessX = int(input("输入的值小了，提示：{}-{}之间：".format(startNum,endNum)))
    except ValueError:
        print("输入的不是整数，我退出了!拜拜")
        sys.exit()
    count += 1

else:
    if guessX==x:
        print("牛牛牛，猜了{}次就对了，X={}!".format(count,x))
    else:
        print("欢迎下来再来挑战")


