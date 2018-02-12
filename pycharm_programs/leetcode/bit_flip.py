
class BitFlip(object):
    def __init__(self):
        pass

    def _get_binary(self, input):
        #convert input integer to a string, characters of string are binary digits
        import pdb;pdb.set_trace()
        return bin(input)[2:]

    def find_max(self, input):
        bin = self._get_binary(input)
        max_value = input
        

c=BitFlip()
c.find_max(12)

