class ToMass:

    def __init__(self, lst):
        self.lst = lst

    def __getitem__(self, item):
        return self.lst[item - 1]

    def __setitem__(self, item, value):
        self.lst[item - 1] = value

    def __str__(self):
        return self.lst


a = ToMass([1, 2, 4])
print(a[1])
