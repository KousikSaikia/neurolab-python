class Car:

    def __init__(self,name,color):
        self.name = name
        self.color = color
    def displayCarDetails(self):
        print('car name is ',self.name,' and color is ',self.color)

    @staticmethod
    def initialMessage():
        print('Car info !!!!!')


Car.initialMessage()
car1=Car('Kia Seltos', 'Red')
car1.displayCarDetails()