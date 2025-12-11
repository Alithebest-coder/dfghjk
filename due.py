def find_due():
    bill=int(input("enter bill amount"))
    paid=int(input("enter paid amount"))
    if paid<bill:
        print("amount due:", bill-paid)
    else:
        due=bill-paid
        print("total bill", bill)
        print("amount paid:", paid)
        print("due:", due)
find_due()