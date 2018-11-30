#keg 1
berkas = open('L200183159', 'w')
berkas.write('L200183159' + '\n')
berkas.write('03-08-2000'+'\n')
berkas.write('Naura Salsabila'+'\n')
berkas.close()

#-------------------------------------------------------
#KEG 2
berkasNew = open('L200183159', 'r')
NIM = berkasNew.readline()
TTL = berkasNew.readline()
NAMA = berkasNew.readline()
berkasNew.close()

import shelve
berkasNew =shelve.open('ollak.data')
berkasNew['Data'] = [NIM ,TTL ,NAMA]
berkasNew.close()
#--------------------------------------------------------
#keg 3
import shelve

berkasNew = open("L200183159", "r")
NIM = berkasNew.readline()
TTL = berkasNew.readline()
NAMA = berkasNew.readline()
berkasNew.close()

berkasNew = shelve.open("ollak")
berkasNew["Data"] = [NIM, TTL, NAMA]
berkasNew.close()

#--------------------------------------------------------
#keg 4

import shelve

berkasNew = shelve.open("ollak")
print(berkasNew["Data"][0])
print(berkasNew["Data"][1])
print(berkasNew["Data"][2])

