import difflib


def check_plagiarism(text1, text2):
    sequence = difflib.SequenceMatcher(None, text1, text2)
    similarity_score = sequence.ratio() * 100
    return similarity_score


def main():
    text1 = input("Enter the first text: ")
    text2 = input("Enter the second text: ")


    similarity_score = check_plagiarism(text1, text2)
    print("Similarity score: {:.2f}%".format(similarity_score))


if __name__ == "__main__":
    main()
