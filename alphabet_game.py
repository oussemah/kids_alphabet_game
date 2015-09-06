import subprocess #for subprocess handling, mainly to play sounds
import re #for regular expression handling
from evdev import InputDevice, list_devices, categorize, ecodes
import time

def letter_sound(letter):
	return {
        ecodes.KEY_0 : "0.mp3",
        ecodes.KEY_1 : "1.mp3",
        ecodes.KEY_2 : "2.mp3",
        ecodes.KEY_3 : "3.mp3",
        ecodes.KEY_4 : "4.mp3",
        ecodes.KEY_5 : "5.mp3",
        ecodes.KEY_6 : "6.mp3",
        ecodes.KEY_7 : "7.mp3",
        ecodes.KEY_8 : "8.mp3",
        ecodes.KEY_9 : "9.mp3",
        ecodes.KEY_A : "a.mp3",
        ecodes.KEY_B : "b.mp3",
        ecodes.KEY_C : "c.mp3",
        ecodes.KEY_D : "d.mp3",
        ecodes.KEY_E : "e.mp3",
        ecodes.KEY_F : "f.mp3",
        ecodes.KEY_G : "g.mp3",
        ecodes.KEY_H : "h.mp3",
        ecodes.KEY_I : "i.mp3",
        ecodes.KEY_J : "j.mp3",
        ecodes.KEY_K : "k.mp3",
        ecodes.KEY_L : "l.mp3",
        ecodes.KEY_M : "m.mp3",
        ecodes.KEY_N : "n.mp3",
        ecodes.KEY_O : "o.mp3",
        ecodes.KEY_P : "p.mp3",
        ecodes.KEY_Q : "q.mp3",
        ecodes.KEY_R : "r.mp3",
        ecodes.KEY_S : "s.mp3",
        ecodes.KEY_T : "t.mp3",
        ecodes.KEY_U : "u.mp3",
        ecodes.KEY_V : "v.mp3",
        ecodes.KEY_W : "w.mp3",
        ecodes.KEY_X : "x.mp3",
        ecodes.KEY_Y : "y.mp3",
        ecodes.KEY_Z : "z.mp3",
	}.get(letter, "null.mp3")

def letter_image(letter):
	return {
        ecodes.KEY_A : "a.jpg",
        ecodes.KEY_B : "b.jpg",
        ecodes.KEY_C : "c.jpg",
        ecodes.KEY_D : "d.jpg",
        ecodes.KEY_E : "e.jpg",
        ecodes.KEY_F : "f.jpg",
        ecodes.KEY_G : "g.jpg",
        ecodes.KEY_H : "h.jpg",
        ecodes.KEY_I : "i.jpg",
        ecodes.KEY_J : "j.jpg",
        ecodes.KEY_K : "k.jpg",
        ecodes.KEY_L : "l.jpg",
        ecodes.KEY_M : "m.jpg",
        ecodes.KEY_N : "n.jpg",
        ecodes.KEY_O : "o.jpg",
        ecodes.KEY_P : "p.jpg",
        ecodes.KEY_Q : "q.jpg",
        ecodes.KEY_R : "r.jpg",
        ecodes.KEY_S : "s.jpg",
        ecodes.KEY_T : "t.jpg",
        ecodes.KEY_U : "u.jpg",
        ecodes.KEY_V : "v.jpg",
        ecodes.KEY_W : "w.jpg",
        ecodes.KEY_X : "x.jpg",
        ecodes.KEY_Y : "y.jpg",
        ecodes.KEY_Z : "z.jpg",
	}.get(letter, "null.jpg")

def sing(letter):
	singer= subprocess.Popen(["mplayer", "sound/"+letter_sound(letter)], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	return singer
 
def show(letter):
	viewer = subprocess.Popen(['eog', "image/"+letter_image(letter), "-fg"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	return viewer

def main():
	devices = [InputDevice(fn) for fn in list_devices()]
	viewer = subprocess.Popen(['eog', "image/alphabet.jpg", "-fg"], stdout = subprocess.PIPE, stderr=subprocess.PIPE)
	singer = subprocess.Popen(['mplayer', "image/null.mp3"], stdout = subprocess.PIPE, stderr=subprocess.PIPE)
	
	for dev in devices :
		if re.search("KB", dev.name) : #Put something that can define your keyboard name here
			print("Using input device at : "+dev.fn)
			keyb = dev#break #Normally you need to break, 
							 #but I comment it as my keyboard contains a section for media-player
							 #which is presented as another device with the same name.
	for event in keyb.read_loop():
		if event.type == ecodes.EV_KEY and event.value == 0x1 :
			if event.code == ecodes.KEY_ESC: #Quit
				singer.terminate()
				singer.kill()
				subprocess.Popen(["mplayer", "sound/goodbye.mp3"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
				time.sleep(2)
				singer.terminate()
				singer.kill()
				viewer.terminate()
				viewer.kill()
				quit()
			#Continue program
			viewer.terminate()
			viewer.kill()
			singer.terminate()
			singer.kill()
			#print(categorize(event)) #Uncomment if you need to debug
			singer = sing(event.code)
			viewer = show(event.code)

if __name__ == "__main__":
	main()
