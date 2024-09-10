preco_original = float(input("Digite o preço original de mercadoria: "))
percentual_desconto = float(input("Digite o percentual de desconto: "))

valor_de_desconto = (preco_original * percentual_desconto) / 100
o_pagar = preco_original - valor_de_desconto

print("valor do desconto: R$ {:.2f} ".format(valor_de_desconto))
print("Preço a pagar: R$ {:.2f}".format(o_pagar))