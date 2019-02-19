#20190106213326
#pythonista script to search selected text in cantodict

import keyboard
import urllib
import webbrowser

def main():
	text = keyboard.get_selected_text()
	
	task = urllib.parse.quote(text.encode('utf-8'))

	webbrowser.open('https://www.duckduckgo.com/?q=!cantodict%20' + task)

if __name__ == '__main__': 
	main()
