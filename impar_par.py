import random

print("jogo do impar ou par")
par_impar=(input("escolha se você quer ser par ou impar:"))
Humano=int(input("Digite um numero a sua escolha:"))
npc=random.randint(0,10)
print("A escolha do npc foi:",npc)
resultado=(Humano+npc)%2

if resultado==0 and par_impar=="par":
    print("Parabéns você ganhou") 
elif resultado!=0 and par_impar=="impar":
    print("Parabéns você ganhou") 
else:
    print("Derrota infelismente a maquina ganhou")