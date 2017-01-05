from xlwt.Workbook import *
from xlwt.Style import *
	
def process_file(fil):
	ques = ''
	questions = []
	for n in range(0,101):
		temp = str(n+1) + '.'
		while temp not in ques:
			ques = ques + fil.read(1)
		questions.append(ques[:len(ques)-len(temp)])
		ques = ''
		fil.seek(fil.tell()-len(temp))
	return questions
	

def process_question(quest):
	for cnt in range(0,len(quest)):
		temp = quest[cnt].replace('\n','')
		temp = temp.replace('\x0c','')
		quest[cnt] = temp
	master = []
	for qu in quest:
		temp = splice_line(qu)
		master += temp,
	return master

def insert_into_excel(processed_list, ):
	wb = Workbook()
	ws0 = wb.add_sheet('DECAProj')
	ws0.write(0,0,'Question')
	ws0.write(0,1,'Answer Choice 1')
	ws0.write(0,2,'Answer Choice 2')
	ws0.write(0,3,'Asnwer Choice 3')
	ws0.write(0,4,'Answer Choice 4')
	for row in range(1,len(processed_list)):
		for col in range(0,len(processed_list[row])):
			ws0.write(row,col,str(processed_list[row][col]))
	return wb


def splice_line(q):
	temp = []
	dic = {}
	splitList = ['A.','B.','C.','D.']
	for ch in splitList:
		if ch in q:
			if ch == 'A.':
				dic[q.find(ch)] = 'A.'
			elif ch =='B.':
				dic[q.find(ch)] = 'B.'
			elif ch == 'C.':
				dic[q.find(ch)] = 'C.'
			elif ch == 'D.':
				dic[q.find(ch)]= 'D.'
			else:
				pass
	sort_list = sorted(dic)
	sort_list += len(q),
	start = 0
	for end in sort_list:
		temp += q[start:end].strip(),
		start = end
	temp = order_list(temp)
	return temp
		
def order_list(lst):
	temp = []
	tempString = lst[0]
	temp += tempString[tempString.find('.')+1:],
	dic = {}
	count = 0
	for i in range(1,len(lst)):
		if lst[i][:2] == 'A.':
			dic[1] = i
		elif lst[i][:2] == 'B.':
			dic[2] = i
		elif lst[i][:2] == 'C.':
			dic[3] = i
		elif lst[i][:2] == 'D.':
			dic[4] = i
		else:
			pass	
	for j in dic:
		temp += lst[dic[j]],
	return temp