
class Solution:
    def _multiply_digits(self, d1, d2, cin=0):
        val = (int(d1) * int(d2) + cin) % 10
        cout = (int(d1) * int(d2) + cin) / 10
        return val, cout

    def multiplyStrings(self, s1, s2):
        s1 = s1[::-1]
        s2 = s2[::-1]
        result = []
        multiplier = 1
        for c1 in s1:
            carry = 0
            row_result = ''
            for c2 in s2:
                val, carry = self._multiply_digits(c1, c2, carry)
                row_result+=str(val)
            row_result = str(carry) + row_result
            multiplier *= 10
            result.append(int(row_result) * multiplier)
        import pdb;pdb.set_trace()

        return reduce(lambda a,b:a+b , result)

s = Solution()
print s.multiplyStrings('7685', '34')

