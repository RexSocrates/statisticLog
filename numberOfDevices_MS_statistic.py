# collect short logs (Number of devices test)
# total interactions, total signals, successful rate
# Number of devices : 1 ~ 7

devices_list = [i for i in range(1, 8)]
devices_expResultDic = dict()

for devices in devices_list :
	devices_dic = dict()
	# store the interaction times of each default GU
	devices_dic['interactions'] = []
	# store the signals of each default GU
	devices_dic['signals'] = []
	# store the success rate of each default GU
	devices_dic['rate'] = []

	devices_expResultDic[str(devices)] = devices_dic


for sampleIndex in range(0, 100) :
	sampleResultFolder = 'numOfDevices_MS/sample' + str(sampleIndex) + '/'
	shortLogListInEachFolderPath = 'numOfDevices_MS/' + sampleResultFolder + 'logList.txt'

	filePath = 'numOfDevices_MS/sample' + str(sampleIndex) + '/logList.txt'

	# read short log file name
	logFile = open(filePath)
	logFileNameList = []
	for logName in logFile :
		print(logName)
		logFileNameList.append(logName.replace('\n', ''))

	# read each sample log
	expResultDic = dict()
	for logFileIndex in range(0, len(logFileNameList)) :
		logFileName = logFileNameList[logFileIndex]
		logFilePath = sampleResultFolder + logFileName
		shortLogFile = open(logFilePath)
		expResult = shortLogFile.readline()
		expResultArr = [float(item) for item in expResult.split(',')]

		devices = devices_list[logFileIndex]
		expResultDic[str(devices_list)] = expResultArr

		# put experiment result in each default GU dictionary
		devices_dic = devices_expResultDic[str(devices)]
		interactionArr = devices_dic['interactions']
		interactionArr.append(expResultArr[0])

		signalsArr = devices_dic['signals']
		signalsArr.append(expResultArr[1])

		rateArr = devices_dic['rate']
		rateArr.append(expResultArr[2])

# output the statistical result
import csv

with open('numOfDevices_MS_statistic.csv', 'w') as csvfile :
	fields = ['Number of devices', 'Interaction', 'Signals', 'Success rate']
	writer = csv.DictWriter(csvfile, fieldnames = fields)

	writer.writeheader()

	for devices in devices_list :
		devices_dic = devices_expResultDic[str(devices)]
		interactionArr = devices_dic['interactions']
		signalsArr = devices_dic['signals']
		rateArr = devices_dic['rate']

		print('======= ' + str(devices) + '===========')
		print(len(interactionArr))
		print(len(signalsArr))
		print(len(rateArr))

		avgInteraction = sum(interactionArr) / len(interactionArr)
		avgSignals = sum(signalsArr) / len(signalsArr)
		avgRate = sum(rateArr) / len(rateArr)

		writer.writerow({'Number of devices': devices, 'Interaction': avgInteraction, 'Signals' : avgSignals, 'Success rate': avgRate})


