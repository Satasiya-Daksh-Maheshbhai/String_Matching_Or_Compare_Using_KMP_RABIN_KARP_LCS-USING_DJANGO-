from django.shortcuts import render
import time

from .algorithms.kmp import kmp_search
from .algorithms.rabin_karp import rabin_karp
from .algorithms.lcs import lcs_string


def index(request):
    context = {}

    if request.method == "POST":
        text = request.POST.get("text1", "")
        pattern = request.POST.get("text2", "")
        algorithm = request.POST.get("algorithm", "")

        context["text"] = text
        context["pattern"] = pattern
        context["algorithm"] = algorithm.upper()

        start_time = time.time()

        
        if algorithm == "kmp":
            lps_table, comparisons, matches = kmp_search(text, pattern)

            context["lps_table"] = lps_table
            context["comparisons"] = comparisons
            context["matches"] = matches
            context["complexity"] = "O(n + m)"
            

        
        elif algorithm == "rabin":
            hash_mode = request.POST.get("hash_mode")
            modulo = request.POST.get("modulo")
            char_values = request.POST.get("char_values")

            char_map = {}
            if char_values:
                for pair in char_values.split(","):
                    k, v = pair.split("=")
                    
                    char_map[k.strip().upper()] = int(v.strip())

            result = rabin_karp(
                text,
                pattern,
                q=int(modulo) if modulo else None,
                hash_mode=hash_mode,
                char_map=char_map
            )

            context.update({
                "algorithm": "RABIN",
                "rk_steps": result["rk_steps"],
                "pattern_hash": result["pattern_hash"],
                "valid_hits": result["valid_hits"],
                "spurious_hits": result["spurious_hits"],
                "time": result["time"],
                "complexity": "O(n + m)"
            })

        elif algorithm == "lcs":
            result = lcs_string(text, pattern)

            
            left_table = []
            up_table = []

            dp = result["dp"]
            arrows_left = result["arrows_left"]
            arrows_up = result["arrows_up"]

            for i in range(len(dp)):
                row_left = []
                row_up = []
                for j in range(len(dp[0])):
                    row_left.append({
                        "value": dp[i][j],
                        "arrow": arrows_left[i][j]
                    })
                    row_up.append({
                        "value": dp[i][j],
                        "arrow": arrows_up[i][j]
                    })
                left_table.append(row_left)
                up_table.append(row_up)

            context["left_table"] = left_table
            context["up_table"] = up_table
            context["lcs_left"] = result["lcs_left"]
            context["lcs_up"] = result["lcs_up"]
            context["lcs_length"] = result["length"]

            
            lcs_len = result["length"]
            similarity = round((2 * lcs_len) / (len(text) + len(pattern)) * 100, 2) if (len(text) + len(pattern)) > 0 else 0
            context["similarity"] = f"{similarity}%"

            context["complexity"] = "O(n × m)"


    return render(request, "index.html", context)
