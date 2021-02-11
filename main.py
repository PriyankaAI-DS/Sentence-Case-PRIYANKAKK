name=input()
s=name.capitalize()
if s==name:
    t=name.replace(name[1:],name[1:].capitalize())
    print(t)
else:
    print(s)