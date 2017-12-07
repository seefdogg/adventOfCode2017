
def run(data):
    valid = 0
    for line in data:
        words = []
        duplicate = False
        for word in line.split():
            if word in words:
                duplicate = True
                break
            else:
                words.append(word)
        if not duplicate:
            valid += 1
    return valid

def allAnagrams(s):
    ans = []
    if len(s) == 1:
        return [s]
    else:
        char0 = s[0]
        subans = allAnagrams(s[1:])
        for sub in subans:
            for i in range(len(sub)+1):
                ans.append(sub[0:i] + s[0] + sub[i:])
    return ans

def run2(data):
    valid = 0
    for line in data:
        ans = []
        anagram = False
        for word in line.split():
            if word in ans:
                anagram = True
                break
            else:
                curans = allAnagrams(word)
                for c in curans:
                    ans.append(c)
        if not anagram:
            valid += 1
    return valid

if __name__ == '__main__':
    print('--- Advent of Code 2017: Day 04 ---')
    import sys

    filedata = open('input1.txt').readlines()
    num = run(filedata)
    print('valid passphrases: '+str(num))

    num = run2(filedata)
    print('valid passphrases 2: '+str(num))
