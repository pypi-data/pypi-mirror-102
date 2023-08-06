import turtle as ingles

avanzar = ingles.forward
retroceder = ingles.backward
izquierda = ingles.left
derecha = ingles.right

ir_a = ingles.goto
ir_x = ingles.setx
ir_y = ingles.sety
mirar = ingles.setheading
casa = ingles.home

circulo = ingles.circle
punto = ingles.dot

estampa = ingles.stamp
limpiar_estampa = ingles.clearstamp
limpiar_estampas = ingles.clearstamps

deshacer = ingles.undo
velocidad = ingles.speed

posicion = ingles.position
pos = ingles.position
hacia = ingles.towards
x = ingles.xcor
y = ingles.ycor
mirando = ingles.heading
distancia = ingles.distance

grados = ingles.degrees
radianes = ingles.radians

lapiz_abajo = ingles.pendown
bajar = ingles.pendown
lapiz_arriba = ingles.penup
levantar = ingles.penup
lapiz_grosor = ingles.pensize
grosor = ingles.pensize
lapiz = ingles.pen
apoyado = ingles.isdown

color = ingles.color
color_lapiz = ingles.pencolor
color_relleno = ingles.fillcolor

relleno = ingles.filling
rellenar = ingles.begin_fill
empezar_relleno = ingles.begin_fill
rellenado = ingles.end_fill
terminar_relleno = ingles.end_fill

reset = ingles.reset
limpiar = ingles.clear
escribir = ingles.write

mostrar = ingles.showturtle
ocultar = ingles.hideturtle
visible = ingles.isvisible

forma = ingles.shape
modo_escala = ingles.resizemode
forma_escala = ingles.shapesize
corte = ingles.shearfactor
inclinacion_angulo = ingles.settiltangle
inclinacion = ingles.tilt
transformacion = ingles.shapetransform
politortu = ingles.get_shapepoly

en_click = ingles.onclick
en_soltar = ingles.onrelease
en_arrastrar = ingles.ondrag

empezar_poli = ingles.begin_poly
poli = ingles.begin_poly
terminar_poli = ingles.end_poly
gono = ingles.end_poly
poligono = ingles.get_poly
clonar = ingles.clone
tortugo = ingles.getturtle

deshacer_buffer = ingles.setundobuffer
deshacer_entradas = ingles.undobufferentries

color_fondo = ingles.bgcolor
imagen_fondo = ingles.bgpic
pantalla_escala = ingles.screensize
coordenadas_mundo = ingles.setworldcoordinates

esperar = ingles.delay
tracer = ingles.tracer
instantaneo = lambda: ingles.tracer(0,0)
actualizar = ingles.update

escuchar = ingles.listen
en_tecla = ingles.onkey
en_tecla_abajo = ingles.onkeypress
en_cronometro = ingles.ontimer
listo = ingles.done

leer_texto = ingles.textinput
leer_num = ingles.numinput
modo = ingles.mode
modo_color = ingles.colormode
pantalla = ingles.getcanvas
formas = ingles.getshapes
forma = ingles.addshape
tortugas = ingles.turtles
altura_ventana = ingles.window_height
ancho_ventana = ingles.window_width

chau = ingles.bye
adios = ingles.bye
cerrable = ingles.exitonclick
configuracion = ingles.setup
titulo = ingles.title
