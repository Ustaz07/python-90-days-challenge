# Pizza order for small 100, medium 200 or large size 300; with peperoni small size +30,
# medim or large +50; with cheese +20

print("Good day enter pizza size; 100 Rs for small, 200 Rs for medium and 300 Rs for large.")

pizza_size = int(input("Enter pizza size: "))

if (pizza_size == 100):
    print("Your order is small 100 Rs")
    peperoni = input("Do you need Peperoni with 30 Rs addition? (Y/N): ")
    with_peperoni = pizza_size + 30

    if (peperoni == "y" or peperoni == "Y"):
        print(f"Order with peperoni is {with_peperoni}")
        cheese = input("Do you need cheese with 20 Rs addition? (Y/N): ")
        with_peperoni_cheese = with_peperoni + 20

        if (cheese == "y" or cheese == "Y"):
            print(f"Small order with peperoni and cheese is {with_peperoni_cheese}")
        elif (cheese == "n" or cheese == "N"):
            print(f"Order with peperoni, without cheese is {with_peperoni}")

    elif (peperoni == "n" or peperoni == "N"):
        print(f"Order without peperoni is {pizza_size}")
        with_cheese = pizza_size + 20
        cheese = input("Do you need cheese with 20 Rs addition? (Y/N): ")
        
        if (cheese == "y" or cheese == "Y"):
            print(f"Small order without peperoni with cheese is {with_cheese}")
        elif (cheese == "n" or cheese == "N"):
            print(f"Order without peperoni and cheese is {pizza_size}")

elif (pizza_size == 200):
    print("Your order is medium 200 Rs")
    peperoni = input("Do you need Peperoni with 50 Rs addition? (Y/N): ")
    with_peperoni = pizza_size + 50

    if (peperoni == "y" or peperoni == "Y"):
        print(f"Order with peperoni is {with_peperoni}")
        cheese = input("Do you need cheese with 30 Rs addition? (Y/N): ")
        with_peperoni_cheese = with_peperoni + 30

        if (cheese == "y" or cheese == "Y"):
            print(f"Medium order with peperoni and cheese is {with_peperoni_cheese}")
        elif (cheese == "n" or cheese == "N"):
            print(f"Order with peperoni, without cheese is {with_peperoni}")

    elif (peperoni == "n" or peperoni == "N"):
        print(f"Order without peperoni is {pizza_size}")
        with_cheese = pizza_size + 20
        cheese = input("Do you need cheese with 20 Rs addition? (Y/N): ")
        
        if (cheese == "y" or cheese == "Y"):
            print(f"Medium order without peperoni with cheese is {with_cheese}")
        elif (cheese == "n" or cheese == "N"):
            print(f"Order without peperoni and cheese is {pizza_size}")


elif (pizza_size == 300):
    print("Your order is large 300 Rs")
    peperoni = input("Do you need Peperoni with 50 Rs addition? (Y/N): ")
    with_peperoni = pizza_size + 50

    if (peperoni == "y" or peperoni == "Y"):
        print(f"Order with peperoni is {with_peperoni}")
        cheese = input("Do you need cheese with 30 Rs addition? (Y/N): ")
        with_peperoni_cheese = with_peperoni + 30

        if (cheese == "y" or cheese == "Y"):
            print(f"Large order with peperoni and cheese is {with_peperoni_cheese}")
        elif (cheese == "n" or cheese == "N"):
            print(f"Order with peperoni, without cheese is {with_peperoni}")

    elif (peperoni == "n" or peperoni == "N"):
        print(f"Order without peperoni is {pizza_size}")
        with_cheese = pizza_size + 20
        cheese = input("Do you need cheese with 20 Rs addition? (Y/N): ")
        
        if (cheese == "y" or cheese == "Y"):
            print(f"Large order without peperoni with cheese is {with_cheese}")
        elif (cheese == "n" or cheese == "N"):
            print(f"Order without peperoni and cheese is {pizza_size}")

else:
    print("Please select correct pizza amount in Rs e.g. 100, 200 or 300.")











