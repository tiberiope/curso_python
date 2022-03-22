nome1 = "jefferson"
nome2 = "lobato"
nome_completo = "     " + nome1 + "    " + nome2 + "     "
num = 5

print(nome_completo.upper())
print(nome_completo.lower())
print("Eu sou: " + nome_completo.title().strip() + ". Pode falar." )
print("Olá, %s, tudo bem? Tem %i minutos?" %(nome_completo.title().rstrip(), num))
print("Olá, " + nome_completo.title().lstrip() + ", tudo bem? Tem", 5, "minutos?")
print("Olá, " + " ".join(nome_completo.split()).title() + ", tudo bem? Tem " + str(5) + " minutos?")
print("Olá, " + " ".join(nome_completo.split()).title() + ",\ntudo bem?\nTem " + str(5) + " minutos?")