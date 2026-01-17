# Nearest neighbor
1. Spočítám vzdálenosti ke všem bodům
2. Seřadím je
3. Vyberu $k$ nejbližších
4. Těch kterých je víc $\to$ výsledek
![image.png](../../img/Pasted%20image%2020251106095511.png)

# Lineární separace
$$
\hat{y}=ax+b
$$
![image.png](../../img/Pasted%20image%2020251106092828.png)
## perceptron
- binární rozdělení
- rozhodnutí
	- signum
	- $z>0 \implies +1$
	- $z\leq0\implies-1$
- učení
	1. Náhodně zvolím váhy a bias
	2. Pro daný vstup $x_{i}$ spočítá $\hat{y}=sign(w\cdot x_{i}+b)$
	3. Pokud se spletl ($\hat{y}\neq y_{i}$), upraví podle pravidla:
$$
\begin{align}
w&:=w+\eta\cdot y_{i}\cdot x_{i} \\
b&:=b+\eta\cdot y_{i}
\end{align}
$$
	4. Proces se opakuje, dokud nejsou všechny příklady správně klasifikovány nebo dokud se chyba dále nezmenšuje
- Výsledek
	- Po natrénování perceptron najde takové váhy a bias, které určují rozhodovací hranici:
$$
w_{1}\cdot x_{1}+w_{2}\cdot x_{2}+ \dots +w_{n}\cdot x_{n} + b=0
$$
	- Tato přímka/rovina rozděluje prostor dat
