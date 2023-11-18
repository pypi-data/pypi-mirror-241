import re
caracteres_speciaux = []
for i in range(32, 127):
    if not chr(i).isalnum():
        caracteres_speciaux.append(chr(i))

to_replace =list(caracteres_speciaux)
# = [",", ";", "?", "!", "'", ":", "/", ".", " ","_"]

def slugify(chenn, separator="-"):
    for i in chenn:
        if i in to_replace:

            chenn = chenn.replace(i, separator)
            if chenn[-1]  in to_replace :
                chenn = chenn[:-1]
            
    
    return chenn.strip().lower()

def clean_tiret(txt):
    un_tiret = re.sub(r'-+', '-', txt)
    return un_tiret 

def sans_accent(txt):
    accents = {'é': 'e', 'è': 'e', 'à': 'a', 'ê': 'e', 'ô': 'o', 'û': 'u', 'ç': 'c', 'î': 'i', 'â': 'a'}
    convert = ''.join(accents.get(char, char) for char in txt)
    return convert

def fusion_fonct(chenn):
    k = slugify(chenn)
    k = clean_tiret(k)
    k = sans_accent(k)
    
    return k

chenn_input = input("Saisissez un texte : ")
resultat_fusion = fusion_fonct(chenn_input)
index_non_tiret = 0
while index_non_tiret < len(resultat_fusion) and resultat_fusion[index_non_tiret] == "-":
    index_non_tiret += 1

resultat_fusion = resultat_fusion[index_non_tiret:]

print(resultat_fusion)



