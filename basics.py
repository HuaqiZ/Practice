x = int(3)
y = str("variable")
z = list(["Check", "Test", "List"])
a = dict({"name": "HQ", "status": "ok"})


def my_function(list):
    for x in list:
        if x != "List":
            print(x)


my_function(z)
