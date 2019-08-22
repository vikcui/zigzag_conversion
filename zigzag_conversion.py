# author: YANG CUI
"""
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
P   A   H   N
A P L S I I G
Y   I   R

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
P     I    N
A   L S  I G
Y A   H R
P     I
"""

def zigzag_conversion(s, numRows):
    """
    :param s: the input string to convert to zigzag form
    :param numRows: number of rows required in zigzag form
    :return: the zigzag-form string of the input string s
    :time complexity: O(n)
    """
    # if just one row, return the origin string
    if numRows == 1:
        return s
    # compute the length of the input string s
    sLen = len(s)
    zigzagString = ""
    # basic loop structure to fill in the string
    for i in range(numRows):
        interval = 0
        startPos = i
        if i == numRows - 1 or i == 0:
            interval = 2 * numRows - 2
        else:
            interval = (numRows - i - 1) * 2
        while startPos <= sLen - 1:
            if i == numRows - 1 or i == 0:
                zigzagString = zigzagString + s[startPos]
                startPos = startPos + interval
            else:
                zigzagString = zigzagString + s[startPos]
                startPos = startPos + interval
                interval = (2 * numRows - 2) - interval

    return zigzagString

# print(zigzag_conversion("AB", 1))