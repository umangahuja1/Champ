from bs4 import BeautifulSoup
import requests


def songs_info(res):

    soup = BeautifulSoup(res.text, 'lxml')
    data = soup.find('ol', {'class': 'content-list'})
    return data


def get_songs(data, limit=10):
    song_list = []
    count = 0
    for i, count in zip(data.find_all('div', {'class': 'details'}), range(1, int(limit) + 1)):
        song = i.find('p', {'class': 'song-name'}).text
        album = i.find('p', {'class': 'album-name'}).text

        count += 1
        item = song
        if album != song:
            item = item + " (" + album + ")"
        song_list.append(item)
    return song_list

def saavn_tops(lang):
    res = requests.get("https://www.saavn.com/s/featured/" + lang + "/Weekly+Top+Songs")
    data = songs_info(res)
    return get_songs(data)

def hindi_chartbusters():	    
	res = requests.get("https://www.saavn.com/s/charts/Hindi-Chartbusters/u-75xwHI4ks_?&utm_content=wap%3Ahome%3Atop_charts%3Aplay%3Aclick&utm_page=home&utm_button=top_charts")
	data = songs_info(res)
	return get_songs(data)

def english_chartbusters():
	res = requests.get("https://www.saavn.com/s/charts/English-Chartbusters/9J4ePDXBp8k_?utm_content=wap%3Aall_top_charts%3Atop_charts%3Aplay%3Aclick&utm_page=all_top_charts&utm_button=top_charts&")
	data = songs_info(res)
	return get_songs(data)  



