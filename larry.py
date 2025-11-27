def factorial_recursivo(n):
    if n <= 1:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

numero = 5
resultado_factorial = factorial_recursivo(numero)
print(f"{resultado_factorial}")
def sumar_lista_recursiva(lista):
    if not lista:
        return 0
    else:
        return lista[0] + sumar_lista_recursiva(lista[1:])


numeros = [1, 2, 3, 4]
resultado_suma = sumar_lista_recursiva(numeros)
print(f"la suma de los productos de {numeros} es: {resultado_suma}")

class Medicamento:
    stock_critico = 300
    def __init__(self, nombre, categoria, stock, precio, codigo_barras):
        self.nombre = nombre
        self.categoria = categoria
        self.stock = int(stock)
        self.precio = float(precio)
        self.codigo_barras = codigo_barras
        print(f"remedio '{self.nombre}' creado con {self.stock} unidades en stock.")
    def vender(self, cantidad):

        if cantidad > self.stock:
            print(f"no hay  stock de {self.nombre}.")
            print(f"stock actual: {self.stock} cantidad solicitada: {cantidad}.")
            return False
        else:
            self.stock -= cantidad
            print(f"venta exitosa. {cantidad} unidades de {self.nombre} vendidas.")
            print(f"nuevo stock: {self.stock}.")
            return True
    def reponer_stock(self, cantidad):
        self.stock += cantidad
        print(f"reposición realizada {cantidad} unidades añadidas a {self.nombre}.")
        print(f"nuevo stock : {self.stock}.")
    def esta_en_stock_critico(self):
        return self.stock < self.stock_critico
paracetamol = Medicamento(
    nombre="actron 500mg",
    categoria="analgésico",
    stock=1000,
    precio=500,
    codigo_barras="7790001000001"
)
print(f"está {paracetamol.nombre} en stock crítico? {paracetamol.esta_en_stock_critico()}")
paracetamol.vender(cantidad=300)
paracetamol.vender(cantidad=20)
print(f"está {paracetamol.nombre} en stock crítico? {paracetamol.esta_en_stock_critico()}")
paracetamol.reponer_stock(cantidad=50)
print(f"está {paracetamol.nombre} en stock crítico? {paracetamol.esta_en_stock_critico()}")