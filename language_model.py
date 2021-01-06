import random

punctuations = '''()-[]{};:'"\<>/?@#$%^&*_~|'''

# returns a list of all the words in the file in order
# as if all the poems combined into on long continuous poem


def parse_input(input_file):
    starting_word_count = {}
    words_list = []
    current_rhyme = ''
    rhyme_list = []
    for line in input_file:
        if line.startswith("\n") or line.strip()=="":
            pass
        # this line is part of the rhyme
        else:
            rhyme_list.append(line.strip())
        # this line is a title
     
    # last poem
   
    # rhyme is a string representing each poem
    for rhyme in rhyme_list:

        # each poem split into list
        split_str = rhyme.replace('\n','').lower().split()
       
        # flag to check if this is the first word in poem
        for word in split_str:
            for char in word:
                if char in punctuations:
                    word = word.replace(char, '')
            words_list.append(word)
    # sum up the total number of poems
    total = sum(starting_word_count.values())
    # divide each value in the dict by the total, 
    # inorder to get probabilities
    pi = {k: v / total for k, v in starting_word_count.items()}
    
    # print(words_list)
    # split_str = file_string.replace('\n','').lower().split()

    # split_str = file_string.replace('\n','').lower().split()

    # words_list = []
    # for word in split_str:
    #     for char in word:
    #         if char in punctuations:
    #             word = word.replace(char, '')
    #     words_list.append(word)
# method 2
        # if word not in words_list:
        #     words_list.append(word)

    # return words_list, list(set(words_list)), pi
    return words_list, pi

# takes in a list of words
def create_transition_matrix(words):
    d = {}
    prev = words[0]
    curr = words[1]

    for next in words[2:]:
        if prev in d.keys():
            if curr in d[prev].keys():
                if next in d[prev][curr].keys():
                    d[prev][curr][next] += 1
                else:
                    d[prev][curr][next] = 1
            else:
                d[prev][curr] = {}
                d[prev][curr][next] = 1
        else:
            d[prev] = {}
            d[prev][curr] = {}
            d[prev][curr][next] = 1
        prev = curr
        curr = next

    
    for first, first_vals in d.items():
        for second, second_vals in first_vals.items():
            total_sum = sum(second_vals.values())
            # print(total_sum, "= Number of times for ", first, "+", second, "+ _______")
            for third, third_vals in second_vals.items():
                second_vals[third] = third_vals / total_sum 
                # print(third_vals)
    return d

# P is the transition matrix
def generate_poem(pi, P):
    new_rhyme = []
    # starting word
    # add index [0] because random.choices returns list of length 1
    # prev_word = random.choices(list(pi.keys()), weights = pi.values())[0]
    prev_word = "accordingly"
    new_rhyme.append(prev_word)

    # randomly select the second word from possible words that 
    # follow start word
    # curr_word = random.choices(list(P[prev_word].keys()))[0]
    curr_word = "we"
    new_rhyme.append(curr_word)

    i = 2

    while i != 600:
        next_word = random.choices(list(P[prev_word][curr_word].keys()), weights = P[prev_word][curr_word].values())[0]
        new_rhyme.append(next_word)
        
        prev_word = curr_word
        curr_word = next_word
        i += 1

        if i % 20 == 0:
            new_rhyme.append('\n')


    return ' '.join(new_rhyme)

 

    print(start)
def main():
    input_file = open("plato.txt", "r")
    words_list,  pi = parse_input(input_file)
    # print(len(words_list))
    P = create_transition_matrix(words_list)
    rhyme = generate_poem(pi, P)
    print(rhyme)
    print()
    print("Number of words from training (not unique)", len(words_list))
    print("Number of unique words", len(set(words_list)))


    # print(sum(pi.values()))
    # print(P["snake,"])
    # print(random.choices(list(P["mary"].keys())))
    # print(sum(P['i']['love'].values()))
    # print(random.choices(list(P["mary"]["she"].keys()))[0])


    # lst = read_sequences(input_file.read())
    # print(lst)
            


if __name__ == "__main__":
    main()
