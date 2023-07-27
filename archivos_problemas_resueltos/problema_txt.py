#2 listas, una con nombres y otra con apellidos

nombres = ["Oscar","Maria","Angelica","Mario","Roberto"]
apellidos = ["Morelos","Parra","Linares","Puente","Lopez"]

#registrar esta informacion en un txt de forma optima
with open("archivos_problemas_resueltos\\nombres_y_apellidos.txt","w") as arch:
    arch.writelines("Los datos son:\n\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n---------\n")for n,a in zip(nombres,apellidos)] 