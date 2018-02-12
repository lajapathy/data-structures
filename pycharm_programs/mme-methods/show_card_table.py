import re

def show_card_table(self):
    '''
    show card table - collect all fields in tag/value pairs
    options - NA
    # Example entry : dict[1] = {'Slot': 'DPC', 'Card Type' : 'Univ Data Processing Card 2', 'Oper State' : 'Active', 'SPOF' : '-', Attach : ''}
    # result.dict = { 1: { 'Slot': '1', 'Type', 'VC', 'Card Type': '4-Port Virtual Card', 'Oper State': 'Active', 'SPOF': '-', 'Attach': ''} }

    contact: lamadhus@cisco.com
    '''
    dict = {}
    fields_list = []
    result = open('show_card_table_output.txt','r')

    # save all fields in a list for 'show srp info'
    # Example for fields_list
    # ['Slot', 'Card Type', 'Oper State', 'SPOF', 'Attach']
    for line in result.text.split('\n'):
            m = re.match('\s*(.*?)\s{2,}(.*?)\s{2,}(.*?)\s{2,}(.+).*\s{2,}(.*)\s*', line)
            if m:
                for field in m.groups():
                    fields_list.append(field)

        entry_found = False
        for line in result.text.split('\n'):
            m = re.match('\s*(\d+)\s*\:\s*(DPC|PSC|PSC2|VC|MMIO|SSC|FSC)\s*(.*)\s*(Active|Standby)\s*(Yes|No)\s*(.*)', line)
            if m:
                entry_found = True
                dict[m.group(1)] = {fields_list[0] : m.group(2).strip() , fields_list[1] : m.group(3).strip(), fields_list[2] : m.group(4).strip(), fields_list[3] : m.group(5).strip(), fields_list[4] : m.group(6).strip()}
        if not entry_found:
            return dict  # Finding out the chassis card type (Whether it's PSC or PSC2 or DPC etc.,)
    # This is based on assumption that "show card table" output has DPC/PSC/PSC2 as the first entry and NOT SMC or FSC
    dict['chassis_card_type'] = dict['1'][fields_list[1]]
