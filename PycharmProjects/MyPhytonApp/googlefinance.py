from bs4 import BeautifulSoup
import json

googFinDict = dict()
with open('files\GoogleFinance.htm') as f:
    file1 = f.readlines()
    googlefinance = BeautifulSoup(str(file1),'lxml')
    sectorsummary = BeautifulSoup(str(googlefinance.find('div', class_="id-secperf sfe-section-major")), 'lxml')
    secsumtable = str(sectorsummary.find('table').get_text())
    secsumtable = secsumtable.replace('\\n','')
    secsumtable = secsumtable.replace('\'', '')
    secsumtable = secsumtable.strip().split(',')
    #print(secsumtable)
    pos = 0
    for i in secsumtable:
        if 'ENERGY' in i.strip().upper() or \
           'BASIC MATERIALS' in i.strip().upper() or \
           'INDUSTRIALS' in i.strip().upper():
            pair = i.strip()
            value = secsumtable[pos+2].strip().replace('%','')
            googFinDict.update({pair: value})
        pos = pos + 1

    #print(googFinDict)

googEnergyDict = dict()
with open('files\Energy.htm') as f:
    file1 = f.readlines()
    googleenergy = BeautifulSoup(str(file1), 'lxml')
    #print(googleenergy.prettify())
    energysummary = BeautifulSoup(str(googleenergy.find('div', class_="sfe-break-bottom")), 'lxml')
    #print(energysummary)
    energytable = str(energysummary.find('table').get_text())
    energytable = energytable.replace('\\n', '')
    energytable = energytable.replace('\'', '')
    energytable = energytable.replace(', Inc', '@*Inc')
    energytable = energytable.strip().split(',')

    googEnergyDict.update({"biggest_gainer_equity": energytable[9].strip().replace('@*Inc', ', Inc')})
    googEnergyDict.update({"biggest_gainer_change": energytable[15].strip().replace('(','').replace(')','').replace('%','')})
    googEnergyDict.update({"biggest_loser_equity": energytable[62].strip().replace('@*Inc', ', Inc')})
    googEnergyDict.update(
        {"biggest_loser_change": energytable[68].strip().replace('(', '').replace(')', '').replace('%', '')})

   # print(googEnergyDict)

googBasicDict = dict()
with open('files\Basic+Materials.htm') as f:
    file1 = f.readlines()
    googlebasic = BeautifulSoup(str(file1), 'lxml')
    basicsummary = BeautifulSoup(str(googlebasic.find('div', class_="sfe-break-bottom")), 'lxml')
    basictable = str(basicsummary.find('table').get_text())
    basictable = basictable.replace('\\n', '')
    basictable = basictable.replace('\'', '')
    basictable = basictable.replace(', Inc', '@*Inc')
    basictable = basictable.strip().split(',')
    googBasicDict.update({"biggest_gainer_equity": basictable[9].strip().replace('@*Inc', ', Inc')})
    googBasicDict.update(
        {"biggest_gainer_change": basictable[15].strip().replace('(', '').replace(')', '').replace('%', '')})

    googBasicDict.update({"biggest_loser_equity": basictable[62].strip().replace('@*Inc', ', Inc')})
    googBasicDict.update(
        {"biggest_loser_change": basictable[68].strip().replace('(', '').replace(')', '').replace('%', '')})
   # print(googBasicDict)


googIndusDict = dict()
with open('files\Industrials.htm') as f:
    file1 = f.readlines()
    googleindus = BeautifulSoup(str(file1), 'lxml')
    indussummary = BeautifulSoup(str(googleindus.find('div', class_="sfe-break-bottom")), 'lxml')
    industable = str(indussummary.find('table').get_text())
    industable = industable.replace('\\n', '')
    industable = industable.replace('\'', '')
    industable = industable.replace(', Inc', '@*Inc')
    industable = industable.strip().split(',')

    googIndusDict.update({"biggest_gainer_equity": industable[9].strip().replace('@*Inc', ', Inc')})
    googIndusDict.update({"biggest_gainer_change": industable[15].strip().replace('(', '').replace(')', '').replace('%', '')})

    googIndusDict.update({"biggest_loser_equity": industable[62].strip().replace('@*Inc', ', Inc')})
    googIndusDict.update({"biggest_loser_change": industable[68].strip().replace('(', '').replace(')', '').replace('%', '')})




   # print(googIndusDict)


energy = '"Energy":{"biggest_gainer":{' + '"equity":"' + googEnergyDict['biggest_gainer_equity'] + '","change":' + googEnergyDict['biggest_gainer_change'] + "},"
energy = energy + '"biggest_loser":{' + '"equity":"' + googEnergyDict['biggest_loser_equity'] + '","change":' + googEnergyDict['biggest_loser_change']+ "},"
energy = energy + '"change":' + googFinDict['Energy'] + '},'
#print(energy)

basicmaterials = '"Basic Materials":{"biggest_gainer":{' + '"equity":"' + googBasicDict['biggest_gainer_equity'] + '","change":' + googBasicDict['biggest_gainer_change'] + "},"
basicmaterials = basicmaterials + '"biggest_loser":{' + '"equity":"' + googBasicDict['biggest_loser_equity'] + '","change":' + googBasicDict['biggest_loser_change']+ "},"
basicmaterials = basicmaterials + '"change":' + googFinDict['Basic Materials'] + '},'
#print(basicmaterials)

industrials = '"Industrials":{"biggest_gainer":{' + '"equity":"' + googIndusDict['biggest_gainer_equity'] + '","change":' + googIndusDict['biggest_gainer_change'] + "},"
industrials = industrials + '"biggest_loser":{' + '"equity":"' + googIndusDict['biggest_loser_equity'] + '","change":' + googIndusDict['biggest_loser_change']+ "},"
industrials = industrials + '"change":' + googFinDict['Industrials'] + '}'

resultado = '{"results":{' + energy + basicmaterials + industrials + '}}'
print(resultado)

try:
    y = json.loads(resultado)
    print(y['results']['Industrials']['change'])

except:
    print("erro no json")


