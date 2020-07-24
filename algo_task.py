"""Необходимо реализовать функцию, которая принимает в качестве аргумента строку s, содержащую любые буквы латинского алфавита а так-же 
скобки вида (){}[], и выдает в результате наибольшую возможную строку, такую что она является подстрокой бесконечной строки вида sssssss... 
(состоит из бесконечной конкатенации строчек s)  и скобочные символы в ней составляют правильную скобочную последовательность. 
Если такая строка имеет бесконечную длину, вернуть строку "Infinite". 
Также необходимо реализовать тесты. 
Примеры: 
1) Input: }](){ Output: (){} 
2) Input: sh(dh)} Output: sh(dh) 
3) Input: ]h({hdb}b)[ Output: Infinite"""

def string_parser(s):

    s_list = ["(",")","[","]","{","}"]

    count = [s.count(s_list[0]), s.count(s_list[1]),s.count(s_list[2]),s.count(s_list[3]),s.count(s_list[4]),s.count(s_list[5])]

    min_max = [[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]]

    for char in range(len(min_max)):
        for i in range(len(s)):
            if s[i] == s_list[char]:
                if count[char] == 1:
                    min_max[char][0] = i
                    min_max[char][1] = i
                elif min_max[char][0] == -1:
                    min_max[char][0] = i
                elif min_max[char][1] <=i:
                    min_max[char][1] = i

    
    nonpair = 0
    shift = 0
    for i in range(0, len(count), 2):
        if (count[i]+count[i+1])% 2 != 0:
            if count[i] > count[i+1]:
                nonpair = min_max[i][0]
            else:
                nonpair = min_max[i+1][1]
        else:
            if min_max[i+1][1] < min_max[i][0]:
                shift = min_max[i+1][1]

    if nonpair == 0 and shift ==0:
        return "Infinite"
    else:
        return s[nonpair+1:]+s[:nonpair]



if __name__ == '__main__':
    # не обрабатывает правильно неправильную вложенность ("({)}")
    print(string_parser("}](){")) #ok
    print(string_parser("sh(dh)}")) #ok
    print(string_parser("]h({hdb}b)["))#ok