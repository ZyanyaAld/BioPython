'''
# Sesion 6. 
*29/09/2025*

# Velazquez Aldrete Zyanya Valentina 

# Ejercicio. Obtener cadena protéica de cualquiera de sus ORFs
'''
from Bio.Seq import Seq

seq_str = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
seq = Seq(seq_str)

# Codones de paro
stop_codons = ["TAA", "TAG", "TGA"]

def encontrar_orfs(seq):
    """Encuentra todos los ORFs posibles en los 3 marcos de lectura de una secuencia"""
    orfs = []
    for frame in range(3):
        i = frame
        while i < len(seq) - 2:
            codon = str(seq[i:i+3])
            if codon == "ATG":  # codón de inicio
                # buscar stop o final de la secuencia
                for j in range(i, len(seq), 3):
                    codon_j = str(seq[j:j+3])
                    if codon_j in stop_codons or j+3 >= len(seq):
                        orf = seq[i:j+3]
                        orfs.append(orf)
                        break
            i += 3
    return orfs

# ORFs en cadena forward y reversa
orfs_forward = encontrar_orfs(seq)
orfs_reverse = encontrar_orfs(seq.reverse_complement())

# Traducir a proteínas (sin cortar en STOP para ver todo)
proteins = [orf.translate() for orf in orfs_forward + orfs_reverse]

print("ORFs encontrados (nucleótidos):")
for o in orfs_forward + orfs_reverse:
    print(o)

print("\n Proteínas traducidas:")
for p in proteins:
    print(p)

# Elegir la más larga
if proteins:
    longest_protein = max(proteins, key=len)
    print("\nProteína más larga:")
    print(longest_protein)
else:
    print("No se encontraron ORFs.")
