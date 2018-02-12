def verify_mme_statistics(self,*stats_checks):
    '''
        Usage : verify_mme_statistics[('',4000),('',5000)]

    '''
    result = self.generic_collector(['show mme-service statistics'],role="Active")
    for stats_check in stats_checks:
        #We check each tuple
        if result.text[stats_check[0]] < stats_check[1]:
            logging.error(str(stats_check[0]) + ' not within expected range')
            msg = str(stats_check[0]) + ' not within expected range'
            return SystestResult(1,msg)
        else:
            logging.info(str(stats_check[0]) + ' within expected range')

    msg = 'All MME stats check passed'
    return SystestResult(0,msg)
