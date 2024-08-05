def Mid(word_):
    isEven = len(word_)%2 == 0
    if isEven:
        return len(word_)//2
    else:
        return len(word_)//2 + 1
word = "racecar"
mid = Mid(word)
isPalindrome = word[:mid] == word[:-mid-1:-1]
print(isPalindrome)