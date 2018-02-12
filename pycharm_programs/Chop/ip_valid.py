
import re
def validate_ip(ip):
    octet_list=ip.split('.')
    if '' in octet_list:
        return False
    if not octet_list:
        return False
    if len(octet_list)!=4:
        return False

    for octet in octet_list:
        if not re.match('^((1\d{0,1}\d{0,1})|(\d{0,1}\d{0,1})|(2[0-4]\d{1})|(25[0-5]{0,1}))$',octet):
            return False

    return True

print validate_ip('1.1.1.255')
print validate_ip('1.1.1.1')
print validate_ip('0.0.0.0')
print validate_ip('')
print validate_ip('1.1.1.2553')
print validate_ip('2553.1.1.253')
print validate_ip('a.a.a.a')
print validate_ip('1.1.11.s')
print validate_ip('100 .2.3.4')
print validate_ip('...')
print validate_ip('..22.')
print validate_ip('24.23.22.')
