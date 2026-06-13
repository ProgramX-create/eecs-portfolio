# matrix_calc.py - Freshman Year (Summer 2023)
# Pure Python matrix addition utility to master array dimensions

def add_matrices(matrix_a, matrix_b):
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        return "[ERROR] Matrix dimensions must match exactly for addition operations."
    
    # Nested loops map matrix coordinates dynamically
    result = [[matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))] for i in range(len(matrix_a))]
    return result

if __name__ == "__main__":
    print("[SYSTEM] Initializing 2023 CLI Matrix Framework...")
    m1 = [[1, 2], [3, 4]]
    m2 = [[5, 6], [7, 8]]
    print(f"Matrix A: {m1}\nMatrix B: {m2}")
    print(f"Computed Coordinate Sum Vector: {add_matrices(m1, m2)}")

