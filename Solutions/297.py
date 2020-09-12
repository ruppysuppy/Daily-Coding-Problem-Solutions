"""
Problem:

At a popular bar, each customer has a set of favorite drinks, and will happily accept
any drink among this set. For example, in the following situation, customer 0 will be
satisfied with drinks 0, 1, 3, or 6.

preferences = {
    0: [0, 1, 3, 6],
    1: [1, 4, 7],
    2: [2, 4, 7, 5],
    3: [3, 2, 5],
    4: [5, 8]
}
A lazy bartender working at this bar is trying to reduce his effort by limiting the
drink recipes he must memorize. Given a dictionary input such as the one above, return
the fewest number of drinks he must learn in order to satisfy all customers.

For the input above, the answer would be 2, as drinks 1 and 5 will satisfy everyone.
"""

from typing import Dict, List, Set


def check_all_customers_satisfied(
    customers: Set[int], combination: List[int], drinks: Dict[int, Set[int]]
) -> bool:
    # check if the current combination can satisfy all customers
    temp = None
    for drink in combination:
        if temp is None:
            temp = drinks[drink]
        else:
            temp = temp.union(drinks[drink])
    return temp is not None and temp == customers


def get_min_drinks_helper(
    drinks_left: List[int],
    curr_combination: List[int],
    drinks: Dict[int, Set[int]],
    customers: Set[int],
    combination_list: List[List[int]],
) -> None:
    # generating all possible combinations of drinks
    if not drinks_left:
        if check_all_customers_satisfied(customers, curr_combination, drinks):
            combination_list.append(curr_combination)
        return
    curr_drink = drinks_left.pop()
    get_min_drinks_helper(
        drinks_left[:],
        curr_combination + [curr_drink],
        drinks,
        customers,
        combination_list,
    )
    get_min_drinks_helper(
        drinks_left[:], curr_combination, drinks, customers, combination_list
    )


def get_min_drinks(preferences: Dict[int, List[int]]) -> int:
    # transforming preferences from customer -> drink to drink -> customer map
    drinks_transformed = {}
    for customer in preferences:
        for drink in preferences[customer]:
            if drink not in drinks_transformed:
                drinks_transformed[drink] = set()
            drinks_transformed[drink].add(customer)
    combinations = []
    # generating all combinations
    get_min_drinks_helper(
        list(drinks_transformed.keys()),
        [],
        drinks_transformed,
        set(preferences.keys()),
        combinations,
    )
    # returning the combination with minimum drinks
    # NOTE: "min()" can be wrapped with "len()" to get the number of drinks
    return min(combinations, key=lambda x: len(x))


if __name__ == "__main__":
    preferences = {
        0: [0, 1, 3, 6],
        1: [1, 4, 7],
        2: [2, 4, 7, 5],
        3: [3, 2, 5],
        4: [5, 8],
    }
    print(get_min_drinks(preferences))


"""
SPECS:

TIME COMPLEXITY: O(2 ^ drinks + customers x drinks)
SPACE COMPLEXITY: O(customers x drinks)
"""
