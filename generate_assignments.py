import random


def generate_assignments(santas):
    while True:
        santa_dicts = assign_random_giftees(santas)
        if is_derangement(santa_dicts):
            return santa_dicts

def assign_random_giftees(santa_list):
    """
    Creates a randomised list of pairs from a list of names.
    """
    giftee_list = [santa['name'] for santa in santa_list]
    random.shuffle(giftee_list)
    for i, giftee in enumerate(giftee_list):
        santa_list[i]['recipient'] = giftee
    return santa_list

def is_derangement(dict_list):
    """
    Checks if a list of 2-tuples is a derangement, that is, no santa is paired
    with themselves.
    """
    for santa_dict in dict_list:
        if santa_dict['name'] == santa_dict['recipient']:
            return False
    return True