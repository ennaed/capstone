from kivy.core.window import Window
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import OptionProperty, StringProperty, NumericProperty, ListProperty
from kivy.network.urlrequest import UrlRequest
from kivy.core.window import Window
Window.clearcolor = (0.82, 0.82, 0.82, 0.1)
import api
import api2


class TableHeader(Label):
	pass


class PlayerRecord(Label):
	pass


class MyGrid(GridLayout):

	cols = NumericProperty()

	def __init__(self, **kwargs):
		super(MyGrid, self).__init__(**kwargs)	
		try:
			self.fetch_data_from_database()
			self.display_scores()
		except:
			label1 = Label(text = '\n\nError.', valign='bottom', halign='center')
			self.add_widget(label1)


	def fetch_data_from_database(self):
		self.data = api2.fetch('/trucks')

	def display_scores(self):
		self.clear_widgets()
		for i in range(-1,len(self.data)):
			if i < 0:
				row = self.create_header()
			else:
				row = self.create_player_info(i)
			for item in row:
				self.add_widget(item)

	def create_header(self):
		first_column = TableHeader(text='Plate Number')
		second_column = TableHeader(text='Truck ID')
		return [first_column, second_column]

	def create_player_info(self, i):
		first_column = PlayerRecord(text=self.data[i]['plate_number'])
		second_column = PlayerRecord(text=self.data[i]['id'])
		return [first_column, second_column]

class DumpsiteGrid(GridLayout):

	cols = NumericProperty()

	def __init__(self, **kwargs):
		super(DumpsiteGrid, self).__init__(**kwargs)	
		try:
			self.fetch_data_from_database()
			self.display_scores()

		except:
			label1 = Label(text = '\n\nError.', valign='bottom', halign='center')
			self.add_widget(label1)


	def fetch_data_from_database(self):
		self.data = api2.fetch('/dumpsites')

	def display_scores(self):
		self.clear_widgets()
		for i in range(-1,len(self.data)):

			if i < 0:
				row = self.create_header()
			else:

				row = self.create_player_info(i)
			for item in row:
				self.add_widget(item)

	def create_header(self):
		first_column = TableHeader(text='Name')
		second_column = TableHeader(text='ID')
		third_column = TableHeader(text='Type')
		return [first_column, second_column, third_column]

	def create_player_info(self, i):
		lat = str(self.data[i]['lat'])
		lat = lat[:6]
		lon = str(self.data[i]['lon'])
		lon = lon[:6]

		first_column = PlayerRecord(text= self.data[i]['name'])
		second_column = PlayerRecord(text= str(self.data[i]['id']))
		if self.data[i]['legal'] == True:
			third_column = PlayerRecord(text= 'Legal')
		else:
			third_column = PlayerRecord(text= 'Illegal')
		return [first_column, second_column, third_column]

class MessageGrid(GridLayout):

	cols = NumericProperty()

	def __init__(self, **kwargs):
		super(MessageGrid, self).__init__(**kwargs)	
		try:
			self.fetch_data_from_database()
			self.display_scores()
		except:
			label1 = Label(text = '\n\nError.', valign='bottom', halign='center')
			self.add_widget(label1)

	def fetch_data_from_database(self):
		self.data = api.get_processed_data()

	def display_scores(self):
		self.clear_widgets()
		for i in range(-1,len(self.data)):
			if i < 0:
				row = self.create_header()
			else:
				row = self.create_player_info(i)
			for item in row:
				self.add_widget(item)

	def create_header(self):
		first_column = TableHeader(text='Plate Number')
		second_column = TableHeader(text='Dumpsite')
		third_column = TableHeader(text='Date & Time')

		return [first_column, second_column, third_column]

	def create_player_info(self, i):
		first_column = PlayerRecord(text=self.data[i]['plate_number'])
		second_column = PlayerRecord(text= self.data[i]['name'])
		third_column = PlayerRecord(text= str(self.data[i]['date']+ " " + str(self.data[i]['time'])))

		return [first_column, second_column,third_column]		


class SmartDumpsite(BoxLayout):  
	screen_manager = ObjectProperty(None)

	def __init__(self, *args, **kwargs):
		super(SmartDumpsite, self).__init__(*args, **kwargs)
		self.list_of_prev_screens = []

	def onNextScreen(self, btn, next_screen):
		self.list_of_prev_screens.append(btn.parent.parent.parent.name)
		self.screen_manager.current = next_screen

	def onBackBtn(self):
		if self.list_of_prev_screens:
			self.screen_manager.current = self.list_of_prev_screens.pop()
			return True
		return False

	def aboutPopUP(self):
		pop_content = BoxLayout(orientation = 'vertical')
		pop_close = Button(text = 'Close', size_hint=(0.5,0.1), halign='center', pos_hint= {'center_x': 0.5, 'center_y': 0.23})
		p_content = "This is a course requirement for CS 145 \n Department of Computer Science, College of Engineering, University of the Philippines, Diliman \n Developers:\n\n Karen Agnes \n Deanne Caingat \n Joseph Chua \n Michael Mayol \n Kyle Rosales"
		pop_label = Label(text = p_content, valign='middle', halign='center')
		pop_label.bind(size=pop_label.setter("text_size"))
		pop_content.add_widget(pop_label)
		pop_content.add_widget(pop_close)
		p = Popup(title = "About this Application", auto_dismiss = False, content = pop_content, size_hint=(0.8, 1))
		pop_close.bind(on_press = p.dismiss)
		p.open()		

class MainApp(App):  
	def __init__(self, *args, **kwargs):
		super(MainApp, self).__init__(*args, **kwargs)

	def build(self):
		return SmartDumpsite()

	def onBackBtn(self, window, key, *args):
		""" To be called whenever user presses Back/Esc key """
		# 27 is back press number code
		if key == 27:
			return self.root.onBackBtn()
		return False


if __name__ == "__main__":  
	MainApp().run()       