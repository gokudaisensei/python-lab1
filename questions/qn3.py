"""
Lab Excercise 1: Question 3
"""

# Given Pattern 1
"""
                A
            A       B
        A       B       C
    A       B       C       D
A       B       C       D       E
"""

# Taking the character set
characterSet: str = "ABCDE"

patternListA: list[tuple] = []
tabChar = "\t"
newLine = "\n"

for idx, char in enumerate(characterSet):
    charInLine: str = characterSet[: idx + 1]
    numOfTabs: int = len(characterSet) - idx - 1
    initTabPerLine: str = numOfTabs * tabChar
    tabBetweenChar: str = tabChar * 2
    patternLine = (
        initTabPerLine,
        [(char, tabBetweenChar) for char in charInLine],
        newLine,
    )
    patternListA.append(patternLine)


# Given Pattern 2
"""
*
*   *
*   *   *
*   *   *   *
*   *   *   *   *
"""

character: str = "*"
patternListB: list = list()
for i in range(1, 6):
    chars = ""
    for j in range(i):
        chars += character + tabChar
    patternListB.append(chars)
