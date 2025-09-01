import csv #Used to allow python to manipulate csv files
import os #Paired with glob to allow the script to find the folder its located in automatically so the only setup required is placing it in a folder with the csv files and txt files
import glob
import time #Used to improve user experience through digestibility
import statistics #Used to calculate standard deviation (without manual calculation)

print("Beginning analysis...")

#Important variable related to the location of files
folder = os.path.dirname(os.path.abspath(__file__))

#Dictionary of seasons
seasons = {
   "Summer":["December", "January", "February"],
   "Autumn":["March", "April", "May"],
   "Winter":["June", "July", "August"],
   "Spring":["September", "October", "November"],
}
alltemps = {}
RangeDict = {}
ReverseRangeDict = {}
DevDict = {}
ReverseDevDict = {}
writestring = ""
rangestring = "The 10 highest ranges of the dataset are: \n"
devstring = ""
counter = 0

#Seasonal Average Function, finds the average temperature of any given season
def avgtemp(season):
    avgtemp = 0
    for month in seasons[season]:
        avgtemp = avgtemp + float(row[month])
    return(str(round((avgtemp/3),1))+"°C")

#Function that creates a temporary list that is inserted into the dictionary of all temperatures
def listmaker(row):
    ramlist = []
    for season in seasons:
        for month in seasons[season]:
            ramlist.append(float(row[month]))
    return (ramlist)

#This section reads the data in the csv's and sorts it accordingly into the write file of the first objective and the working list of the second objective
for tempchart in glob.glob(os.path.join(folder, "*.csv")):
    year = str(tempchart)[-8:][:4]
    with open(tempchart, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            writestring = writestring + (f"{row['STATION_NAME']} {year}, Summer: {avgtemp('Summer')}, Autumn: {avgtemp('Autumn')}, Winter: {avgtemp('Winter')}, Spring: {avgtemp('Spring')}\n")
            with open ("average_temp.txt", "w") as avgfile:
                avgfile.write(writestring)
            if (row['STATION_NAME']) in alltemps:
                alltemps[(row["STATION_NAME"])] = alltemps[(row["STATION_NAME"])] + listmaker(row)
            else:
                alltemps[(row['STATION_NAME'])] = listmaker(row)
                
#This loop creates the dictionary containing the range and at the same time the dictionary of ranges, sorted by the range (tie checking)
for place in alltemps:
    RangeDict[place] = round(max(alltemps[place])-min(alltemps[place]),1)
    DevDict[place] = round(statistics.stdev(alltemps[place]),1)
    if RangeDict[place] not in ReverseRangeDict:
        ReverseRangeDict[RangeDict[place]] = [place]
    else:
        ReverseRangeDict[RangeDict[place]].append(place)
    if DevDict[place] not in ReverseDevDict:
        ReverseDevDict[DevDict[place]] = [place]
    else:
        ReverseDevDict[DevDict[place]].append(place)
    
#This creates a second dictionary of ranges in the order of the highest to lowest range
OrderedRange = dict(sorted(RangeDict.items(), key=lambda item: item[1], reverse=True))


for place in OrderedRange:
    rangestring = rangestring + (f'Station: {place}: Range {OrderedRange[place]}°C (Max: {max(alltemps[place])}°C, Min: {min(alltemps[place])}°C)\n')
    counter = counter + 1
    if counter == 10:
        break

for Rngno in dict(sorted(ReverseRangeDict.items(), reverse=True)):
    if len(ReverseRangeDict[Rngno]) >= 2:
        if rangestring.count('ties') == 1:
            rangestring = rangestring + (f'\nRange {Rngno}°C')
            for station in ReverseRangeDict[Rngno]:
                rangestring = rangestring + (f', {station}')
        else:
            rangestring = rangestring + (f'\nThe following ties ocurred:\nRange {Rngno}°C')
            for station in ReverseRangeDict[Rngno]:
                rangestring = rangestring + (f', {station}')
ReverseDevDict = dict(sorted(ReverseDevDict.items(), reverse=True))
ORDevList = list(dict(sorted(ReverseDevDict.items(), reverse=True)).keys())

if len(ReverseDevDict[ORDevList[-1]]) >= 2:
    devstring = devstring + (f'The Most Stable stations have a Stdev of {ORDevList[-1]}°C')
    for station in (ReverseDevDict[ORDevList[-1]]):
        devstring = devstring + (f', {station}')
else:
    devstring = devstring + (f'Most Stable: Station {ReverseDevDict[ORDevList[-1]]}: StdDev {ORDevList[-1]}°C')

if len(ReverseDevDict[ORDevList[0]]) >= 2:
    devstring = devstring + (f'\nThe Most Variable stations have a Stdev of {ORDevList[0]}°C')
    for station in (ReverseDevDict[ORDevList[0]]):
        devstring = devstring + (f', {station}')
else:
    devstring = devstring + (f'\nMost Variable: Station {ReverseDevDict[ORDevList[0]]}: StdDev {ORDevList[0]}°C')

for Devno in dict(sorted(ReverseDevDict.items(), reverse=True)):
    if len(ReverseDevDict[Devno]) >= 2:
        if devstring.count('ties') == 1:
            devstring = devstring + (f'\nStdev {Devno}°C')
            for station in ReverseDevDict[Devno]:
                devstring = devstring + (f', {station}')
        else:
            devstring = devstring + (f'\nThe following ties ocurred:\nStdev {Devno}°C')
            for station in ReverseDevDict[Devno]:
                devstring = devstring + (f', {station}')


with open ("largest_temp_range_station.txt", "w") as rngfile:
    rngfile.write(rangestring)
with open ("temperature_stability_stations.txt", "w") as devfile:
    devfile.write(devstring)

print('\nActions complete')
time.sleep(1)
print('\nResults available in:\naverage_temp.txt\nlargest_temp_range_station.txt\ntemperature_stability_stations.txt')
time.sleep(3)
quit
