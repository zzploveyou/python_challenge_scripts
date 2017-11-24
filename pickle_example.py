import cPickle as pickle
import urllib
url = "http://www.pythonchallenge.com/pc/def/banner.p"
filename = "banner.p"
# urllib.urlretrieve(url, filename)
fw = open(filename, 'r')
a = pickle.load(fw)
for i in a:
    print "".join([j*k for j,k in i])
    # print
fw.close()
