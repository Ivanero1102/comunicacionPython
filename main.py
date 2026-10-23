import threading
texto = ""
textoCompleto = ""
terminamos = False
lock = threading.Lock()

def agregarParte1(parte1):
    lock.acquire()
    global textoCompleto 
    textoCompleto = textoCompleto + parte1
    lock.release()

def agregarParte2(parte2):
    lock.acquire()
    global textoCompleto 
    textoCompleto = textoCompleto + parte2
    lock.release()

def escritura():
    lock.acquire()
    global textoCompleto 
    print(textoCompleto)
    lock.release()

#def escritura2():
#    textoReserva = ""
#    while terminamos:
#        global textoCompleto 
#        if textoReserva != textoCompleto:
#            lock.acquire()
#            textoReserva = textoCompleto
#            print(textoCompleto)
#            lock.release()

while terminamos:
    print("Introduce un texto, -1 corta la ejecucion")
    texto = input()
    if(texto != "-1"):
        mitad = len(texto) // 2
        parte1 = texto[:mitad]
        print(parte1)
        parte2 = texto[mitad:]
        print(parte2)
        hiloAgregarParte1 = threading.Thread(target=agregarParte1, args=(parte1,))
        hiloAgregarParte2 = threading.Thread(target=agregarParte2, args=(parte2,))
        hiloAgregarParte1.start()
        hiloAgregarParte2.start()
    else:
        terminamos = True

hiloEscritura = threading.Thread(target=escritura,)
hiloEscritura.start()