# Q2_Agreement_Feature.py
subject_features = {
    "he": {
        "number": "singular",
        "person": "third"
    },

    "she": {
        "number": "singular",
        "person": "third"
    },

    "it": {
        "number": "singular",
        "person": "third"
    },

    "they": {
        "number": "plural",
        "person": "third"
    }
}
# Feature structures for verbs
verb_features = {
    "runs": {
        "number": "singular"
    },

    "writes": {
        "number": "singular"
    },

    "run": {
        "number": "plural"
    },

    "write": {
        "number": "plural"
    }
}


def check_agreement(subject, verb):
    """
    Check whether the subject and verb agree
    according to their feature structures.
    """

    subject = subject.lower()
    verb = verb.lower()

    # Check whether subject exists
    if subject not in subject_features:
        return False

    # Check whether verb exists
    if verb not in verb_features:
        return False

    # Get feature structures
    subject_feature = subject_features[subject]
    verb_feature = verb_features[verb]

    # Compare number
    if subject_feature["number"] == verb_feature["number"]:
        return True

    return False


# Main program
print("======================================")
print(" SUBJECT-VERB AGREEMENT CHECKER")
print("======================================")

subject = input("Enter subject: ")
verb = input("Enter verb: ")

result = check_agreement(subject, verb)

print("\nSubject:", subject)
print("Verb:", verb)
print("Agreement:", result)