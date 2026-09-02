def promedio(nums):
    return sum(nums) / len(nums)
def desviacion(nums):
    prom = promedio(nums)
    suma = 0
    for x in nums:
        suma += (x - prom) ** 2
    return (suma / (len(nums) - 1)) ** 0.5
entrada = input("Ingrese 10 números: ").split()
nums = list(map(float, entrada))
print(f"El promedio es {promedio(nums):.2f}")
print(f"La desviación estandar es {desviacion(nums):.5f}")