import random


def main():
    lvl=get_level()
    i=0
    score=0
    chance=3

    while i<10:
        x=generate_integer(lvl)
        y=generate_integer(lvl)
        while True:
            try:
                ans=int(input(f"{x} + {y} = "))
                if ans==x+y:
                    chance=3
                    score+=1
                    break
                if ans!=x+y:
                    print("EEE")
                    chance-=1
                if chance==0:
                    ans=False
                    print(f"{x} + {y} =",x+y)
                    break

            except:
                chance-=1
                if chance==0:
                    print(f"{x} + {y} =",x+y)
                    ans=False
                    break
                else:
                    print("EEE")
                    continue

        i+=1
    print("Score:",score)



def get_level():
    while True:
        try:
            n=int(input("Level: "))
        except:
            continue
        else:
            if n==1 or n==2 or n==3:
                break
    return n



def generate_integer(level):
    if level==1:
        return random.randint(0,9)

    elif level==2:
        return random.randint(10,99)


    elif level==3:
        return random.randint(100,999)




if __name__ == "__main__":
    main()
