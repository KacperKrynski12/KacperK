#Pytanie usera o jego imie 
def hello():
    mojeimie = input("Jak masz na imie:").strip().title()
    print(f"cześć {mojeimie}")
# mojeimie = mojeimie.strip()
# mojeimie = mojeimie.capitalize()
# mojeimie = mojeimie.title()
#end i sep w środku?

# String methods
#Removing white space
#Title method - each word start with Capital letter.
#We can combine string methods for instance mojeimie = mojeimie.capitalize().title()

#int
#typy danych
x = float(input("what's x? "))
y = float(input("What's y? "))
z = round(x/y)

print(f"{z}")

#Funkcje
hello()



