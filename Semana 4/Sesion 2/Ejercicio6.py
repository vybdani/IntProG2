
p1 = float(input("Precio del primer producto: "))
p2 = float(input("Precio del segundo producto: "))
p3 = float(input("Precio del tercer producto: "))

subtotal = p1 + p2 + p3

iva = subtotal * 0.15

total = subtotal + iva

print(f"Subtotal: {subtotal}")
print(f"IVA (15%): {iva}")
print(f"Total a pagar: {total}")
