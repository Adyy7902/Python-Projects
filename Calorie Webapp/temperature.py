import requests
from selectorlib import Extractor


class Temperature:
     '''
     Represent a temperature value extracted from the timeanddate.com/weather webpage.
     '''
     base_url = 'https://www.timeanddate.com/weather/'
     yml_path = 'temperature.yaml'

     def __init__ (self, country, city):
          self.city = city.replace(" ", "-")
          self.country = country.replace(" ", "-")

     def _build_url (self):
          """Builds the url string by adding country and city"""
          return self.base_url + self.country + '/' + self.city

     def _scrape (self):
          """Extract a value as instructed by the yml file and returns a dictionary"""
          url = self._build_url()
          extractor = Extractor.from_yaml_file(self.yml_path)
          r = requests.get(url)
          full_content = r.text
          return extractor.extract(full_content)

     def get (self):
          """Cleans the output of _scrape() method"""
          scraped_content = self._scrape()
          return float(scraped_content["temp"].replace("°C", "").strip())


if __name__ == "__main__":
     country = input("Enter the country: ")
     city = input("Enter the city: ")
     temperature = Temperature(country, city)
     print(temperature.get())
