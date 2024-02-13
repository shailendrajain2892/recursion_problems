nubmer_to_char = ['','',"abc",'def','ghi','jkl','mno','pqrs','tuv','wxyz']
list_of_words = []
def words_from_digit(a, N, temp='', i=0):
    if i == N:
        list_of_words.append(temp)
        return
    if a[i] == '':
        return
    for j in nubmer_to_char[a[i]]:
        words_from_digit(a, N, temp+j, i+1)
    return list_of_words


print(words_from_digit([2, 3], 2))