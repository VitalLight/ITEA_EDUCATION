def dictionary():
    print("create dictionary")
    dic = {}
    key = input("Enter key    ")
    pas = input("Enter pass   ")

    dic.update({key:pas})
    print(f" Your dictionary {dic}")
dictionary()
