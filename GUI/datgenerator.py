import os.path

#guiData
budget=10000
minGain=1
names=['Test1','Test2','Test3']
rates=["23", "34", "56"]

datFileName='Proje2kt.dat'

if os.path.isfile(datFileName):
	datFile=open(datFileName,'r')
	lines=datFile.readlines()
	datFile.close()
	datFile=open(datFileName,'w')
	datFile.truncate(0)
	datFile.write("budget="+str(budget)+";\n")
	datFile.write("minGain="+str(minGain)+";\n")
	datFile.write("nCurrencies="+str(len(names))+";\n")
	datFile.write("nSamples="+str(len(lines)-6)+";\n")
	datFile.write("names=[")
	for name in names[:-1]:
		datFile.write("\""+name+"\",")
	datFile.write("\""+name+"\"];\n")

	datFile.write("quotes=[\n")
	for line in lines[6:(len(lines)-1)]:
		datFile.write(line)
	datFile.write("[")
	for rate in rates[:-1]:
		datFile.write(rate+",")
	datFile.write(rate+"]\n];")

else:
	datFile=open(datFileName,'a')
	datFile.write("budget="+str(budget)+";\n")
	datFile.write("minGain="+str(minGain)+";\n")
	datFile.write("nCurrencies="+str(len(names))+";\n")
	datFile.write("nSamples=1;\n")
	datFile.write("names=[")
	for name in names[:-1]:
		datFile.write("\""+name+"\",")
	datFile.write("\""+name+"\"];\n")

	datFile.write("quotes=[\n[")
	for rate in rates[:-1]:
		datFile.write(rate+",")
	datFile.write(rate+"]\n];")

datFile.close()