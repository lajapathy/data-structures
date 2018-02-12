
import pexpect
import sys

class Connect(object):
    def __init__(self,ip,username,password):
        self.ip = ip
        self.username = username
        self.password = password
        self.connect()


    def connect(self):
        self.pexpect_obj = pexpect.spawn('ssh ' + str(username) + '@' + self.ip)
        c = self.pexpect_obj.expect(['Are you sure','password :',pexpect.TIMEOUT])
        if c==0:
            self.pexpect_obj.send('yes')
            self.pexpect_obj.expect('password:')
            self.pexpect_obj.expect(self.password)
            self.pexpect_obj.expect('#')
        elif c==1:
            self.pexpect_obj.expect(self.password)
            self.pexpect_obj.expect('#')
        else:
            print 'Error connecting to the remote device. Aborting'
            sys.exit(1)


