from tkinter import *


def first_step(event):
    """Get the content of entries and 
       passes result to the output area
    """
    try:
        a=int(ent_1.get())
        b=int(ent_2.get())
        c=int(ent_3.get())
        text = calculation(a, b, c)
        lbl5.configure(text = text)
        
    except ValueError:
        text="Убедитесь, \nчто вы ввели все данные."
        lbl5.configure(text=text)
    return

def calculation (a:float, b:float, c:float):
    D=b*b-4*a*c
    if D==0:
        x=round(((-b)/2*a), 2)
        text=f"D=0 \nx={x}"
    elif D>0:
        x1=round(((-b-D*D)/2*a),2)
        x2=round(((-b+D*D)/2*a),2)
        text=f"D>0 \nx1={x1} \nx2={x2}"
    elif D<0:
        text="D<0 \nКорней нет."
    return text


window=Tk()
window.title("Квадратные уравнения")
window.geometry("550x250")
window.iconbitmap("math_1.ico")

lbl=Label(window, text="Решение квадратного уравнения", fg="#6C6A69", font=("Arial", 18, "bold"))
lbl.pack()

ent_1=Entry(window, fg="blue", width=5, font="Arial, 15")
ent_1.bind("<Return>")
ent_1.pack(side=LEFT)

lbl2=Label(window, text="x**2+", fg="#6C6A69", font=("Arial", 16, "bold"))
lbl2.pack(side=LEFT)

ent_2=Entry(window, fg="blue", width=5, font="Arial, 15")
ent_2.bind("<Return>")
ent_2.pack(side=LEFT)

lbl3=Label(window, text="x+", fg="#6C6A69", font=("Arial", 16, "bold"))
lbl3.pack(side=LEFT)


ent_3=Entry(window, fg="blue", width=5, font="Arial, 15")
ent_3.bind("<Return>")
ent_3.pack(side=LEFT)

lbl4=Label(window, text="=0", fg="#6C6A69", font=("Arial", 16, "bold"))
lbl4.pack(side=LEFT)

btn_1=Button(window, text="Решить", font=("Arial", 15, "bold"), fg="#6C6A69", bg="#B7B6B6")
btn_1.bind("<Button-1>", first_step)
btn_1.pack(side=LEFT)

lbl5=Label(window, width=30, height=4, bg="#B7B6B6", text="Результат:", fg="black", font=("Arial", 10, "bold"))
lbl5.pack(side=BOTTOM)

window.mainloop()