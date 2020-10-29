from os import walk


'''
    dict: dictionary containing for each term (key) a list of docIDs (posting List of integers)
    file_lexicon: <term,length posting list> for each line
    file_postings: contains, one for line, the posting list of each term (sorted list of integer docIDs)
    
'''

PATH_DIRECTORY = "data/documents/"
PATH_DICTIONARY = "data/dictionary/"
FORMAT = ".dat"
LEXICON_NAME = "lexicon.txt"
POSTING_NAME = "-postings.txt"
COMPRESSED_POSTING_NAME = "-compressed_postings.txt"


def create_index(dictionary, file_lexicon=LEXICON_NAME, file_postings=POSTING_NAME, path=PATH_DICTIONARY):
    if file_lexicon:
        f1 = open(path + file_lexicon, 'w')
    f2 = open(path + file_postings, 'w')
    voc = list(dictionary.keys())
    voc.sort()
    for term in voc:
        if file_lexicon:
            f1.write("{} {}\n".format(term, len(dictionary[term])))
        for doc_id in dictionary[term]:
            f2.write("{} ".format(doc_id))
        f2.write("\n")
    if file_lexicon:
        f1.close()
    f2.close()


def read_postings(file_postings=POSTING_NAME):
    try:
        f1 = open(PATH_DICTIONARY + file_postings, 'r')

        line_posting_lists = []
        for posting_list in f1:
            line_posting_lists.append(posting_list.split())
        f1.close()
        return line_posting_lists

    except IOError:
        print("File ", file_postings, 'r')


def read_index(file_postings=POSTING_NAME, file_lexicon=LEXICON_NAME, path=PATH_DICTIONARY):
    try:
        f1 = open(path + file_lexicon, 'r')
    except IOError:
        print("File ", file_lexicon, "doesn't exist!")
    try:
        f2 = open(path + file_postings, 'r')
    except IOError:
        print("File ", file_postings, 'r')
    new_dict = {}
    for line in f1:  # mange study number of post_list
        p = f2.readline()
        l = line.split()
        pl = p.split()
        new_dict[l[0]] = [int(el) for el in pl]

    f1.close()
    f2.close()
    return new_dict


# Parse all .dat files in the directory
def get_files(directory=PATH_DIRECTORY):
    files = []
    i = 0
    for (dirpath, dirnames, filenames) in walk(directory):
        for f in filenames:
            if FORMAT in f:
                files.append(dirpath + f)
                i += 1
    return files


def SPIMI_indexer(files):
    dictionary = {}

    doc_id = 0
    tot_set = 0
    tot_tokens = 0
    tot_postings = 0

    for f in files:
        count_tokens = 0
        count_postings = 0

        try:
            file = open(f, 'r')
            tot_set += 1
            for line in file:
                ll = line.split()

                if len(ll) != 0:
                    if ll[0] == ".I":
                        doc_id += 1
                    elif ll[0] != ".W":
                        count_tokens += len(ll)
                        for el in ll:
                            if el.isalpha() or el.isdigit():
                                if el in dictionary:
                                    lenl = len(dictionary[el])
                                    if doc_id != dictionary[el][lenl - 1]:
                                        dictionary[el].append(doc_id)
                                        count_postings += 1
                                else:
                                    dictionary[el] = [doc_id]
                                    count_postings += 1

            file.close()
        except IOError:
            print("File ", f, "doesn't exist!")

        # print(f, " -set :", tot_set, " tokens: ", count_tokens)
        tot_postings += count_postings
        tot_tokens += count_tokens
    # print("Total no. of tokens:", tot_tokens)
    print("Total no. of documents:", doc_id)
    print("Total no. of terms:", len(dictionary))
    print("Total no. of postings:", tot_postings)
    return dictionary, doc_id


def create_dictionary():
    list_files = get_files()
    return SPIMI_indexer(list_files)


