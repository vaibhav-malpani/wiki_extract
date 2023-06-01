import urllib.request
from bs4 import BeautifulSoup
import os

keywords_list = ['Tesla,_Inc.']


def write_to_file(data, keyword):
  if not os.path.exists('wiki_output'):
      os.makedirs('wiki_output')

  file_location = "./wiki_output/"+keyword+".txt"
  with open(file_location, "w", encoding="utf-8") as f:
    f.write(data)

def get_html(keyword):
  try:
    fp = urllib.request.urlopen("https://en.wikipedia.org/wiki/"+keyword)
    html = fp.read().decode("utf8")
    fp.close()
    return html
  except:
    print("page for "+keyword+" does not exist")

def extract_data(html):
  extracted_data = []
  soup = BeautifulSoup(html, 'html.parser')
  for data in soup.find_all('p'):
    extracted_data.append(data.text)
  return extracted_data

for keyword in keywords_list:
  keyword = keyword.replace(" ","_")
  html = get_html(keyword)
  data = "\n".join(extract_data(html))
  write_to_file(data,keyword)

print("Done for "+str(keywords_list)+" keywords")