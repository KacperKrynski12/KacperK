x = int(input("What's x? "))
# y = int(input("WHat's y? "))

# if x < y:
#     print("x is less than y")
# elif x > y:
#     print("x is grether than y")
# elif x == y:
#     print("x is equal to y")


match x:
    case x if x < 10:
        print ("x jest mniejsze od 10")
    case 20:
        print("x=20")
    case _:
        print("Domyślna wartość")
    