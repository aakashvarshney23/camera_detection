def checkInclusion(s1, s2):
    if len(s1) > len(s2): return False
    hashTable = {}
    slidingWindow = {}
    lengthOfS1 = len(s1)
    for char in s1:
        if char not in hashTable:
            hashTable[char] = 1
        else:
            hashTable[char] += 1
    for i in range(len(s2)):
        char = s2[i]
        if char not in slidingWindow:
            slidingWindow[char] = 1
        else:
            slidingWindow[char] += 1
        if i - lengthOfS1 >= 0:
            slidingWindow[s2[i - lengthOfS1]] -= 1
            if slidingWindow[s2[i - lengthOfS1]] == 0:
                del slidingWindow[s2[i - lengthOfS1]]
            # Time is O(1), since the maximum num of hashTable is 26
        if slidingWindow == hashTable:
            return True
    return False


def main():

     a = checkInclusion("dog", "god")
     print (a)


if __name__ == "__main__":
    main()