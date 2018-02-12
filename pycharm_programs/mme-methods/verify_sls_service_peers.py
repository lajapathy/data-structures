import re

def show_sls_service_peers_all():
    '''
    show sls-service peers all - collect SLS peers state
    '''
    dict = {}
    assoc_status = []
    total_count=0
    result = self.send(["show sls-service peers all"])

    for line in result.text.split('\n'):
        m = re.match('No matching service(s)', line)
        if m:
            return CollectResult(1, dict, line)

        m = re.match('MM ESMLC-ID', line)
        if m:
            continue
        m = re.match('-- --------', line)
        if m:
            continue
        m = re.match('Total ESMLC\s*:\s*(\d+)', line)
        if m:
            total_count = m.group(1)
            continue

        m = re.match('^(\d+)\s+(\d+)\s+(UP|DOWN)\s+(\S+)\s+(\d+)\s+((\d+\.){3}\d)\[(UP|DOWN)\]\s+((\d+\.){3}\d)\[(UP|DOWN)\]', line)
        if m:
            esmlc_id=m.group(1) #This will be the master key
            dict[esmlc_id]={'MM': m.group(1), 'AssocStatus' : m.group(3), 'Uptime' : m.group(4), 'Peer-ID' : m.group(5), 'IP-Addresses-1': m.group(6),  'IP-Addresses-2': m.group(9)}
        else:
            logging.error("CLI output for show sls peers full all not as expected" )

        dict['total_esmlc_count'] = total_count
        return dict


    def verify_sls_service_peers(self, count, max_wait=30, retry_wait=10):
        '''
        verify count of SLS peers within max_wait seconds
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
            result = self.show_sls_service_peers_all()
            assoc_status_up = len([x for x in result.values().values() if x in ['UP']])
            assoc_status_down = len([x for x in result.values().values() if x in ['DOWN']])

            if assoc_status_up == count:
                logging.info("%s SLS peers are in UP State --> expected %s" % (assoc_status_up, count))
                return 0
            else:
                if assoc_status_up >= count:
                    logging.warn(
                        "%s SLS peers are UP - These are more than expected peers count (%s) in UP state - You might want to check/correct the verify count here." % (
                        assoc_status_up, count))
                up_state = assoc_status_up
                down_state = assoc_status_down
                total_state = result['total_esmlc_count']
                assoc_status_up = 0
                assoc_status_down = 0
                total_assoc_status = 0

            if duration >= max_wait:
                logging.error('SLS peers UP %s, DOWN %s, Total peers %s after %d secs' % (
                up_state, down_state, total_state, duration))
                self.log('FAIL: SLS peers UP %s not as expected (%s) in %d secs' % (up_state, count, duration))
                return 1
            duration += retry_wait
            time.sleep(retry_wait)
