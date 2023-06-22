from bs4 import BeautifulSoup
import requests

#----------------------------------EXTRACTING JOBS DATA FROM LINKEDLN--------------------------------------------------
URL = "https://news.ycombinator.com/jobs"

response = requests.get(url = URL).text

#----------------------- NOW USING EXTRACTED DATA TO  FIND JOBS NAMES ETC--------------------------------------------------------
job_data = []

soup = BeautifulSoup(response,"html.parser")

job_titles = soup.find_all(name="span",attrs={"class" : "titleline"})


for title in job_titles:
    job_title_ = title.text
    a_tag = title.find("a")
    href = a_tag.get("href")
    data = {
        "job_title" : job_title_,
        "job_link" : href
    }
    job_data.append(data)

print(job_data)
   
    




