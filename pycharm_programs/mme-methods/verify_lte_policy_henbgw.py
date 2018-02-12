import re

def verify_lte_policy_henbgw(self, henbgw_count_expected, *mme_service_tuple):
    '''
    Usage : verify_lte_policy_henbgw[henbgw_count = 55,(mme_svc_1,henbdb1,henbtype1),(mme_svc_2,henbdb2,henbtype2)]
    '''
    for chassis in self.get_dut_list():
        #Get henbdb name from config
        config_lines_object = self.send(["show config"], chassis)
        if config_lines_object.returncode:
            msg = 'unable to retrive config'
            return SystestResult(1, msg)
        else:
            config_lines = config_lines_object.text
            #Find henbdb name configured in the configuration
            for line in config_lines:
                if "associate henbgw-mgmt-db" in line:
                    henbdb_name_from_config = re.match('\s*associate henbgw-mgmt-db\s*(.*)',line).group(1)
        #Find henbdb name from CLI output
        result = self.send(['show lte-policy mme henbgw mgmt-db summary'],chassis)
        if result.returncode:
            logging.error('Unable to retrieve henbdb name from CLI output')
            logging.error(result.text)
            return SystestResult(1, result.text)
        else:
            for line in result.text:
                if "HenbGW Management DB " in line:
                    henbdb_name_cli = re.match('\s*HenbGW Management DB\s*(.*)',line).group(1)
        #Compare henbdb values
        if henbdb_name_from_config != henbdb_name_cli:
            msg = 'HENB-DB names doesnt match'
            return SystestResult(1, msg)
        logging.info('HENB-DB names match. Proceeding')

        #Verify count of HeNBGWs
        result = self.send(['show lte-policy mme henbgw mgmt-db name '+str(henbdb_name_cli)])
        if result.returncode:
            logging.error('Error retrieving show lte-policy mme henbgw mgmt-db name '+str(henbdb_name_cli) +' CLI output')
            msg = 'Error retrieving show lte-policy mme henbgw mgmt-db name '+str(henbdb_name_cli) +' CLI output'
            return SystestResult(1, result.text)
        else:
            henbgw_count = 0
            for line in result.text:
                if "HenbGW Global Enbid" in line:
                    henbgw_count+=1
            if henbgw_count != henbgw_count_expected:
                msg = 'HeNBGW count doesnt match. Expected = '+str(henbgw_count_expected)+' Actual = '+str(henbgw_count)
                return SystestResult(1, msg)
            else:
                logging.info('HeNBGW count matched. Expected = '+str(henbgw_count_expected)+' Actual = '+str(henbgw_count))

        #Verify mme-service HeNBGW DB name and type
        henb_db_from_cli_output = ''
        for tuple in mme_service_tuple:
            result = self.send(['show mme-service name '+str(tuple[0])])
            if result.returncode:
                logging.error('Unable to retrieve CLI output - show mme-service name '+str(tuple[0]))
                logging.error(result.text)
                return SystestResult(1, result.text)
            else:
                cli_output = result.text
                for line in cli_output:
                    if "HenbGW Management DB" in line:
                        henb_db_from_cli_output = re.match('\s*HenbGW Management DB\s*:\s*(.*)',line).group(1)
                        if henb_db_from_cli_output != tuple[1]:
                            logging.error('Incorrect HENBGW Mgmt DB name. Actual = '+str(henb_db_from_cli_output)+'. Expected = '+str(tuple[1]))
                            msg = 'Incorrect HENBGW Mgmt DB name. Actual = '+str(henb_db_from_cli_output)+'. Expected = '+str(tuple[1])
                            return SystestResult(1, msg)
                    if "HENBGW HeNodeB Type" in line:
                        henb_type_from_cli_output = re.match('\s*HENBGW HeNodeB Type\s*:\s*(.*)',line).group(1)
                        if henb_type_from_cli_output != tuple[1]:
                            logging.error('Incorrect HENBGW Mgmt Type. Actual = '+str(henb_type_from_cli_output)+'. Expected = '+str(tuple[2]))
                            msg = 'Incorrect HENBGW Mgmt DB name. Actual = '+str(henb_type_from_cli_output)+'. Expected = '+str(tuple[2])
                            return SystestResult(1, msg)
        msg = 'All checks done. No issues found'
        return SystestResult(0,msg)



