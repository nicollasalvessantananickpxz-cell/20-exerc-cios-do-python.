preco = float(input("Digite o preco do produto: R$"))
desconto = float(input("Digite a porcentagem de desconto: "))
valor_desconto = preco * (desconto /100)
preco_final = preco - valor_desconto
print(f"desconto: R$ {valor_desconto:.2f} | preco final: R$ {preco_final:.2f}")
