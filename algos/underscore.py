class Underscore(object):
    def __init__(self):
        pass
    def map(self,array,callback):
        list=[]
        for each in array:
            list.append(callback(each))
        return list
    def reduce(self,array,callback):
        if len(array) >= 2:
            value = array.pop(0)
            if len(array) > 1:
                return callback(value,self.reduce(array,callback))
            else:
                return callback(value,array[0])
    def find(self,array,callback):
        for each in array:
            if callback(each):
                return each
        return None
    def filter(self,array,callback):
        list=[]
        for each in array:
            if callback(each):
                list.append(each)
        return list
    def reject(self,array,callback):
        list=[]
        for each in array:
            if not callback(each):
                list.append(each)
        return list
_ = Underscore()
evens = _.filter([1,2,13,24,5,6,17,18],lambda x: x % 2 ==0)
print evens
odds = _.reject([1,2,13,24,5,6,17,18],lambda x: x % 2 ==0)
print odds
print _.find([1,51,13,5,17,19],lambda x: x % 2 ==0)
print _.map([1,2,3,4],lambda x: x ** 2)
print _.reduce([1,2,3,4,5],lambda x,y: x - y)
print _.reduce(['A','B','C','D',"E"],lambda x,y: x + y)
