class mathDojo(object):
    def __init__(self):
        self.equation = ''
        self.value = 0
    def add(self,arg0,*restOfArgs):
        self.equation += '+'+str(arg0)
        self.value += arg0
        for i in range(0,len(restOfArgs)):
            self.equation += '+'+str(restOfArgs[i])
            self.value += int(restOfArgs[i])
        return self
    def subtract(self,arg0,*restOfArgs):
        self.equation += '-'+str(arg0)
        self.value -=arg0
        for i in range(0,len(restOfArgs)):
            self.equation += '-'+str(restOfArgs[i])
            self.value -= int(restOfArgs[i])
        return self
    def result(self):
        print self.equation,"=",self.value
        return self

md = mathDojo()
print md
md.add(2).result().add(2,3,4,5).result().subtract(4,4,2).result()
