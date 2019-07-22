from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, FallOutTransition, RiseInTransition
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics.texture import Texture
import cv2
import os


Builder.load_file("welcomepage.kv")
Builder.load_file("loginpage.kv")
Builder.load_file("profilepage.kv")



########################################################## screens ###########################################################

class WelcomePage(Screen):
    pass


class Nextscreen(Screen):
	background_image = ObjectProperty(Image(source=os.path.dirname(os.path.abspath(__file__)) + "/data/images/uniziklogo3.png"))


class Profilepage(Screen):
	pass

########################################################## other widgets ###########################################################

class Mywig(Widget):
	nau_image = ObjectProperty(Image(source = os.path.dirname(os.path.abspath(__file__)) + "/data/images/uniziklogo3.png"))
	pass


class ProfilePic(Widget):
	"""docstring for ProfilePic"""
	profileimage = ObjectProperty(Image(source=os.path.dirname(os.path.abspath(__file__)) + "/data/images/profilepicsubstitute.jpg"))
		

class ScanScreen(Widget):
	#myimg = ObjectProperty(Image(source="\\home\\AiPeek\\data\\images\\uniziklogo2.jpg"))
	myimgg = Image()
	video = cv2.VideoCapture(0)
	#def work(self,startCam=startCam,updateCam=updateCam):
	#startCam()
	cascade = cv2.CascadeClassifier(os.path.dirname(os.path.abspath(__file__)) + "/data/haarcascade_frontalface_alt.xml")
	def updateCam(self,video=video,myimgg=myimgg,cascade=cascade):
		ret, Frame = video.read()
		if ret:
			grayFrame = cv2.cvtColor(Frame,cv2.COLOR_BGR2GRAY)
			faces = cascade.detectMultiScale(grayFrame,1.5,5)
			for (x,y,w,h) in faces:
				cv2.rectangle(Frame,(x,y),(x+w,y+h),(200,255,0),3)

			buf1 = cv2.flip(Frame,90)
			buf = buf1.tostring()
			texture1 = Texture.create(size=(Frame.shape[1],Frame.shape[0]),colorfmt="bgr")
			texture1.blit_buffer(buf, colorfmt="bgr",bufferfmt="ubyte")
			myimgg.texture = texture1

	Clock.schedule_interval(updateCam,1/30)

def changescreen(self):
		sm.current = "nextpage"
		check = "notnone"


sm = ScreenManager(transition=FadeTransition())
sm.add_widget(WelcomePage(name="welcomepage"))
sm.add_widget(Nextscreen(name="nextpage"))
sm.add_widget(Profilepage(name="profilepage"))


class mainApp(App):


	def build(self):
		Clock.schedule_once(changescreen,5)
		return sm

    
mainApp().run()
