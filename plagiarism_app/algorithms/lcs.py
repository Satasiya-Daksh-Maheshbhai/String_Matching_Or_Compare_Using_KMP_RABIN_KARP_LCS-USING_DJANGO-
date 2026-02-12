def lcs_string(X, Y):
    n = len(X)
    m = len(Y)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    arrows_left = [[""] * (m + 1) for _ in range(n + 1)]
    arrows_up = [[""] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                arrows_left[i][j] = "↖"
                arrows_up[i][j] = "↖"
            else:
                left = dp[i][j - 1]
                up = dp[i - 1][j]

                if left > up:
                    dp[i][j] = left
                    arrows_left[i][j] = "←"
                    arrows_up[i][j] = "←"
                elif up > left:
                    dp[i][j] = up
                    arrows_left[i][j] = "↑"
                    arrows_up[i][j] = "↑"
                else:  # tie
                    dp[i][j] = left
                    arrows_left[i][j] = "←"   # LEFT priority
                    arrows_up[i][j] = "↑"     # UP priority

    
    i, j = n, m
    lcs_left = []
    while i > 0 and j > 0:
        if arrows_left[i][j] == "↖":
            lcs_left.append(X[i - 1])
            i -= 1
            j -= 1
        elif arrows_left[i][j] == "←":
            j -= 1
        else:
            i -= 1
    lcs_left.reverse()

    
    i, j = n, m
    lcs_up = []
    while i > 0 and j > 0:
        if arrows_up[i][j] == "↖":
            lcs_up.append(X[i - 1])
            i -= 1
            j -= 1
        elif arrows_up[i][j] == "↑":
            i -= 1
        else:
            j -= 1
    lcs_up.reverse()

    return {
        "dp": dp,
        "arrows_left": arrows_left,
        "arrows_up": arrows_up,
        "lcs_left": "".join(lcs_left),
        "lcs_up": "".join(lcs_up),
        "length": dp[n][m]
    }
