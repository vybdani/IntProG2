presupuesto = float(input("Monto del presupuesto anual: "))
urgencias = presupuesto * 0.37
pediatria = presupuesto * 0.42
trauma = presupuesto * 0.21
print(f"Urgencias: ${urgencias}")
print(f"Pediatría: ${pediatria}")
print(f"Traumatología: ${trauma}")
