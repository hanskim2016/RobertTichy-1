class Animal(object):
    def __init__(self,name):
        self.name = name
        self.hp = 100
    def walk(self):
        print self.name, "walked"
        self.hp -= 1
        return self
    def run(self):
        print self.name, "ran"
        self.hp -= 5
        return self
    def displayHealth(self):
        print "Healh:",self.hp
        return self
class Dog(Animal):
    def __init__(self,name):
        super(Dog,self).__init__(name)
        self.hp = 150
    def pet(self):
        print self.name, "gets petted"
        self.hp += 5
        return self
class Dragon(Animal):
    def __init__(self,name):
        super(Dragon,self).__init__(name)
        self.hp = 170
    def fly(self):
        print self.name,"flew"
        self.hp -= 10
        return self
    def displayHealth(self):
        print "This is a Dragon!"
        super(Dragon,self).displayHealth()
        return self
animal = Animal('animal')
animal.walk().walk().walk().run().run().displayHealth()
dog0 = Dog('Barney')
print dog0.name
dog0.displayHealth()
dog0.walk().walk().walk().run().run().pet().displayHealth()
dragon0 = Dragon('Smaug')
dragon0.displayHealth()
dragon0.walk().walk().walk().run().run().fly().fly().displayHealth()
animal.fly()
animal.pet()
