def parse_cfg(sentence):
    """
    Validate a sentence using the given CFG
    and construct a parse tree.
    """
    words = sentence.lower().split()
    # A valid sentence must contain exactly 5 words
    if len(words) != 5:
        return None

    det = ["the", "a"]
    nouns = ["student", "teacher", "book"]
    verbs = ["reads", "likes"]

    # Check each grammar rule
    if words[0] not in det:
        return None

    if words[1] not in nouns:
        return None

    if words[2] not in verbs:
        return None

    if words[3] not in det:
        return None

    if words[4] not in nouns:
        return None

    # Construct parse tree
    parse_tree = {
        "S": [
            {
                "NP": [
                    {"Det": [words[0]]},
                    {"N": [words[1]]}
                ]
            },
            {
                "VP": [
                    {"V": [words[2]]},
                    {
                        "NP": [
                            {"Det": [words[3]]},
                            {"N": [words[4]]}
                        ]
                    }
                ]
            }
        ]
    }

    return parse_tree


def print_tree(tree, level=0):
    """
    Display the parse tree in a readable format.
    """

    for key, value in tree.items():

        print("  " * level + key)

        for child in value:

            if isinstance(child, dict):
                print_tree(child, level + 1)

            else:
                print("  " * (level + 1) + child)


# Main program
print("======================================")
print(" CFG PARSER AND PARSE TREE")
print("======================================")

sentence = input("Enter a sentence: ")

tree = parse_cfg(sentence)

if tree is None:
    print("\nInvalid Sentence")
else:
    print("\nValid Sentence")
    print("\nParse Tree:")
    print_tree(tree)