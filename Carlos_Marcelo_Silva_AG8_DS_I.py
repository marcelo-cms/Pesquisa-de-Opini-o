# Pesquisa de Opinião

print("== Pesquisa de Opinião do Cliente ==")

total_entrevistados = 10

# Contadores para as estatísticas
qtd_excelente = 0
qtd_bom = 0
qtd_ruim = 0

for i in range(1, total_entrevistados + 1):
    print(f"\n--- Entrevistado {i} ---")
    
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    opiniao = int(input("Digite a opinião (1-EXCELENTE | 2-BOM | 3-RUIM): "))

    
    if opiniao == 1:
        print("Você avaliou como EXCELENTE.")
        qtd_excelente += 1
    elif opiniao == 2:
        print("Você avaliou como BOM.")
        qtd_bom += 1
    elif opiniao == 3:
        print("Você avaliou como RUIM.")
        qtd_ruim += 1
    else:
        print("Opção inválida!")

# Relatório final após coletar de todos os entrevistados
print("\n" + "="*10)
print("RESULTADO FINAL DA PESQUISA")
print("="*10)
print(f"Total de votos EXCELENTE: {qtd_excelente}")
print(f"Total de votos BOM: {qtd_bom}")
print(f"Total de votos RUIM: {qtd_ruim}")
