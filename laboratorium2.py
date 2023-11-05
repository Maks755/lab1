x = int(input("średnie spalanie paliwa(w litrach na 100 km): "))
import random
los = random.randint(1, 100000)
cena_paliwa = 6,5
print(los)
s = los/100
y = s*x
print("samochód zużyje: " + str(int(y))+ " l")
t = y*6.5
print("a szacowane koszty podróży to: " + str(int(t))+ " zł")