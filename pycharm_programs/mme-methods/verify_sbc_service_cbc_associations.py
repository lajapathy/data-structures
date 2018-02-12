def show_sbc_service_cbc_associations_all(self):
    '''
    show sbc-service cbc-associations all
    '''
    dict = {}
    assoc_count = 0

    result = self.send(["show sbc-service cbc-associations all"])
    if result.returncode:
        return CollectResult(1, dict, result.text)

    for line in result.text.split('\n'):
        m = re.match('No matching peers(s)', line)
        if m:
            return CollectResult(1, dict, line)

        m = re.match('(\d+)\s+(\d+)\s+(.*?)\s+(.*?)\s+(\d+\.\d+\.\d+\.\d+)\:(\d+)', line)
        if m:
            if m.group(2) not in dict.keys():
                dict[m.group(2)]=[(m.group(3),m.group(5),m.group(6))]
                assoc_count+=1
            else:
                # If we already have an entry, APPEND SBC service name, IP address and port information as another tuple
                dict[m.group(2)].append((m.group(3),m.group(5),m.group(6)))
                assoc_count += 1
        dict['assoc_count']=assoc_count
    return dict

def verify_sbc_service_cbc_associations(self, count, max_wait=30, retry_wait=10):
        '''
        verify count of SBC associations within max_wait seconds
        return - 0 PASS, 1 FAIL
        '''
        duration = 0
        count = int(count)
        max_wait = int(max_wait)
        retry_wait = int(retry_wait)
        assoc_status_up = 0
        assoc_status_down = 0
        total_assoc_status = 0

        while duration <= max_wait:
            result = self.show_sbc_service_cbc_associations_all()
            if result['assoc_count'] == count:
                logging.info("%s SBC associations are established --> expected %s associations" % (result, count))
                return 0

            if result['assoc_count'] >= count:
                logging.warn(
                    "%s SBC associations found - These are more than expected associations count (%s) - You might want to check/correct the verify count here." % (
                    result, count))

            if duration >= max_wait:
                logging.error(
                    'SBC associations not found as expected - Found associations count (%s) after %d secs while expected are (%s)' % (
                    result, duration, count))
                self.log('FAIL: SBC associations count found (%s) not as expected (%s) in %d secs' % (
                result, count, duration))
                return 1
            duration += retry_wait
            time.sleep(retry_wait)

