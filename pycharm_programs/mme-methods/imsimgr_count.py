
    def verify_imsimgr_count(self):
        for chassis in self.get_dut_list():
            # get config lines with the desired configurations, in configuration FILE
            config_lines = self.check_config('task facility mmemgr', chassis)
            imsimgr_count_configured = False
            #Check if desired configuration is present
            for line in config_lines:
                m = re.match('.*facility imsimgr max\s*(\d+)\s*',line)
                if m:
                    user_defined_imsimgr_count =  m.group(1)
                    imsimgr_count_configured = True

            #Check whether show config shows the expected output
            config_lines = self._send(["show config"], chassis)
            if imsimgr_count_configured:
                # Check imsimgr count from SHOW CONFIG CLI. Verify that it's the same
                for line in [line for line in config_lines if 'task facility imsimgr max' in line]:
                    encountered_cli = True
                    if re.match('\s*task facility imsimgr max\s*(\d+)\s*', line):
                        user_configured_imsimgr_per_chassis = re.match('\s*task facility mmemgr max\s*(\d+)\s*',line).group(1)
                        if user_configured_imsimgr_per_chassis != user_defined_imsimgr_count:
                            return 1

            if not imsimgr_count_configured:
                user_defined_imsimgr_count = 8 #Default number of imsimgrs

            # Get actual number of mmemgr count using Prashant's method
            actual_imsimgr_count_dict = self.show_task_resources('imsimgr')[1]
            actual_imsimgr_count = len(actual_imsimgr_count_dict.keys())

            # Compare
            if actual_imsimgr_count == user_defined_imsimgr_count:
                logging.info('Found expected')
                return 0
            else:
                return 1

