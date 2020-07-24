'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, cur_ind = 0, result = 0):
    if cur_ind + 1 >= len(word):
        return result
    if word[cur_ind] + word[cur_ind+1] == "th":
        result += 1
    cur_ind += 1
    return count_th(word, cur_ind, result)

if __name__ == '__main__':
    print(count_th("the"))
    print(count_th("teeth"))
    print(count_th("hello"))
    print(count_th("thekjkjdsfThfeewth"))
