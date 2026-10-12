
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O']
}

leaves = {'H': 3, 'I': 12, 'J': 8, 'K': 2, 'L': 4, 'M': 6, 'N': 14, 'O': 5}


minimax_nodes = 0

def minimax(node, is_max):
    global minimax_nodes
    minimax_nodes += 1


    if node in leaves:
        return leaves[node]

    if is_max:
        best = -999
        for child in tree[node]:
            val = minimax(child, False)
            if val > best:
                best = val
        return best
    else:
        best = 999
        for child in tree[node]:
            val = minimax(child, True)
            if val < best:
                best = val
        return best


ab_nodes = 0

def alphabeta(node, alpha, beta, is_max):
    global ab_nodes
    ab_nodes += 1

    if node in leaves:
        return leaves[node]

    if is_max:
        best = -999
        for child in tree[node]:
            val = alphabeta(child, alpha, beta, False)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = 999
        for child in tree[node]:
            val = alphabeta(child, alpha, beta, True)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

minimax_nodes = 0
res_mm = minimax('A', True)

ab_nodes = 0
res_ab = alphabeta('A', -999, 999, True)

print("--- Солдан оңға қарай ---")
print("Minimax тапқан мән:", res_mm, "| Тексерген түйіндері:", minimax_nodes)
print("Alpha-Beta тапқан мән:", res_ab, "| Тексерген түйіндері:", ab_nodes)
print("Қысқартылған түйіндер саны:", 15 - ab_nodes)
