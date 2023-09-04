import requests
from bs4 import BeautifulSoup




# url = 'https://media4.giphy.com/media/kgAzAJl4eUZzO/giphy.gif?cid=ecf05e4782je6qr60q7f2nj0wqpo9cfbotmd0rza5tnizcmw&amp;ep=v1_gifs_search&amp;rid=giphy.gif&amp;ct=g'
# response = requests.get(url)
# html_content = response.content
#
# soup = BeautifulSoup(html_content, 'html.parser')
#
# image_tag = soup.find('img')
#
# image_url = image_tag['src']
#
# image_response = requests.get(image_url)
# with open('image.jpg', 'wb') as f:
#     f.write(image_response.content)


url = 'https://media4.giphy.com/media/kgAzAJl4eUZzO/giphy.gif?cid=ecf05e4782je6qr60q7f2nj0wqpo9cfbotmd0rza5tnizcmw&ep=v1_gifs_search&rid=giphy.gif&ct=g'
response = requests.get(url)

if response.status_code == 200:
    with open('image.gif', 'wb') as f:
        f.write(response.content)
    print('Image downloaded successfully.')
else:
    print('Failed to download image.')



