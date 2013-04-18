import urllib2, json, time, random

class Weather(object):
    
    def getting(self):
        f = urllib2.urlopen('<---ADD YOUR REFURRAL ADDRESS HERE-->')
        json_string = f.read()
        print "Checked web page"
        f.close()
        
if __name__ == '__main__':
    a = 1
    while a == 1:
        sleeplist = [2, 3, 4, 5, 6, 7, 8, 9]
        timelist = random.choice(sleeplist)
        ask = Weather()
        ask.getting()
        print timelist
        time.sleep(timelist)
