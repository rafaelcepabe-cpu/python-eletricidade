import random
import time

print("=" * 40)
print("  SISTEMA DE VERIFICAÇÃO ELÉTRICA")
print("=" * 40)

while True:

    tensao = random.randint(90, 250)
    corrente = random.randint(1, 40)

    print(f"\nTensão atual: {tensao}V")
    print(f"Corrente atual: {corrente}A")

     # Verificação da tensão
    if tensao < 110:
        print("⚠ ALERTA: Baixa tensão detectada!")

    elif tensao > 220:
        print("⚠ ALERTA: Sobretensão detectada!")

    else:
        print("✅ Tensão normal")

     # Verificação da corrente

    if corrente > 30:
        print("⚠ ALERTA: Sobrecarga elétrica!")

    else:
        print("✅ Corrente dentro do limite")

      # Simulação de queda de energia

    if tensao < 100:
        print("❌ Possível queda de energia!")

    print("-" * 40)

    time.sleep(5)