#import real expressions
import re
import time

def readFile(path):
    message =open(path)
    return message

def checkForSymptoms(message):
    bagOfWords = ['chest pain','sweating','heart ache','fainting','nausea', 'sweat','cold sweat', 'fatigue', 'pain in chest', 'sudden dizziness','lethargy', 'tingling', 'numbness','seizures','difficulty seeing']
    #can read it from a file , for now hardcoded.
    count = 0
    symptomsFound = []
    for line in message:
        count +=1
        if count == 2:
            locationURL = line.strip()
            locationOnMap = locationURL.split('=')
            lat,long = map(float,locationOnMap[1].split(','))
            #print(locationOnMap[1])
            
            
            #print(locationOnMap)
        for word in bagOfWords:
            if re.search(word,line):
                symptomsFound.append(word)
                
    if len(symptomsFound) == 0:
        print('\nNo symptoms found')
        return {'authentic':False,'location':None,'symptoms':None}
    else:
        print('\n\nsymptoms Found =',symptomsFound)
        print('lat=',lat,'\nlong =',long)
        return {'authentic':True,'latitude':lat,'longitude':long,'symptoms':symptomsFound}


if __name__ == '__main__':
    path = input('Enter the path of message file:')
    message = readFile(path)
    startTime = time.time()
    symptoms = {}
    # retuns authenticity of message, location and symptoms as a dictionary
    symptoms = checkForSymptoms(message)
    print('\ndictionary returned =',symptoms)
    print(time.time() - startTime)
