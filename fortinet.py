import ipaddress
import subprocess

inputFile = ('iplist.txt')      #Change to your filename
ASNumber = ('')          #E.g Google = AS15169
IPlist = ''
subnet, bigList, checkList = [], [], []

def ASNCheckScript(ASN):
    finList = []
    cmd = 'whois -h whois.ripe.net -T route '+ASN+' -i origin | egrep "route: " | awk "{print $NF}"'

    ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = ps.communicate()[0]
    output = output.decode()

    templist = output.split("route:")  # Split by route:
    cleaned = list(filter(None, templist))  # Remove any items in list that are empty
    for i in cleaned:
        i = i.strip(' \t\n\r')
        finList.append(i)
    return finList

try:
    with open(inputFile) as myfile:
        IPlist = myfile.read().splitlines()
except:
    print("No file has been found, defaulting to AS Number")

if len(ASNumber) == 0:
    print("Please provide an input file or an AS Number to check")
    exit()

if len(IPlist) == 0:
    IPlist = ASNCheckScript(ASNumber)

for i in IPlist:
    for x in ipaddress.IPv4Network(i):
        subnet.append(str(x))

counter = 0
with open('fortinet_victim_list_2021.txt', 'r') as f:
    for line in f:
        counter += 1
        if counter > 15:
            bigList.append(line)

for x in bigList:
    checkList.append(x.split(':')[0])

bigList = [i for i in checkList if i in subnet]

if len(bigList) > 0:
    print("The following IP's are affected by this leak;")
    print(bigList)
else:
    print("No matches found.")