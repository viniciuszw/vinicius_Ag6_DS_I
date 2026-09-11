# Programa: Sistema de Desconto Progressivo
# Autor: [Seu Nome Aqui]
# Descrição: Calcula o desconto e o valor final de uma compra com base em faixas de preço estabelecidas.

# Solicita o valor total da compra ao usuário e converte para ponto flutuante
valor_compra = float(input("Digite o valor total da compra (R$): "))
    
    # Determina o percentual de desconto de acordo com o valor da compra
if valor_compra < 200.00:
        percentual_desconto = 0.05  # 5% de desconto para compras abaixo de R$ 200,00
elif valor_compra < 300.00:
        percentual_desconto = 0.10  # 10% de desconto para compras entre R$ 200,00 e R$ 299,99
else:
        percentual_desconto = 0.15  # 15% de desconto para compras de R$ 300,00 ou mais
        
    # Calcula o valor monetário do desconto e o valor total a ser pago
valor_desconto = valor_compra * percentual_desconto
valor_final = valor_compra - valor_desconto
    
    # Exibe os resultados formatados para o usuário
print("\n--- Resumo da Compra ---")
print(f"Valor original: R$ {valor_compra:.2f}")
print(f"Desconto aplicado: {int(percentual_desconto * 100)}% (R$ {valor_desconto:.2f})")
print(f"Valor final a ser pago: R$ {valor_final:.2f}")
