import Tkinter
from tkinter.font import Font
#execfile("CS10 Timothy Vaipan THE AMAZING RACE")

root = Tkinter.Tk()
root.title('THE AMAZING RACE')

canvas = Tkinter.Canvas(root, height = 1000, width = 1590, relief = Tkinter.RAISED, bg = 'white')
canvas.grid()


'''def scuba_pass_show():
    if self.scuba_pass == True:'''
for i in range(5):
    canvas.create_rectangle(100+i, 200-i, 200+i, 300+i)
check = canvas.create_line(100, 250, 150, 300, 220, 150, fil = '#b2b2b2', width = 20)
message = canvas.create_text(380, 250, text = 'Try this!', font = ('Arial', -100))
'''else:
        for i in range(5):
            canvas.create_rectangle(100+i, 200-i, 200+i, 300+i)
        check = canvas.create_line(100, 250, 150, 300, 220, 150, fil = 'green', width = 20)
        message = canvas.create_text(380, 250, text = 'Try this!', font = ('Arial', -100))'''

#scuba_pass_show()

root.mainloop()