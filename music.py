# Inspired in https://www.instagram.com/p/CC6Q55TnTDE/

from pygame import mixer

file = 'music.mp3'

mixer.init()
mixer.music.load(file)
mixer.music.play()
