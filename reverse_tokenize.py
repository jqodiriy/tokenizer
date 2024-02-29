
def build_string_with_substrings(substring_list, target_string):
    def backtrack(start_index, current_path):
        if start_index == len(target_string):
            result.append(list(current_path))
            return

        for substring in substring_list:
            original_substring = substring
            if start_index == 0 and original_substring.startswith("##"):
                continue

            if original_substring.startswith("##"):
                substring = original_substring[2:]

            if target_string.startswith(substring, start_index):
                current_path.append(original_substring)
                backtrack(start_index + len(substring), current_path)
                current_path.pop()

    result = []
    backtrack(0, [])

    return result


def get_substring_combinations(substring_list, target_string):
    ways = build_string_with_substrings(substring_list, target_string)
    matrix = []
    for way in ways:
        matrix.append(way)

    return matrix


if __name__ == "__main__":
    # Example usage:
    substring_list = ["abc", "ab", "##cd", "##def", "ab", "cdef", "##ef", "##abcd"]
    target_string = "abcdef"

    result_matrix = get_substring_combinations(substring_list, target_string)
    print("All ways:")
    for row in result_matrix:
        print(row)
