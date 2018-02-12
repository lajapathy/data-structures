
systest.py

import re

    def verify_mmemgr_count(self):
        # database for abbrevation of card type
        abbrevation_dict = {'Univ Data Processing Card 2': 'dpc2', 'Univ Data Processing Card': 'dpc',
                            'System Status Card': 'ssc', 'Fabric & 2x200GB Storage Card': 'fsc',
                            'Packet Services Card 3': 'psc3', 'Packet Services Card 2': 'psc2',
                            'Packet Services Card': 'psc', 'System Management Card': 'smc',
                            'Redundancy Crossbar Card': 'rcc', '2-Port Virtual Card': 'ssi'}

        # database for default and max number of mmemgr per sesscard and per chassis
        default_num_mmemgr_per_sesscard_db = {('psc', '19.2'): 1, ('psc', '20.0'): 1, ('psc', '21.0'): 1,
                                           ('psc2', '19.2'): 1, ('psc2', '20.0'): 1, ('psc2', '21.0'): 1,
                                           ('psc3', '19.2'): 1, ('psc3', '20.0'): 1, ('psc3', '21.0'): 1,
                                           ('dpc', '19.2'): 4, ('dpc', '20.0'): 4, ('dpc', '21.0'): 4,
                                           ('dpc2', '19.2'): 6, ('dpc2', '20.0'): 6, ('dpc2', '21.0'): 8,
                                           ('ssi', '19.2'): 2, ('ssi', '20.0'): 2, ('ssi', '21.0'): 2}
        max_num_mmemgr_per_sesscard_db = {('psc', '19.2'): 2, ('psc', '20.0'): 2, ('psc', '21.0'): 2,
                                       ('psc2', '19.2'): 2, ('psc2', '20.0'): 2, ('psc2', '21.0'): 2,
                                       ('psc3', '19.2'): 2, ('psc3', '20.0'): 2, ('psc3', '21.0'): 2,
                                       ('dpc', '19.2'): 6, ('dpc', '20.0'): 6, ('dpc', '21.0'): 6,
                                       ('dpc2', '19.2'): 6, ('dpc2', '20.0'): 6, ('dpc2', '21.0'): 8,
                                       ('ssi', '19.2'): 2, ('ssi', '20.0'): 2, ('ssi', '21.0'): 2}
        default_num_mmemgr_per_chassis_db = {('psc', '19.2'): 12, ('psc', '20.0'): 12, ('psc', '21.0'): 12,
                                          ('psc2', '19.2'): 12, ('psc2', '20.0'): 12, ('psc2', '21.0'): 12,
                                          ('psc3', '19.2'): 12, ('psc3', '20.0'): 12, ('psc3', '21.0'): 12,
                                          ('dpc', '19.2'): 24, ('dpc', '20.0'): 24, ('dpc', '21.0'): 24,
                                          ('dpc2', '19.2'): 36, ('dpc2', '20.0'): 36, ('dpc2', '21.0'): 48,
                                          ('ssi', '19.2'): 2, ('ssi', '20.0'): 2, ('ssi', '21.0'): 2}
        max_num_mmemgr_per_chassis_db = {('psc', '19.2'): 12, ('psc', '20.0'): 12, ('psc', '21.0'): 12,
                                      ('psc2', '19.2'): 12, ('psc2', '20.0'): 12, ('psc2', '21.0'): 12,
                                      ('psc3', '19.2'): 12, ('psc3', '20.0'): 12, ('psc3', '21.0'): 12,
                                      ('dpc', '19.2'): 24, ('dpc', '20.0'): 24, ('dpc', '21.0'): 24,
                                      ('dpc2', '19.2'): 36, ('dpc2', '20.0'): 36, ('dpc2', '21.0'): 48,
                                      ('ssi', '19.2'): 2, ('ssi', '20.0'): 2, ('ssi', '21.0'): 2}

        for chassis in self.get_dut_list():

            encountered_cli = False

            # Get build version
            # Ex: 21.1.M0.65811
            build_version_match_obj = re.match('(\d+\.\d+)\..*',self.get_info('version'))
            if build_version_match_obj:
                build_version = build_version_match_obj.group(1)
            else:
                self.log('Image version not found.')

            # Get card type
            dict = self.show_card_table(self)[1]
            card_type = abbrevation_dict[dict['chassis_card_type']]
            default_num_mmemgr_per_sesscard = default_num_mmemgr_per_sesscard_db[(card_type,build_version)] #A
            max_num_mmemgr_per_sesscard = max_num_mmemgr_per_sesscard_db[(card_type,build_version)] #B
            default_num_mmemgr_per_chassis = default_num_mmemgr_per_chassis_db[(card_type,build_version)] #C
            max_num_mmemgr_per_chassis = max_num_mmemgr_per_chassis_db[(card_type,build_version)] #D
            mmemgr_count_configured = False
            per_sesscard_mmemgr_count_configured = False
            # Get number of session cards
            num_active_session_cards = len([value for value in dict.values() if value['slot'] == card_type]) #G

            # get config lines with the desired configurations, in configuration FILE
            config_lines = self.check_config('task facility mmemgr',chassis)

            # Extract max_mmemgr_count and per_sesscard_mmemgr_count from CONFIG FILE
            for line in config_lines:
                m = re.match('.*task facility mmemgr max\s*(\d+)\s*',line)
                if m:
                    user_defined_mmemgr_count =  m.group(1)
                    mmemgr_count_configured = True
                m = re.match('.*task facility mmemgr per-sesscard-count\s*(\d+)\s*', line)
                if m:
                    user_defined_per_sesscard_mmemgr_count = m.group(1)
                    per_sesscard_mmemgr_count_configured = True

            config_lines = self._send(["show config"], chassis)

            if mmemgr_count_configured:
                # Check mmemgr  _count from SHOW CONFIG CLI
                for line in [line for line in config_lines if 'task facility mmemgr max' in line]:
                    encountered_cli = True
                    if re.match('\s*task facility mmemgr max\s*(\d+)\s*', line):
                        #F
                        user_configured_max_mmemgr_per_chassis = re.match('\s*task facility mmemgr max\s*(\d+)\s*',line).group(1)
                        if user_configured_max_mmemgr_per_chassis > max_num_mmemgr_per_chassis:
                            return 1

            elif not encountered_cli:
                # No explicit configuration. Default values are being used.
                #Check that show config | grep doesnt show anything
                user_configured_max_mmemgr_per_chassis = default_num_mmemgr_per_chassis
                if [line for line in config_lines if 'task facility mmemgr max' in line]:
                    return 1

            #Reset this flag, to re-use it for "per_sesscard_mmemgr_count"
            encountered_cli = False

            if per_sesscard_mmemgr_count_configured:
                #Check per_sesscard_mmemgr_count from SHOW CONFIG CLI
                for line in [line for line in config_lines if 'task facility mmemgr per-sesscard-count' in line]:
                    encountered_cli = True
                    if re.match('\s*task facility mmemgr per-sesscard-count 8\s*(\d+)\s*', line):
                        #E
                        user_configured_max_mmemgr_per_sesscard = re.match('\s*task facility mmemgr max\s*(\d+)\s*', line).group(1)
                        if user_configured_max_mmemgr_per_sesscard > max_num_mmemgr_per_chassis:
                            return 1

            elif not encountered_cli:
                # No explicit configuration. Default values are being used.
                # Check that show config | grep doesnt show anything
                user_configured_max_mmemgr_per_sesscard = default_num_mmemgr_per_sesscard
                if [line for line in config_lines if 'task facility mmemgr per-sesscard-count' in line]:
                    return 1


            # Calculate expected number of mmemgrs to be spawned

            if mmemgr_count_configured and per_sesscard_mmemgr_count_configured:
                #expected_mmemgr_count = min(min(E * G, F), min (B * G, D))
                expected_mmemgr_count = min(min(user_configured_max_mmemgr_per_sesscard * num_active_session_cards, user_configured_max_mmemgr_per_chassis), min (max_num_mmemgr_per_sesscard * num_active_session_cards, max_num_mmemgr_per_chassis))

            else :
                #expected_mmemgr_count = min(A * G, C)
                expected_mmemgr_count = min ( default_num_mmemgr_per_sesscard * num_active_session_cards, default_num_mmemgr_per_chassis)

            #Get actual number of mmemgr count using Prashant's method
            actual_mmemgr_count_dict = self.show_task_resources('mmemgr')[1]
            actual_mmemgr_count = len(actual_mmemgr_count_dict.keys())

            #Compare
            if actual_mmemgr_count == expected_mmemgr_count:
                logging.info('Found expected')
                return 0
            else:
                return 1

#In collect.py

    def check_config(self,keyword,chassis):
        config_cli_list=[]
        #Get chassis configuration file.
        relative_chassis_config_path = self.get_info('config_file', chassis)
        #This will return relative path only. So, we add the CWD
        abs_path = os.path.join(os.getcwd(),relative_chassis_config_path)

        #Search for lines in the configuration with the desired keyword.
        config_cli_list = [line for line in open(abs_path,'r') if keyword in line]

        return config_cli_list