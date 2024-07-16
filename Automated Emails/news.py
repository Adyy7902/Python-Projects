import requests
import datetime as dt

class NewsFeeds:
     """
     Representing multiple news title and links in a single string
     """
     base_url = "https://newsapi.org/v2/everything?"
     api_Key = "{Enter_Your_NewsAPI_API_Key}"

     def __init__(self, interest, from_date="", to_date="", language = 'en'):
          self.interest = interest
          self.from_date = "&from="+from_date
          self.to_date = "&to"+to_date
          self.language = language

     def get(self):
          url = self._build_url()
          articles = self._get_articles(url)

          return self._email_body(articles)

     def _email_body (self, articles):
          email_body = ""
          count = 1
          for article in articles:
               email_body = email_body + str(count) + ". " + article['title'] + "\n" + article['url'] + "\n\n"
               count += 1
          return email_body

     def _get_articles (self, url):
          response = requests.get(url)
          content = response.json()
          articles = content['articles']
          return articles

     def _build_url (self):
          url = (f"{self.base_url}"
                 f"qInTitle={self.interest}"
                 f"{self.from_date}"
                 f"{self.to_date}"
                 f"&language={self.language}"
                 f"&apiKey={self.api_Key}")
          return url
