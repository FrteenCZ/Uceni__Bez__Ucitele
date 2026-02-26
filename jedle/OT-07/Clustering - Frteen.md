![image.png](../../img/Pasted%20image%2020251113100626.png)
# K means
- rozdělit data do $k$ skupin, aby body ve stejném clusteru byli podobný a v odlišných rozdílný
- hledá centroidy
- bod se zařadí k nejbližšímu centroidu

## postup
1. zvol $k$
2. náhodná inicializace počátečních centroidů
3. vzdálenost všech bodů k centroidům a přiřaď k nejbližšímu
4. přepočítej centroidy, jako průměr všech bodů skupiny
5. opakujeme dokud se něco mění

## vlastnosti
- konvergentní
- může skončit v lokálním minimu 