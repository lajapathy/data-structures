
def show_card_table(self):
    dict = {}
    fields_list = []
    abbrevation_dict = {'Univ Data Processing Card 2': 'dpc2', 'Univ Data Processing Card': 'dpc',
                        'System Status Card': 'ssc', 'Fabric & 2x200GB Storage Card': 'fsc',
                        'Packet Services Card 3': 'psc3', 'Packet Services Card 2': 'psc2',
                        'Packet Services Card': 'psc', 'System Management Card': 'smc',
                        'Redundancy Crossbar Card': 'rcc', '2-Port Virtual Card': 'ssi'}

    result = self.send(["show card table"])
    if result.returncode:
        return CollectResult(1, dict, result.text)

    # save all fields in dict for 'show srp info'
    for line in result.text.split('\n'):
        m = re.match('\s*(.*?)\s{2,}(.*?)\s{2,}(.*?)\s{2,}(.+).*\s{2,}(.*)\s*',line)
        if m:
            for field in m.groups():
                fields_list.append(field)
        m = re.match('\s*(\d+)\s*\:\s*(DPC|PSC|PSC2|VC|MMIO|SSC|FSC)\s*(.*)\s*(Active|Standby)\s*(Yes|No)', line)
        if m:
            # Ex: dict[(1, 'DPC')] = ('Active', 'No')
            dict[(m.group(1),m.group(2))] = (m.group(4),m.group(5))
        else:
            return CollectResult(1,dict)

    # Finding out the chassis card type (Whether it's PSC or PSC2 or DPC etc.,)
    # This is based on assumption that "show card table" output has DPC/PSC/PSC2 as the first entry and NOT SMC or FSC
    dict['chassis_card_type'] = dict.keys()[0][1]
    return CollectResult(0, dict)
