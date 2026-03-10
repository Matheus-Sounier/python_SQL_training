print("I've imported my module")

def find_index(to_search: str, target: str) -> str:
    for i, index in enumerate(to_search):
        if index == target:
            return 1
    return -1

