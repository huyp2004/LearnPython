# s = 'LVI'
# roman_dict = {
#     'I':1,
#     'V':5,
#     'X':10,
#     'L':50,
#     'C':100,
#     'D':500,
#     'M':1000
# }
# result = 0

# # for i in s:
# #     # if roman_dict[i]
# #     print(f'{result} + {roman_dict[i]} = {result + roman_dict[i]}')
# #     result += roman_dict[i]

# for i in range(len(s)):
#     for j in range(i+1, len(s)):
#         if roman_dict[s[i]] < roman_dict[s[j]]:
#             result += roman_dict[s[j]] - roman_dict[s[i]]
            
#             continue
#         else:
#             result += roman_dict[s[i]] + roman_dict[s[j]]
# print(result)
