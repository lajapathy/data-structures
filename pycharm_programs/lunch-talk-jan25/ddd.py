
d={}
s = "Handover Statistics+Inter Technology handover+LTE-to-S2aGTP handover+Failed"
s_list = s.split("+")
x='d'
for i in xrange(len(s_list)):
    x= x+'['+s_list

x='d[HS][IT]'



for i in xrange(len(s_list)):
    x = d[s_list[i]]
    del s_list[i]

