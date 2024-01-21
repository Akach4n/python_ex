import turtle

def dibujar_circulo():
    t = turtle.Turtle()
    turtle.getscreen().bgcolor("black")
    t.circle(100)
    turtle.done()

def dibujar_caca():
    t = turtle.Turtle()
    colors = ['orange','red','blue','yellow', 'pink', 'green']
    turtle.getscreen().bgcolor("black")
    for i in range(360):
        t.color(colors[i % len(colors)])
        t.pensize(width = i/100 + 1)
        t.left(360/6 - 1)
        t.forward(i)
    turtle.done()

with open("Dtexto.txt","r", encoding="utf-8") as texto:
    dibujar_caca()
    linea = texto.readline()
    while linea != None:
        if "círculo" in linea or "circulo" in linea:
            dibujar_circulo()
        else:
            print("nada")
        break

        
