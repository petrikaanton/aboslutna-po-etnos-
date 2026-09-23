import random
počet_opakovani = 10000
vyskit = {}
percento = {}
for i in range(1,10):
    vyskit[i] = 0

for i in range(1,10):
    percento[i] = 0


for i in range(0,počet_opakovani+1):
    cislo = random.choice(range(1,100))**random.choice(range(1,100))
    prva_cislica = int(str(cislo)[0])
    vyskit[prva_cislica] += 1

for i in range(1,10):
    percento[i] += round(vyskit[i]/10000 * 100,2)

print(vyskit)
print(percento)