class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def clarks(self):
        print(f"My name is {self.name} "
              f"i am {self.age} years old" )


mypple = People(name="Michael", age=18)
mypple2 = People(name="Kim", age=20)
mypple3 = People(name="Edu", age=25)
mypple4 = People(name="Gerad", age=27)
mypple5 = People(name="Yobra", age=17)
mypple.clarks()
mypple2.clarks()
mypple3.clarks()
mypple4.clarks()
mypple5.clarks()
