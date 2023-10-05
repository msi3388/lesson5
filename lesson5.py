class ExampleClass:
    def __init__(self, val):
        self.val=val
    def __repr__(self):
        return "Bu classning nomi ExampleClass"
    def __str__(self):
        return "This is ExampleClass"
    def __bool__(self):
        return False

    # Dunder, Magic Methods
if __name__=="__main__":
    object=ExampleClass(5)
    object2=ExampleClass(15)
    object3=ExampleClass(7)
    print(object)
    print([object])
    print(bool(object))
    print(str(object)+str(object2))
