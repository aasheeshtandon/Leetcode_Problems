class Solution:

    def removeSpaces(self, s):
        """
        :type s: str
        :rtype: str
        """
        return (s.strip())

    def validInput(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "" or s == " ":
            return False

        if s[0] != '-' and s[0] != '+':
            if s[0] < '0' or s[0] > '9':
                return False

        if int(s) < -91283472332 or int(s) > 91283472332:
            return False

        return True

    def atoi(self, s):
        """
        :type s: str
        rtype: int
        """
        s = self.removeSpaces(s)
        if self.validInput(s):
            i = 0
            sign = 1
            result = 0
            if s[0] == '-':
                sign = -1
                i = 1
            elif s[0] == '+':
                sign = 1
                i = 1
            while i < len(s):
                result = (result * 10) + ord(s[i]) - ord('0')
                i += 1
            return (result * sign)

        else:
            print("Invalid input")
            return 0


# Driver function to test the Solution Class
if __name__ == '__main__':
    o1 = Solution()
    s = " 9 "
    ans = o1.atoi(s)
    print(ans)
