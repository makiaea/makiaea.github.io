import re
import keyboard
import webbrowser
import urllib

def main():
	text = keyboard.get_selected_text()
	
	if re.search("^[^A-Za-z]+$", text):
		task = urllib.parse.quote(text.encode('utf-8'))

		webbrowser.open('icabmobile://www.cantonese.sheik.co.uk/dictionary/search/?searchtype=1&text=' + task)
	else:
		text = re.sub("^<div>|</div>$|^&nbsp;|&nbsp;<br>$|<br>$|^<br>|<u>|</u>","",text, re.MULTILINE)
		
		text = re.sub("<td>|</td>|<tr>|</tr>|<tbody>|</tbody>|<table>|</table>|{|}|<span class=\"Apple-tab-span\" style=\"white-space:pre\"> </span>","",text)
		
		'''a little trick so we don't need to use two separate scripts'''
		if len(text) <= 40: 
			text = re.sub(r"(\D)(\d|\d\S\d|\d\S\S\S\d)(\s|$|&nbsp;|,\D|;|<)",r"\1<sup>\2</sup>\3" ,text)
			text = re.sub(" |&nbsp;","",text)
		else:
			text = re.sub(r"(\D)(\d|\d\S\d|\d\S\S\S\d)(\s|$|&nbsp;|,\D|;|<)",r"\1<sup>\2</sup>\3" ,text)
		
		text = re.sub(" - | -- | –– ", " &mdash; ",text)
		text = re.sub("--|––", "&mdash;",text)
		text = text.replace("-", "&ndash;")
		text = text.replace("...", "…")
		
		text = re.sub("<div>","<br>",text,1)
		
		text = re.sub(r"(\S\D)(c|d|g|h|l|m|n|r|t|v)iz(e|a)", r"\1\2is\3",text)
		text = text.replace("avor", "avour")
		text = text.replace("honor", "honour")
		text = text.replace("color", "colour")
		text = text.replace("成语 saw", "idiom")
		
		text = re.sub("&nbsp;</div><div>|&nbsp;<br>| <br>|</div><div>|<br />|<br/>", "<br>",text)
		
		text = re.sub("<div>|</div>","",text)
		
		text = text.replace("  ", " ")
		text = text.replace(" / ", "/")
		text = re.sub(r"( |^)'(\b|<)",r"\1&lsquo;\2",text)
		text = re.sub(r"(\b|>)'(\s|\.|,|:|;|\))",r"\1&rsquo;\2",text)
		text = text.replace("'", "&rsquo;")
		text = re.sub(r"( |^)\"(\b|<)",r"\1&ldquo;\2",text)
		text = re.sub(r"(\b|>|\?|!)\"(\s|\.|,|:|;|<|\)|$)",r"\1&rdquo;\2",text)
		text = re.sub("\(Jyutping\)|\(jyutping\)|Jyutping|jyutping", "[<a href=\"http://www.cantonese.sheik.co.uk/dictionary/characters/751/\">粵</a>]",text)
		text = re.sub("\(Pinyin\)|\(pinyin\)|Pinyin|pinyin", "[<a href=\"http://www.cantonese.sheik.co.uk/dictionary/characters/331/\">國</a>]",text)
		
		text = text.replace("msg&ndash;", "msg-")
		text = re.sub("<br>$|^<br>|&nbsp;$","",text, re.MULTILINE)
		text = re.sub("<br>$|^<br>|&nbsp;$","",text, re.MULTILINE)
		text = re.sub("<sup><sup>","<sup>",text)
		text = re.sub("</sup></sup>","</sup>",text)
		text = re.sub("&nbsp;"," ",text)
		text = text.replace("lit.,", "<em>lit.</em>")
		
		'''prep for pasting'''
		text = text.replace("\n\n","<br><br>")
		text = text.replace("\n","<br>")
		text = text.replace("<br><br><br>", "<br><br>")
		text = re.sub("<br>$|^<br>|^ ","",text, re.MULTILINE)
		text = re.sub("<br>$|^<br>|^ ","",text, re.MULTILINE)
	
	
	if keyboard.is_keyboard():
		keyboard.play_input_click()
		keyboard.insert_text(text)
	else:
		# For debugging in the main app:
		print(f'Keyboard input: {text}')

if __name__ == '__main__': 
	main()
	quit()
