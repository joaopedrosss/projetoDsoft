from Cliente import Cliente

car = Cliente("jord","jord")

contratos = dict([])

new_user = "maga"
contratos[new_user] = ["carro4","carro6"]

new_user = "carlos"
contratos[new_user] = ["carro1","carro2"]

new_user = "artur"
contratos[new_user] = ["carro3","carro4"]

contratos[new_user].append("carro69090")
contratos[new_user].append(car)

print(contratos)
contratos[new_user].remove(car)
print(contratos)
"""
for i in contratos.keys():
    print(i)

for i in contratos.values():
    print(i)

#print(contratos)

for j in contratos.items():
    print(j)

#print(contratos.items())


if "carlos" in contratos:
    print("SIM! EXISTE")
"""
