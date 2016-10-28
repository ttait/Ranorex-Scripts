#!/usr/bin/python
# Look on craigs for cheap tickets, xbox equipment & iphones
import re
import urllib
import time
import MySQLdb
import exceptions

class tix:
    def __init__(self, link):
    
        time.sleep(0)
        f = urllib.urlopen(link)
        myfile = f.read()

        nam = str(re.findall('hdrlnk"\>[a-zA-Z0-9 ]*</a>[\t\n\r ]+</span>[\t\n\r ]+<span class="l2">[\t\n\r ]+<span class="price"\>\$[,.0-9]*', myfile))

        nam = nam.replace('</a>',"")
        nam = nam.replace('</span></a>',"") 
        nam = nam.replace('</span>',"") 
        nam = nam.replace("<span class=\"l2\">","") 
        nam = nam.replace("<span class=","")
        nam = nam.replace("$","")

        snam = re.split('[\'\"][a-z]+"\>', nam)

        try:
            mydb = MySQLdb.connect(host = 'localhost',
                                    user = 'user',
                                    passwd = 'passwd',
                                    db = 'tkts')
            cur = mydb.cursor()

            i=0
            for sn in snam:

                if i > 1:
                    sn=sn.replace("',","")
                    sn=sn.replace("']","")
                    statement = """INSERT INTO concert(act, price) VALUES("%s", "%s")""" %(osn,sn)

                    cur.execute(statement)
                    i=0
                i=i+1  
                osn = sn

            cur.execute("""INSERT INTO concert(act, price) VALUES("Steve Hackett", "65.00")""") 
            cur.execute("""INSERT INTO concert(act, price) VALUES("Other Lives", "12.00")""")
            cur.execute("""INSERT INTO concert(act, price) VALUES("theFIXX", "25.00")""")
            cur.execute('SELECT * FROM concert WHERE price <= 250')
            results = cur.fetchall()
            for record in results:
                rec = re.sub("[\t\n\r]+","",record[0])
                print rec, " $", record [1]
            time.sleep (15)
        except:
            print ("Start mySql")    
tix("http://portland.craigslist.org/search/wsc/moa")
tix("http://portland.craigslist.org/tia")
tix("http://portland.craigslist.org/search/vga?query=xbox+one+console")
    
   

    
                
                    
