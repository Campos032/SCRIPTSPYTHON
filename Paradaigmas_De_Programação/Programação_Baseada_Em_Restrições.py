# A Programação Baseada em Restrições (PBR) é uma abordagem para resolver problemas computacionais que envolvem
# encontrar uma solução que satisfaça a um conjunto de restrições. Em vez de especificar uma sequência de passos para
# alcançar uma solução, como em algoritmos convencionais, a PBR se concentra em declarar as restrições que a solução
# deve satisfazer e usa técnicas de inferência para encontrar uma solução que as cumpra.

# Essa abordagem é especialmente útil em problemas onde é difícil ou impraticável definir um algoritmo passo a passo
# para alcançar a solução. Um exemplo clássico é o problema das N-Rainhas, onde o objetivo é posicionar N rainhas em
# um tabuleiro de xadrez de forma que nenhuma delas possa atacar outra. Em PBR, as restrições seriam que cada rainha
# não pode estar na mesma linha, coluna ou diagonal de outra rainha.

# Exemplo: Considere o problema de agendar horários para reuniões entre várias pessoas, onde cada pessoa tem suas
# próprias restrições de disponibilidade. Suponha que temos três pessoas, Alice, Bob e Carol, e queremos encontrar um
# horário em que todos possam participar de uma reunião.

# As restrições seriam as disponibilidades de cada pessoa. Por exemplo, Alice pode estar disponível das 9h às 12h e
# das 14h às 17h, Bob das 10h às 13h e das 15h às 18h, e Carol das 11h às 14h e das 16h às 19h.

# Ao aplicar a programação baseada em restrições, o sistema tentaria encontrar um horário em que todas as restrições
# sejam atendidas. Isso pode envolver técnicas como busca heurística ou algoritmos de satisfação de restrições para
# encontrar uma solução que satisfaça todas as restrições, como agendar a reunião das 11h às 12h, onde todos estão
# disponíveis.

# A PBR oferece uma abordagem flexível e poderosa para resolver uma ampla variedade de problemas em várias áreas,
# como logística, escalonamento, design de sistemas e muitos outros.

def encontrar_horario_disponivel(disponibilidades):
    # Define um conjunto com horários disponíveis da primeira pessoa
    horarios_comuns = set(disponibilidades[0])

    # Percorre a lista a partir da segunda pessoa
    for disponibilidade in disponibilidades[1:]:
        # Resulta em um novo conjunto contendo apenas os elementos que estão presentes em ambos os conjuntos
        horarios_comuns = horarios_comuns.intersection(disponibilidade)

    # Verifica se o conjunto está vazio ou não
    if horarios_comuns:
        return horarios_comuns
    else:
        return None


# Disponibilidades de cada pessoa
alice = {'9h', '10h', '11h', '12h', '14h', '15h', '16h', '17h'}
bob = {'10h', '11h', '12h', '13h', '15h', '16h', '17h', '18h'}
carol = {'11h', '12h', '13h', '14h', '16h', '17h', '18h', '19h'}

# Encontrar horário disponível para todos
disponibilidades = [alice, bob, carol]
horario_comum = encontrar_horario_disponivel(disponibilidades)

if horario_comum:
    print("Horário disponível para todos:", horario_comum)
else:
    print("Não há horário disponível para todos.")
