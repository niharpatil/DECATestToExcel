
def handle_questions(f):
    import ReadTests
    qs = ReadTests.process_file(f)
    ultra_list = ReadTests.process_question(qs)
    wb = ReadTests.insert_into_excel(ultra_list)
    return wb

def handle_answers(f):
    import ReadAnswers
    cf = ReadAnswers.clean_file(f)
    ar = ReadAnswers.turn_to_array(cf)
    pr = ReadAnswers.process_array(ar)
    wb = ReadAnswers.push_data_excel(pr)
    wb.save('wowow.xls')
    #return wb
    
if __name__ == '__main__':
	f = file('tester.txt','r')
	handle_answers(f)