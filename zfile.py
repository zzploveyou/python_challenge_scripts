import zipfile

'''
#6 http://www.pythonchallenge.com/pc/def/channel.html
'''

zfile = zipfile.ZipFile('channel.zip', 'r')
num = "90052"

st = []
while 1:
    filename = num + ".txt"
    if filename in zfile.namelist():
        content = zfile.read(filename)
        print content
        num = content.split()[-1]

        st.append(zfile.getinfo(filename).comment)
        # raw_input()
    # print num
    if not num.isdigit() and num not in zfile.namelist():
        break

print "".join(st)


'''
****************************************************************
****************************************************************
**                                                            **
**   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  **
**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   **
**   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    **
**   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     **
**   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      **
**   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      **
**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      **
**   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      **
**                                                            **
****************************************************************
 **************************************************************
'''
