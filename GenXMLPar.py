import sys
import xml.dom.minidom as dm

file = sys.argv[1]


doc = dm.parse(file)
books = {}
if doc.hasChildNodes:
    cnt = 0
    for cn in doc.childNodes:


        if cn.nodeValue != None and len(str(cn.nodeValue).split()) != 0:
            print  'cn Node Name : ', doc.nodeName
            print 'cn Node Value : ', cn.nodeValue

        #print 'cnN', cn.nodeName
        #print 'cnV', cn.nodeValue
        try:
            for i in cn.attributes.keys():
                print cn.nodeName,"Key : ", i
                print cn.nodeName," Val : ", cn.getAttribute(i)
                cnt = cnt + 1
        except AttributeError:
            pass



        if cn.hasChildNodes:

            for cn1 in cn.childNodes:
                if cn1.nodeName == '#text':
                    #print len(cn1.nodeValue.split())
                    if cn1.nodeValue != None and len(str(cn1.nodeValue).split()) != 0:
                        print  'Node Name : ', cn.nodeName
                        print 'Node Value : ', cn1.nodeValue
                #print 'cn1N', cn1.nodeName
                #print 'cn1V', cn1.nodeValue
                try:
                    for i in cn1.attributes.keys():
                        print cn1.nodeName,"Key : ", i
                        print cn1.nodeName," Val : ", cn1.getAttribute(i)
                        #cnt = cnt + 1
                except AttributeError:
                    pass

                if cn1.hasChildNodes:

                    for cn2 in cn1.childNodes:
                        #print 'cn2N', cn2.nodeName
                        #print 'cn2V', cn2.nodeValue
                        if cn2.nodeValue != None and len(str(cn2.nodeValue).split()) != 0:
                            print  'Node Name : ', cn1.nodeName
                            print 'Node Value : ', cn2.nodeValue
                        try:
                            for i in cn2.attributes.keys():
                                print cn2.nodeName,"Key : ", i
                                print cn2.nodeName," Val : ", cn2.getAttribute(i)
                                cnt = cnt + 1
                        except AttributeError:
                            pass

                        if cn2.hasChildNodes:

                            for cn3 in cn2.childNodes:

                                #print 'cn3N', cn3.nodeName
                                #print 'cn3V', cn3.nodeValue
                                if cn3.nodeValue != None and len(str(cn3.nodeValue).split()) != 0:
                                    print  'Node Name : ', cn2.nodeName
                                    print 'Node Value : ', cn3.nodeValue
                                try:
                                    for i in cn3.attributes.keys():
                                        print cn3.nodeName,"Key : ", i
                                        print cn3.nodeName," Val : ", cn3.getAttribute(i)
                                        cnt = cnt + 1
                                except AttributeError:
                                    pass

                                if cn3.hasChildNodes:

                                    for cn4 in cn3.childNodes:
                                        if cn4.nodeValue != None and len(str(cn4.nodeValue).split()) != 0:
                                            print  'Node Name : ', cn3.nodeName
                                            print 'Node Value : ', cn4.nodeValue
                                       # print 'cn4N', cn4.nodeName
                                       # print 'cn4N', cn4.nodeValue
                                        try:
                                            for i in cn4.attributes.keys():
                                                print cn4.nodeName,"Key : ", i
                                                print cn4.nodeName," Val : ", cn4.getAttribute(i)
                                                cnt = cnt + 1
                                        except AttributeError:
                                            pass

