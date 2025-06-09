'''
메타문자
    . 
    ^ 
    $ 
    * 
    + 
    ? 
    { } 
    [ ]     문자 클래스, [a,b,c] == 하나라도 있는지 | [a-zA-D] == 소문자와 대문자 D까지중 하나라도 있는지 | [^0-9] == 숫자가 아닌지
        \d - 숫자와 매치된다. [0-9]와 동일한 표현식이다.
        \D - 숫자가 아닌 것과 매치된다. [^0-9]와 동일한 표현식이다.
        \s - 화이트스페이스(whitespace) 문자와 매치된다. [ \t\n\r\f\v]와 동일한 표현식이다. 맨 앞의 빈칸은 공백 문자(space)를 의미한다.
        \S - 화이트스페이스 문자가 아닌 것과 매치된다. [^ \t\n\r\f\v]와 동일한 표현식이다.
        \w - 문자+숫자(alphanumeric)와 매치된다. [a-zA-Z0-9_]와 동일한 표현식이다.
        \W - 문자+숫자(alphanumeric)가 아닌 문자와 매치된다. [^a-zA-Z0-9_]와 동일한 표현식이다.
    \ 
    | 
    ( )
'''

data = """
park 800905-1049118
kim  700905-1059119
"""

result = []
for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))
