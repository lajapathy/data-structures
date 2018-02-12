import re

def henbgw_count(self):
    for chassis in self.get_dut_list():
        config_lines = self._send(["show config"], chassis)
        henbgw_mgmt_db_name_from_config = ''
        henbgw_mgmt_db_name_from_cli_output = ''
        for line in config_lines:
            if "associate henbgw-mgmt-db" in line:
                henbgw_mgmt_db_name_from_config = re.match('\s*associate henbgw-mgmt-db\s*(.*)\s*',line).group(1)
                break
        cli_output = self._send(["show lte-policy mme henbgw mgmt-db summary"], chassis)
        for line in cli_output:
            if "HenbGW Management DB" in line:
                henbgw_mgmt_db_name_from_cli_output = re.match('\s*HenbGW Management DB\s*(.*)\s*',line).group(1)
                break

        if henbgw_mgmt_db_name_from_cli_output != henbgw_mgmt_db_name_from_config:
            return SystestResult(1, henbgw_mgmt_db_name_from_cli_output)

        #Now, we verify henbgw count

