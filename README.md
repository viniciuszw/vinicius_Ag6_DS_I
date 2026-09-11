# Sistema de Desconto Progressivo em Python

Este projeto consiste em um programa desenvolvido em Python para calcular o valor de descontos progressivos em uma loja online, com base no valor total da compra efetuada pelo cliente.

## 📋 Regras de Negócio

O sistema aplica os descontos de forma automática conforme as seguintes faixas de valores:

* **Menor que R$ 200,00:** Desconto de 5%
* **De R$ 200,00 até R$ 299,99:** Desconto de 10%
* **R$ 300,00 ou mais:** Desconto de 15%

## 🚀 Tecnologias Utilizadas

* **Python 3.x**

## 💻 Como Executar o Programa

1. Certifique-se de ter o Python instalado em sua máquina.
2. Baixe ou clone o arquivo do projeto (`seuNome_Ag6_DS_I.py`).
3. Abra o terminal ou prompt de comando na pasta onde o arquivo está salvo.
4. Execute o comando abaixo:

```bash
python seuNome_Ag6_DS_I.py

```

5. Insira o valor total da compra solicitado no terminal e pressione **Enter** para visualizar o resumo detalhado (valor original, percentual de desconto, valor economizado e o total final a ser pago).

## 📂 Estrutura do Código

O código foi estruturado utilizando boas práticas de programação:

* **Função dedicada (`calcular_desconto`):** Isola a lógica principal de cálculo e interação com o usuário.
* **Estruturas condicionais (`if`, `elif`, `else`):** Validação otimizada das faixas de preço sem redundâncias.
* **Comentários explicativos:** Documentam cada etapa do processo para facilitar a compreensão e manutenção do código.
