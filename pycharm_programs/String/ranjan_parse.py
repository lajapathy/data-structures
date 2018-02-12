import sys,os,re

def create_dict():
    inner_dict = {}
    my_dict = {}


    for line in open('datafile1','r+'):
        print '%s' %line
        m = re.match('(\d+)\s+(\d+)\s+(.*)\s+([a-zA-Z-0-9]+)\s+(.*)$', line)
        if m:
            #print m
            #print 'Mod %s, Ports %s, Module-Type %s, Model %s, Status %s' %(m.group(1), m.group(2), m.group(3), m.group(4), m.group(5))
            inner_dict['Ports'] = m.group(2).strip()
            inner_dict['Module-Type'] = m.group(3).strip()
            inner_dict['Model'] = m.group(4).strip()
            inner_dict['Status'] = m.group(5).strip()
            my_dict['Mod', m.group(1)] = inner_dict

    return my_dict

print create_dict()