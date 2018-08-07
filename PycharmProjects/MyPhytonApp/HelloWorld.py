import math
print(math.sqrt(4))

def margem_contribuicao(custo_variavel,  valor_venda):
    margem = valor_venda - custo_variavel
    margem_pc = (margem / valor_venda) * 100
    return margem, margem_pc

mc, mc_pc = margem_contribuicao(280, 350)
print(mc)
print(mc_pc)

