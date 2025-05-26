import random
import time
def sveiciens():
    vārds = input ("Ievadi savu vārdu:")
    print (f"Sveiks, {vārds}")
    return vārds 
def minet_skaitli ():
    pareizais_skaitlis = random.randint (1, 10)
    meginas = int(input("mini skaitli no 1 līdz 10:")) 

    if meginas == pareizais_skaitlis: 
        print ("pareizi")
    else: 
        print (f"nepareizi. pareizas skaitlis bija {pareizais_skaitlis}")

def vai_turpināt():
    atbilde = input("vai vēlies spēlēt vēlreiz? (jā/ne):").lower()
    return atbilde == 'jā'
def galvena_programma():
    sākums = time.time()

    sveiciens()

    while True: 
        minet_skaitli()
        if not vai_turpināt():
            break 
    beigas = time.time()
    ilgums = beigas - sākums 
    print(f"programma darbojas {ilgums:.2f}) sekundes")
    print("čau")
if __name__ == "__main__":
    galvena_programma()