from turtle import *

f = (5**0.5-1)/2.0   # (sqrt(5)-1)/2 -- golden ratio


def kite(l):
    fl = f * l
    lt(36)
    fd(l)
    rt(108)
    fd(fl)
    rt(36)
    fd(fl)
    rt(108)
    fd(l)
    rt(144)


# color('red', 'yellow')
# a = 50
# begin_fill()
# title("Welcome to the turtle zoo!")

# pos()
# bk(100)
# right(170)
# while True:

#     forward(200)
#     left(170)
#     a -= 1
#     if abs(pos()) < 1 or a == 0:
#         break

kite(100)
end_fill()

done()
