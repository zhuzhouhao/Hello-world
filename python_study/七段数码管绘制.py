'''
step:
1.获得单个数字对应的数码管
2.获得一串数字，绘制对应的数码管
3.获得当前系统的时间，绘制对应的数码管
'''
import turtle,time
def drawGap():#绘制数码管间隔
    turtle.penup()
    turtle.fd(5)
def drawLine(draw):#绘制单段数码管
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    turtle.right(90)
def drawDigit(digit):#根据数字绘制七段数码管
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()#为绘制后续数字确定位置
    turtle.fd(20)#为绘制后续数字确定位置
def drawDate(date):#获得要输入的数字
    turtle.pencolor('red')
    for i in date:
        if i == '-':
            turtle.write('年',font = ("Arial",18,"normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == '=':
            turtle.write('月',font = ("Arial",18,"normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == '+':
            turtle.write('日',font = ("Arial",18,"normal"))
        else:
            drawDigit(eval(i))
def main():
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate(time.strftime("%Y-%m=%d+",time.gmtime()))
    turtle.done()
main()
