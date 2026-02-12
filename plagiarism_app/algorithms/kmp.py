def build_lps_verbose(pattern):
    table = []

    for i in range(1, len(pattern) + 1):
        sub = pattern[:i]

        prefixes = []
        suffixes = []

        for j in range(1, len(sub)):
            prefixes.append(sub[:j])
            suffixes.append(sub[j:])

        max_len = 0
        for p in prefixes:
            if p in suffixes:
                max_len = max(max_len, len(p))

        table.append({
            "pattern": sub,
            "prefix": ", ".join(prefixes) if prefixes else "Nil",
            "suffix": ", ".join(suffixes) if suffixes else "Nil",
            "lps": max_len
        })

    lps = [row["lps"] for row in table]
    return lps, table


def kmp_search_verbose(text, pattern):
    lps, lps_table = build_lps_verbose(pattern)

    i = j = 0
    steps = []
    matches = []
    step_no = 1

    while i < len(text):
        step = {
            "step": step_no,
            "t_index": i + 1,
            "t_char": text[i],
            "p_index": j + 1 if j < len(pattern) else "-",
            "p_char": pattern[j] if j < len(pattern) else "-",
            "action": "",
            "jump": ""
        }

        if text[i] == pattern[j]:
            step["action"] = "Match → move forward"
            i += 1
            j += 1
        else:
            step["action"] = "Mismatch"
            if j != 0:
                old_j = j + 1
                j = lps[j - 1]
                step["jump"] = f"Pattern jumps from P[{old_j}] → P[{j + 1}] using LPS"
            else:
                step["jump"] = "Pattern at start → move text forward"
                i += 1

        if j == len(pattern):
            matches.append(i - j + 1)
            step["action"] = "FULL MATCH FOUND"
            step["jump"] = f"Pattern found at T[{i - j + 1}], jump to P[{lps[j - 1] + 1}]"
            j = lps[j - 1]

        steps.append(step)
        step_no += 1

    return lps_table, steps, matches



def kmp_search(text, pattern):
    return kmp_search_verbose(text, pattern)
