

def MatchingCharacters(string):
    cnt = [0]
    for ind, char in enumerate(string):
        curr_ind = ind + 1
        while True:
            try:
                new_ind = string.index(char,curr_ind)
                inner_string = string[ind+1:new_ind]
                cnt.append(len(set(inner_string)))
                curr_ind = new_ind + 1
            except Exception:
                break
    
    return max(cnt)


string = 'ahyjakh'
print(MatchingCharacters(string))
string = 'ghececgkaem'
print(MatchingCharacters(string))
string = 'mmmerme'
print(MatchingCharacters(string))
string = 'abccdefghi'
print(MatchingCharacters(string))