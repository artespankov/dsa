"""
Description
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
Implement encode and decode

Example 1
Input: ["we","really","love","you"]
Output: ["we","really","love","you"]
Explanation:
One possible encode method is: "we:;really:;love:;you"



Example2
Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"

"""

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        return "".join(map(lambda s: f"{len(s)}#{s}", strs))


    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        res = []
        i = 0
        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            word_length = int(str[i:j])
            i = j + 1
            j = i + word_length
            res.append(str[i:j])
            i = j
        return res


if __name__ == "__main__":
    s = Solution()
    encoded = s.encode(["we", "say", ":", "yes"])
    decoded = s.decode(encoded)
    print(encoded)
    print(decoded)

    encoded = s.encode(["we","really","love","you"])
    decoded = s.decode(encoded)
    print(encoded)
    print(decoded)




