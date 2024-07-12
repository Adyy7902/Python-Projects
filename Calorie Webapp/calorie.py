from temperature import Temperature


class Calorie:
     """
          Represent amount of calories calculated with
          BMR = 10 * weight + 6.25 * height - 5 * age
          + 5 - 10 * temperature
     """

     def __init__(self, weight, height, age, temperature):
          self.weight = weight
          self.height = height
          self.age = age
          self.temperature = temperature

     def calculate(self):
          return 10 * self.weight + 6.25 * self.height \
               - 5 * self.age + 5 - 10 * self.temperature

if __name__ == "__main__":
     temperature = Temperature(country = "india", city = "new delhi").get()
     calorie = Calorie(temperature = temperature, weight = 78, height = 198, age = 18)
     print(calorie.calculate())