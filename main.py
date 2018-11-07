
#coding:utf-8 




from Tkinter import *
from random import randint
from time import time
from time import sleep
import pickle





from params import kwargs
from math import sqrt

sys.path.append('../template')

from experiment_template import Experiment


consomn_string = "zrtpqsdfghjklmwxcvbn"
consomn_string = consomn_string.upper()



class IntuitionExperiment(Experiment):

	def __init__(self,total_time=20,output_file='nico',timing_step_scale=15):
		self.point_size = 50 
		self.string_lenght = 5
		self.launching_white_round = False
		self.launching_step = None
		self.white_round_persistence = 0
		self.results = {
			"white_time":[],
			"response_time":[],
			"boule":[],
		}
		Experiment.__init__(self,700,total_time,output_file)
		self.timing_step_scale = timing_step_scale
		self.total_time = total_time
		self.__init_window__()
		self.run()


	def get_random_string(self):
		st = ""
		for i in range(self.string_lenght):
			st += consomn_string[randint(0,19)]
		return st

	def print_random_string(self):
		random_string = self.get_random_string()
		self.canvas.create_text(
			self.window_size/2,
			self.window_size/2,
			text=random_string,
			font="Arial 32 italic",
			fill="blue")

	def print_number(self,number):
		st = self.letter_matching(number)
		self.canvas.create_text(
			self.window_size/2,
			self.window_size/2,
			text=st,	
			font="Arial 32 italic",
			fill="blue")


	def letter_matching(self,number):
		if number == 1:
			return 'OOOOO'
		elif number == 2:
			return 'OOOOO'
		elif number == 3:
			return 'OOOOO'
		elif number == 4:
			return 'OOOOO'
		else:
			return 'OOOOO'
		
	def test_conditions(self):
		return self.launching_white_round

	def right_click(self):
		self.results["boule"].append(True)
		self.results["response_time"].append(self.white_time-time())

	def wrong_click(self):
		self.results["boule"].append(False)
		self.results["response_time"].append(None)

	def loop_step(self):
		if self.timing_step < self.white_round_persistence:
			self.add_point_to_canvas(self.window_size/2,self.window_size/2,"white")
		elif not self.launching_white_round and randint(1,1000) > 985:
			self.launching_white_round = True
			self.launching_step = self.timing_step
			self.white_time = time()+1
			self.print_random_string()
			self.results["white_time"].append(self.white_time)
		elif not self.launching_white_round:
			self.print_random_string()
		elif self.timing_step - self.launching_step == int(1000/self.timing_step_scale):
			self.add_point_to_canvas(self.window_size/2,self.window_size/2,"white")
			self.launching_white_round = False
			self.white_round_persistence = self.timing_step + int(200/self.timing_step_scale)
		elif (self.timing_step - self.launching_step) % int(250/self.timing_step_scale) == (int(250/self.timing_step_scale)-1):
			self.print_number(4-(self.timing_step-self.launching_step)/(int(250/self.timing_step_scale)+1))
		else:
			self.print_random_string()

IntuitionExperiment(**kwargs)
