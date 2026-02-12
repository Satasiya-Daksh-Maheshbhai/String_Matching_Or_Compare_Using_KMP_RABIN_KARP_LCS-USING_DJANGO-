import time

def rabin_karp(text, pattern, q=None, hash_mode="mod", char_map=None):

    start = time.time()

    n = len(text)
    m = len(pattern)

    steps = []
    valid_hits = []
    spurious_hits = 0

    def compute_hash(s):
    
        if hash_mode == "mod":
            return int(s) % q, f"mod {q}"

        
        value = 0
        formula = []

        for ch in s:
            
            uc = ch.upper()
            if uc not in char_map:
                raise ValueError(f"Character '{ch}' not found in your mapping. Please include it in char_values input.")
            v = char_map[uc]
            value += v
            formula.append(str(v))

        return value, " + ".join(formula)


    
    pattern_hash, pattern_formula = compute_hash(pattern)

    
    for i in range(n - m + 1):
        window = text[i:i+m]
        window_hash, window_formula = compute_hash(window)

        if window_hash == pattern_hash:
            if window == pattern:
                result = "Valid Hit"
                valid_hits.append(i)
            else:
                result = "Spurious Hit"
                spurious_hits += 1
        else:
            result = "No Match"

        steps.append({
            "index": i,
            "window": window,
            "hash_calc": window_formula,
            "window_hash": window_hash,
            "result": result
        })

    end = time.time()

    return {
        "rk_steps": steps,
        "pattern_hash": pattern_hash,
        "valid_hits": valid_hits,
        "spurious_hits": spurious_hits,
        "time": round(end - start, 6)
    }
