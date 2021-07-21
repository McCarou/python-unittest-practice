from rabbit_mq import RabbitMqModule

class MyBeautifulClass:
    def __init__(self, quote='hi world', count=3):
        self.mq_connection = RabbitMqModule()
        self.quote = quote
        self.count = count
    
    def printQuoteCountTimes(self):
        print(self.quote * self.count)

    def splitQuote(self) -> list:
        return self.quote.split(' ')

    def splitCusotmQuote(self, customQuote) -> list:
        return customQuote.split(' ')

    def publishQuoteToMq(self):
        self.mq_connection.publishMessage()


if __name__ == "__main__":
    x = MyBeautifulClass('hi', 3)
    x.printQuoteCountTimes()
