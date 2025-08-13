"""
Sesion 1. 
12/08/2025

Velazquez Aldrete Zyanya Valentina 

Ejercicio 2. Genera la clase gen con almenos 3 atributos y 3 metodos (contando el constructor)

"""

import random

class Gen:
    def __init__(self, nombre='', secuencia='', organismo='', aspecto=None):
        self.nombre = nombre
        self.secuencia = secuencia.upper()
        self.organismo = organismo
        self.aspecto = aspecto  # Nuevo atributo opcional

    def mostrar_secuencia(self):
        codones_paro = ["UAG", "UAA", "UGA"]
        print(f"La secuencia del gen {self.nombre} es: {self.secuencia}")
        encontrado = False

        for codon in codones_paro:
            posicion = self.secuencia.find(codon)
            if posicion != -1:
                pos_nucl = posicion 
                print(f" Codón de paro encontrado: {codon} en la posición {pos_nucl}")
                encontrado = True

                if not encontrado :
                    print("No se encontraron codones de paro.")

    def mutar(self):
        bases = ["A", "U", "C", "G"]
        secuencia_lista = list(self.secuencia)
        cantidad_mutaciones = random.choice([1, 2])
        posiciones_mutadas = random.sample(range(len(secuencia_lista)), cantidad_mutaciones)

        print(f" Secuencia original: {self.secuencia}")
        for pos in posiciones_mutadas:
            base_original = secuencia_lista[pos]
            nueva_base = random.choice([b for b in bases if b != base_original])
            secuencia_lista[pos] = nueva_base
            print(f" - Mutación en posición {pos+1}: {base_original} → {nueva_base}")

        self.secuencia = "".join(secuencia_lista)
        print(f" Nueva secuencia: {self.secuencia}")

    def expresar(self):
        if "U" in self.secuencia:  # ARN
            print(f"El gen {self.nombre} es ARN y está siendo transcrito.")
            if self.organismo.lower() == "gato" and self.aspecto:
                print(f"Por ende el aspecto del {self.organismo} es {self.aspecto}")
        elif self.organismo.lower() == "gato" and self.aspecto:
            print(f"El gen {self.nombre} en el gato ({self.aspecto}) está siendo expresado.")
        else:
            print(f"El gen {self.nombre} no se está expresando actualmente.")


# Prueba
Ypgn = Gen('PreP', 'ACGUACGUAGCUAGCUACGAGU', 'gato', aspecto='negro')

Ypgn.mostrar_secuencia()
Ypgn.mutar()
Ypgn.expresar()