#15- A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,...
#Faça um programa capaz de gerar a série até o n−ésimo termo.

N = int(input("Digite o n−ésimo termo. : "))

fibonacciSeries = [0,1]

if N>2:
	for i in range(2, N):
		nextElement = fibonacciSeries[i-1] + fibonacciSeries[i-2]
		fibonacciSeries.append(nextElement)

print(fibonacciSeries)
