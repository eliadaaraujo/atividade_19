# Faça um dicionário com 3 frutas e seus respectivos preços. Depois, peça ao usuário para digitar o nome de uma fruta e exiba o preço correspondente.

frutas = {
    "banana": 8,
    "maçã": 7,
    "abacate": 10 
}

fruta_nome = (input("Escolha uma fruta entre banana, maçã e abacate: "))
print("O preço da", fruta_nome, "é", frutas[fruta_nome])