"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""

class Classy(object):
    
    def __init__(self):
        self.items = []
        self.add = 0

    def addItem(self, item):
        self.items.append(item)

    def classiness(self):
        for item in self.items:
            print (item)
            if "tophat" == item:
                self.add += 2
            elif "bowtie" == item:
                self.add += 4
            elif "monocle" == item:
                self.add += 5
            else :
                self.add += 0
        return self.add

def main():
    me = Classy()
    result = me.classiness()
    print(result)
    me.addItem("tophat")
    result = me.classiness()
    me.addItem("bowtie")
    me.addItem("jacket")
    me.addItem("monocle")
    result = me.classiness()
    me.addItem("bowtie")
    result = me.classiness()

if __name__ == '__main__':
    main()
    
