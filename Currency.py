__author__ = 'Ethan Busbee'

class Currency:
    def __init__(self, amount=None):
        self._uDollars = 0 # Number of micro-USD (for precision)
        if type(amount) is type(self):
            self._uDollars = amount.getAmount()
        elif amount is not None:
            self._uDollars = int(round(amount * 1000000))

    def getAmount(self): return self._uDollars
    def toString(self): return "$" + "{:1,.2f}".format(self._uDollars / 1000000.0)

    def getDollarPart(self): return self._uDollars / 1000000
    def getCentPart(self): return (self._uDollars / 10000) % 100

    def add(self, other):
        if type(other) is not type(self):
            other = Currency(other)
        self._uDollars += other.getAmount()

    def sub(self, other):
        if type(other) is not type(self):
            other = Currency(other)
        self._uDollars -= other.getAmount()

    def mul(self, factor):
        self._uDollars *= factor
        self._uDollars = int(round(self._uDollars))

    def div(self, factor):
        self._uDollars /= factor
        self._uDollars = int(round(self._uDollars))

if __name__ == "__main__":
    print "Note: this class simulates down to micro-dollars to reduce rounding error."
    print "Also, right now this class ONLY handles USD and all output is formatted with regards to that."
    print "It doesn't yet do conversion of any kind, so you'll need to write your own glue code."
    print "Made with <3 by Ethan Busbee for his own learning."
    print ""

    print "***Init to $12.34"
    dough = Currency(12.34)
    print dough.toString()

    print "***Add $10"
    dough.add(10)
    print dough.toString()

    print "***Remove $5.00"
    dough.sub(5.00)
    print dough.toString()

    print "***Multiply by 5x"
    dough.mul(5)
    print dough.toString()

    print "***Divide by 5x"
    dough.div(5)
    print dough.toString()

    print "***Show dollars and cents separately."
    print "Dollars: " + str(dough.getDollarPart())
    print "Cents: " + str(dough.getCentPart())
