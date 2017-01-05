import re
from xlwt.Workbook import *
from xlwt.Style import *

def clean_file(file_name):
	answers = file_name.read()
	answers = answers.replace('\n',' ')
	answers = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff]', '', answers)
	print answers
	return answers

def turn_to_array(cleaned_text):
	line = ''
	answer_array = []
	seek = 0
	for ind in range(1,101):
		temp = str(ind+1)+'.'
		try:
			while temp not in line:
				line += cleaned_text[seek]
				seek += 1
		except IndexError:
			pass
		answer_array.append(line[:len(line)-len(temp)])
		line = ''
		seek -= len(temp)
	print answer_array
	return answer_array

def process_array(arr):
	line = []
	new_arr = []
	for ind in range(len(arr)):
		temp = str(ind+1)+'.'
		tmpline = arr[ind]
		source_loc = tmpline.find('SOURCE')
		line += [tmpline[tmpline.find(temp)+len(temp):len(temp)+3],tmpline[source_loc:source_loc+15]]
		new_arr.append(line)
		line = []
	print new_arr
	return new_arr

def push_data_excel(arr):
	wb = Workbook()
	ws0 = wb.add_sheet('Answers')
	for row in range(0,len(arr)):
		for col in range(0,2):
			ws0.write(row,col,arr[row][col])
	wb.save('wowowow.xls')
	return wb