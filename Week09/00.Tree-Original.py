#ลองนำโค้ดนี้ไปรันแล้วเปลี่ยนตัวเลขในวงเล็บดูสิ!

import turtle as t

for i in range(6):
        for j in range(6):
            t.forward(50)
            t.left(60)
        t.left(60)


#โค้ดนี้เอาไปรันแล้วลองเปลี่ยนเลขใน tree() บรรทัดสุดท้ายดูสิ! โปรแกรมมิ่งทำอะไรได้เยอะแยะเลย!

import turtle as t

def tree(leaf):
    t.forward(100)
    leaves(leaf)

def leaves(n,size = 100):
    if n == 0:
        return

    t.left(30)
    t.forward(size/1.5)
    leaves(n-1,size/1.5)
    t.backward(size/1.5)
    t.right(60)
    t.forward(size/1.5)
    leaves(n-1,size/1.5)
    t.backward(size/1.5)
    t.left(30)

t.left(90)
tree(8)
