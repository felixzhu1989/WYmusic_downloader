import requests
import config as cf

url_song = cf.url_song
url_id = cf.url_id
url_name = cf.url_name
headers = cf.headers


def safeget(url,headers,red=False):
   res = requests.get(url=url,headers=headers,allow_redirects=red)
   if str(res.status_code)[0] not in ['4','5']:
      return res
   raise ConnectionError

def get_id_by_name(name):
   url = url_id.format(name)
   json = safeget(url,headers).json()['data']
   return None if json['songCount']==0 else [(i['name'],i['ar'][0]['name'],i['id']) for i in json['songs']]

def get_name_by_id(_id):
   #res = safeget(url_name+str(_id),headers=headers)
   return str(_id)+'.mp3'

def get_music_url_by_id(_id):
   url = url_song+str(_id)
   response = safeget(url,headers)
   location = response.headers['Location']
   return location if location.split('/')[-1]!='404' else None,get_name_by_id(_id)

def download(url,path='./music.py'):
   res = safeget(url=url,headers=headers)
   with open(path,'wb') as f:
      f.write(res.content)

if __name__ == '__main__':
   #test_area
   pass