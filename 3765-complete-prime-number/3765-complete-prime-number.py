class Solution:
    def completePrime(self, num: int) -> bool:
        def is_prime(n):
            if n < 2:
                return False

            i = 2
            while i * i <= n:
                if n % i == 0:
                    return False
                i += 1

            return True

        s = str(num)

        # Check all prefixes
        for i in range(1, len(s) + 1):
            if not is_prime(int(s[:i])):
                return False

        # Check all suffixes
        for i in range(len(s)):
            if not is_prime(int(s[i:])):
                return False

        return True