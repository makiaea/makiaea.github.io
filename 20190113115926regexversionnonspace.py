import re
import keyboard

def main():
	text = keyboard.get_selected_text()
	
	text = re.sub("^&nbsp;","",text)
	text = re.sub("&nbsp;<br>$","",text)
	text = re.sub("<br>$|^<br>","",text)
	text = re.sub("<u>|</u>","",text)
	
	text = re.sub("<td>|</td>|<tr>|</tr>|<tbody>|</tbody>|<table>|</table>|{|}","",text)
	text = re.sub(r"(\D)(\d|\d\S\d|\d\S\S\S\d)(\s|$|&nbsp;|,\D|;|<)",r"\1<sup>\2</sup>\3" ,text)
	
	'''text = re.sub(" |&nbsp;","",text)'''
	
	text = re.sub(" - | -- | –– ", " — ",text)
	text = re.sub("--|––", "—",text)
	text = text.replace("-", "–")
	text = text.replace("...", "…")
	
	text = re.sub("<div>","<br>",text,1)
	
	text = re.sub(r"(\S\D)(c|d|g|h|l|m|n|r|t|v)ize", r"\1\2ise",text)
	text = text.replace("avor", "avour")
	text = text.replace("honor", "honour")
	text = text.replace("color", "colour")
	text = text.replace("成语 saw", "idiom")
	
	text = re.sub("&nbsp;</div><div>|&nbsp;<br>| <br>|</div><div>|<br />|<br/>", "<br>",text)
	text = text.replace("<br><br><br>", "<br><br>")
	
	text = re.sub("<div>|</div>","",text)
	
	text = text.replace("  ", " ")
	text = text.replace(" / ", "/")
	text = re.sub(r"( |^)'(\b|<)",r"\1‘\2",text)
	text = re.sub(r"(\b|>)'(\s|\.|,|\))",r"\1’\2",text)
	text = text.replace("'", "’")
	text = re.sub(r"( |^)\"(\b|<)",r"\1“\2",text)
	text = re.sub(r"(\b|>)\"(\s|\.|,|\)|$)",r"\1”\2",text)
	text = re.sub("\(Jyutping\)|\(jyutping\)", "[<a href=\"http://www.cantonese.sheik.co.uk/dictionary/characters/751/\">粵</a>]",text)
	text = re.sub("\(Pinyin\)|\(pinyin\)", "[<a href=\"http://www.cantonese.sheik.co.uk/dictionary/characters/331/\">國</a>]",text)
	
	text = text.replace("msg–", "msg-")
	text = re.sub("<br>$|^<br>|&nbsp;$","",text)
	text = re.sub("<br>$|^<br>|&nbsp;$","",text)
	text = re.sub("&nbsp;"," ",text)
	
	if keyboard.is_keyboard():
		keyboard.play_input_click()
		keyboard.insert_text(text)
	else:
		# For debugging in the main app:
		print(f'Keyboard input: {text}')

if __name__ == '__main__': 
	main()
