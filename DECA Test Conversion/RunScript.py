import ReadTests

filename = raw_input('Please enter exact text-file name: ')

deca_file = open(filename,'r')
qs = ReadTests.process_file(deca_file)
deca_file.close()
ultra_list = ReadTests.process_question(qs)
file = ReadTests.insert_into_excel(ultra_list)
sprdName = raw_input('Please enter desired spread sheet name: ')
file.save(sprdName + '.xls')