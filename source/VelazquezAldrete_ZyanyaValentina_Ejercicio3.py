"""
Sesion 2. 
19/08/2025

Velazquez Aldrete Zyanya Valentina 

Ejercicio 3. Usando el concepto de Herencia una subclase de la clase gen, llamada tRNA, 
y otra clase llamada RNA no codificante. Luego deriva de tRNA otra subclase llamada proteina. 

"""

from VelazquezAldrete_ZyanyaValentina_Ejercicio2 import Gen

class tRNA(Gen):
    def __init__(self, nombre='', secuencia='', organismo='', aspecto=None, anticodon='', aminoacido=''):
        super().__init__(nombre, secuencia, organismo, aspecto)
        self.anticodon = anticodon.upper()
        self.aminoacido = aminoacido
    
    def mostrar_estructura(self):
        print(f"tRNA {self.nombre}: Anticodón {self.anticodon}, transporta {self.aminoacido}")
    
    def unir_aminoacido(self):
        print(f"El tRNA {self.nombre} se está uniendo al aminoácido {self.aminoacido}")
    
    def reconocer_codon(self, codon_mRNA):
        codon_mRNA = codon_mRNA.upper()
        if self.anticodon == self._complementario(codon_mRNA):
            print(f"El tRNA {self.nombre} reconoce el codón {codon_mRNA}")
            return True
        else:
            print(f"El tRNA {self.nombre} NO reconoce el codón {codon_mRNA}")
            return False
    
    def _complementario(self, secuencia):
        complemento = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}
        return ''.join(complemento[base] for base in secuencia)


class RNANoCodificante(Gen):
    def __init__(self, nombre='', secuencia='', organismo='', aspecto=None, funcion='', localizacion=''):
        super().__init__(nombre, secuencia, organismo, aspecto)
        self.localizacion = localizacion
    
    def mostrar_localizacion(self):
        print(f"El RNA no codificante {self.nombre} se localiza en: {self.localizacion}")
    
    def regular_expresion(self, gen_objetivo):
        print(f"El RNA no codificante {self.nombre} está regulando la expresión de {gen_objetivo}")


class Proteina(tRNA):
    def __init__(self, nombre='', secuencia='', organismo='', aspecto=None, anticodon='', 
                 aminoacido='', estructura='', funcion_biologica=''):
        super().__init__(nombre, secuencia, organismo, aspecto, anticodon, aminoacido)
        self.estructura = estructura
        self.funcion_biologica = funcion_biologica
    
    def plegarse(self):
        print(f"La proteína {self.nombre} se está plegando en estructura {self.estructura}")
    
    def realizar_funcion_biologica(self):
        print(f"La proteína {self.nombre} está realizando su función: {self.funcion_biologica}")
    
    def degradarse(self):
        print(f"La proteína {self.nombre} se está degradando (proteólisis)")


# Pruebas de las clases
if __name__ == "__main__":
        
    # tRNA
    print("\n tRNA")
    trna1 = tRNA('DemS5', 'GGGCAGAGUCCUAGCGU', 'humano', None, 'CAU', 'Metionina')
    trna1.mostrar_secuencia()
    trna1.mostrar_estructura()
    trna1.reconocer_codon('AUG')
    trna1.unir_aminoacido()
    
    # RNAnocodif
    print("\n RNA no codificante")
    mirna = RNANoCodificante('miR-21', 'UGCUUAUCAGACUGGAUGUUGA', 'humano', None, 
                           'Regulación post-transcripcional', 'Citoplasma')
    mirna.mostrar_secuencia()
    mirna.mostrar_localizacion()
    mirna.regular_expresion('gen PTEN')
    
    # Proteína
    print("\n Proteína ")
    insulina = Proteina('Insulina', 'MALWMRLLPLLALLALWGPDPAAAFVNQHLCGSHLVEALYLVCGERGFFYTPKT', 
                       'humano', None, '', '', 'Terciaria', 'Regulación de glucosa en sangre')
    insulina.mostrar_secuencia()
    insulina.plegarse()
    insulina.realizar_funcion_biologica()
    
    # Mutación (heredado de Gen)
    print("\n Mutación en tRNA ")
    trna1.mutar()