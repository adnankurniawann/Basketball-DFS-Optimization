# Program Simulasi Rute Operan Optimal - Skenario 2 (Elite Interior Defense)
# Oleh: Muhammad Adnan Kurniawan

def dfs_optimal_path(graph, current, target, path, current_prob, best_path):
    # Base case: jika bola sudah sampai di target (Shooting Guard)
    if current == target:
        if current_prob > best_path['prob']:
            best_path['prob'] = current_prob
            best_path['route'] = list(path)
        return

    # Batas kedalaman (Maksimal 4 operan untuk meniru shot clock)
    if len(path) > 4:
        return

    # Rekursi penelusuran ke node tetangga
    for neighbor, weight in graph.get(current, {}).items():
        if neighbor not in path: 
            path.append(neighbor)
            dfs_optimal_path(graph, neighbor, target, path, 
                             current_prob * weight, best_path)
            path.pop() # Backtrack

def main():
    # Inisialisasi Graf (Skenario 2: Pertahanan ketat di area Center)
    # Probabilitas operan ke 'C' diturunkan, probabilitas ke 'SG' dinaikkan.
    basketball_network = {
        'PG': {'SG': 0.85, 'SF': 0.70, 'PF': 0.60, 'C': 0.20},
        'SG': {'SF': 0.70, 'PF': 0.60, 'C': 0.65},
        'SF': {'SG': 0.80, 'PF': 0.65, 'C': 0.65},
        'PF': {'C': 0.25},
        'C': {} 
    }

    best = {'route': [], 'prob': 0.0}
    
    print("----------------------------------------")
    print("Evaluating Scenario 2: Elite Interior Defense...")
    print("Target Node Changed to: SG (3-Point Attempt)")
    
    # Eksekusi DFS dari Point Guard (PG) ke target baru, Shooting Guard (SG)
    dfs_optimal_path(basketball_network, 'PG', 'SG', ['PG'], 1.0, best)

    print(f"Optimal Passing Route: {' -> '.join(best['route'])}")
    print(f"Maximum Success Probability: {best['prob']:.3f} ({best['prob']*100:.1f}%)")
    
    # Hitungan rute alternatif untuk pembuktian analisis
    print("\nAlternative Evaluated Route: PG -> SF -> SG")
    alt_prob = basketball_network['PG']['SF'] * basketball_network['SF']['SG']
    print(f"Probability: {basketball_network['PG']['SF']:.2f} * {basketball_network['SF']['SG']:.2f} = {alt_prob:.3f} ({alt_prob*100:.1f}%)")
    print("----------------------------------------")

if __name__ == "__main__":
    main()