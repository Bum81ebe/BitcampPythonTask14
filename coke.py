
def calculate():
    Amount_due = 50
    print(f"Amount due: {Amount_due}")
    while Amount_due > 0:
        money = int(input("Insert Coin: "))
        if money == 5 or money == 10 or money == 25:
            Amount_due = Amount_due - money   
            if Amount_due > 0:
                print(f"Amount Due: {Amount_due}")
                continue
            if Amount_due == 0:
                print(f"Change Owe: {Amount_due}")
                break
            if Amount_due < 0:
                print(f"Change Owed: {Amount_due * -1}")


calculate()