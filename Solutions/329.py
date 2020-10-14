"""
Problem:

The stable marriage problem is defined as follows:

Suppose you have N men and N women, and each person has ranked their prospective
opposite-sex partners in order of preference.

For example, if N = 3, the input could be something like this:

guy_preferences = {
    'andrew': ['caroline', 'abigail', 'betty'],
    'bill': ['caroline', 'betty', 'abigail'],
    'chester': ['betty', 'caroline', 'abigail'],
}
gal_preferences = {
    'abigail': ['andrew', 'bill', 'chester'],
    'betty': ['bill', 'andrew', 'chester'],
    'caroline': ['bill', 'chester', 'andrew']
}
Write an algorithm that pairs the men and women together in such a way that no two
people of opposite sex would both rather be with each other than with their current
partners.
"""

from typing import Dict, List, Tuple


def woman_prefers_man1_over_man2(
    gal_preferences: Dict[str, List[str]], woman: str, man1: str, man2: str
) -> bool:
    # check if a given woman prefers man1 more than man2
    for man in gal_preferences[woman]:
        if man == man1:
            return True
        if man == man2:
            return False


def stable_marriage(
    guy_preferences: Dict[str, List[str]], gal_preferences: Dict[str, List[str]]
) -> List[Tuple[str, str]]:
    woman_partners = {woman: None for woman in gal_preferences}
    man_free = {man: True for man in guy_preferences}
    free_count = len(guy_preferences)
    # forming partners
    while free_count > 0:
        # random single man selection
        curr = None
        for man, status in man_free.items():
            if status:
                curr = man
                break
        # pairing up the current man with a woman
        for woman in guy_preferences[curr]:
            if not man_free[curr]:
                break
            # engaged the current man if a single woman is encountered
            if not woman_partners[woman]:
                woman_partners[woman] = curr
                man_free[curr] = False
                free_count -= 1
            # updating woman's partner in case the current man is more favoured by the
            # woman than the man she is engaged with
            else:
                engaged_man = woman_partners[woman]
                if woman_prefers_man1_over_man2(
                    gal_preferences, woman, curr, engaged_man
                ):
                    woman_partners[woman] = curr
                    man_free[engaged_man] = True
                    man_free[curr] = False
    return list(woman_partners.items())


if __name__ == "__main__":
    guy_preferences = {
        "andrew": ["caroline", "abigail", "betty"],
        "bill": ["caroline", "betty", "abigail"],
        "chester": ["betty", "caroline", "abigail"],
    }
    gal_preferences = {
        "abigail": ["andrew", "bill", "chester"],
        "betty": ["bill", "andrew", "chester"],
        "caroline": ["bill", "chester", "andrew"],
    }
    print(stable_marriage(guy_preferences, gal_preferences))


"""
SPECS:

TIME COMPLEXITY: O(n ^ 2)
SPACE COMPLEXITY: O(n)
"""
