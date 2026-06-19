# Program Simulasi Rute Operan Optimal (Revisi NBA Data)
# Oleh: Muhammad Adnan Kurniawan

def dfs_optimal_path(graph, current, target, path, current_prob, best_path):
    # Base case: jika bola sudah sampai di target (Center)
    if current == target:
        if current_prob > best_path['prob']:
            best_path['prob'] = current_prob
            best_path['route'] = list(path)
        return

    # Batas kedalaman (Maksimal 4 operan untuk meniru shot clock 24 detik)
    if len(path) > 4:
        return

    # Rekursi penelusuran ke node tetangga
    for neighbor, weight in graph.get(current, {}).items():
        if neighbor not in path: # Mencegah operan bolak-balik (cyclic)
            path.append(neighbor)
            dfs_optimal_path(graph, neighbor, target, path, 
                             current_prob * weight, best_path)
            path.pop() # Backtrack untuk mencoba cabang lain

def main():
    # Inisialisasi Graf (Berdasarkan estimasi data tracking NBA)
    basketball_network = {
        'PG': {'SG': 0.75, 'SF': 0.70, 'PF': 0.60, 'C': 0.50},
        'SG': {'SF': 0.70, 'PF': 0.60, 'C': 0.65},
        'SF': {'PF': 0.65, 'C': 0.65},
        'PF': {'C': 0.45},
        'C': {} # Target Node
    }

    best = {'route': [], 'prob': 0.0}
    print("----------------------------------------")
    print("Evaluating all possible passing permutations...")
    
    # Eksekusi DFS dari Point Guard (PG) ke Center (C)
    dfs_optimal_path(basketball_network, 'PG', 'C', ['PG'], 1.0, best)

    # Mencetak Hasil
    print(f"Optimal Passing Route: {' -> '.join(best['route'])}")
    print(f"Maximum Success Probability: {best['prob']:.3f} ({best['prob']*100:.1f}%)")
    print("----------------------------------------")

if __name__ == "__main__":
    main()