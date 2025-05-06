times = int(input())
results=[]
for i in range(times):
    sinal=input()
    sinal1=input()
    if sinal == 'ataque' and sinal1 == 'pedra':
        results.append('Jogador 1 venceu')
    elif sinal1 == 'ataque' and sinal == 'pedra':
        results.append('Jogador 2 venceu')
    elif sinal == 'papel' and sinal1 == 'papel':
        results.append('Ambos venceram')
    elif sinal == 'papel' and sinal1 == 'ataque':
        results.append('Jogador 2 venceu')
    elif sinal1 == 'papel' and sinal == 'ataque':
        results.append('Jogador 1 venceu')
    elif sinal == 'pedra' and sinal1 == 'papel':
        results.append('Jogador 1 venceu')
    elif sinal1 == 'pedra'and sinal == 'papel':
        results.append('Jogador 2 venceu')
    elif sinal1 == 'pedra' and sinal == 'pedra':
        results.append('Sem ganhador')
    elif sinal1 == 'ataque' and sinal == 'ataque':
        results.append('Aniquilacao mutua')
for j in range(len(results)):
    print(results[j])