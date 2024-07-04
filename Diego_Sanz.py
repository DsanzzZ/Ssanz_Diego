from os import system
system("cls")

class pedido:
    def ppedido(self, id_pedido, cliente, direccion):
        self.id_pedido=id_pedido
        self.cliente=cliente
        self.direccion=direccion
        self.estado= "pendiente"

def pedidoo(self):
    return f"pedido #{self.id_pedido} - cliente: {self.cliente}, comuna: {self.comuna}, estado: {self.estado}"
pedidos= []


def registrar_pedidos():
    print("regista un nuevo pedido: ")
    id_pedido= len(pedidos) +1
    cliente= input("ingrese su nomnbre: ")
    comuna= input("ingrese su comuna: ")
    nuevo_pedido=pedido(id_pedido, cliente, comuna)
    pedidos.append(nuevo_pedido)
    input("precione enter para continuar")

def listar_pedidos():
    print("listado de pedidos: ")
    if not pedidos:
        print("no hay pedidos")
    else:
        for pedido in pedidos:
            print(pedido)
    input("precione enter para continuar")

def imprimir_hoja_de_ruta():
    print("imprimir hoja de ruta")
    if not pedidos:
        print("no hay pedidos")
    else:
        for pedido in pedidos:
            print(f"{pedido.id_pedido}: ")
    input("precione enter para continuar")

def buscar_pedido_por_id():
    print("buscar pedido por id")
    id_buscar= int(input("ingrese id del pedido: "))
    encontrada = False
    for pedido in pedidos:
        if pedido.id_pedido== id_buscar:
            print("pedido encontrado!")
            print(pedido)
            encontrada=True
        if not encontrada:
            print("el pedido no se a encontrado o no puso bien el codigo.")
    input("precione enter para continuar")

def salir_del_Programa():
    print("chao weta")
    exit()

def mostrar_menu():
    print(""" bienvenido! que deseas hacer?
    1. Registrar pedido
    2. Listar los todos los pedidos
    3. Imprimir hoja de ruta
    4. Buscar un pedido por ID
    5. Salir del programa""")

def main():
    while True:
        mostrar_menu()
        opcion=input("ingrese una opcion: ")
        if opcion=="1":
            registrar_pedidos()
        elif opcion=="2":
            listar_pedidos()
        elif opcion=="3":
            imprimir_hoja_de_ruta()
        elif opcion=="4":
            buscar_pedido_por_id()
        elif opcion=="5":
            salir_del_Programa()
        else:
            input("opcion invalida, preciona enter e intenta denuevo: ")
