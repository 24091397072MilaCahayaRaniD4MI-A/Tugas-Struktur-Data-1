def function(n):
    # Bagian O(n)
    for i in range(n):
        print(i)

    # Bagian O(n^2)
    for i in range(n):
        for j in range(n):
            print(i, j)

n = int(input("Masukkan nilai n = "))    
function(n)
