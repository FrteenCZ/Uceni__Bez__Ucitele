# MINIMALIZACE POMOCÍ KARNAUGHOVY MAPY- PRAVIDLA
1) Sousední políčka se stejnými hodnotami zahrnujeme do SMYČEK.
2) Smyčky mohou mít velikost mocnin čísla 2 tj. 2$^n$ (počet jedniček ve smyčce může být: 1, 2, 4, 8 atd., NE LICHÝ počet 3, 5 atd.).
3) Smyčky se snažíme dělat co největší a mohou se překrývat.
4) Sousední políčka jsou políčka, která se liší v jediné proměnné. Krajní políčka mapy považujeme za sousední.
5) Disjunktní tvar: píšeme pro logické jedničky jako součet součinů. Pod čarou jsou hodnoty např. A, B, x1, x2 apod., mimo čáru jsou proměnné $\overline A$, $\overline B$, $\overline x_{1}$, $\overline x_{2}$ atd.
6) Konjunktní tvar: píšeme pro logické nuly jako součin součtů. Pod čarou jsou proměnné např. $\overline A$, $\overline B$, $\overline x_{1}$, $\overline x_{2}$ apod., mimo čáru jsou proměnné A, B, x1, x2 atd.
![image.png](../../img/Pasted%20image%2020250604112012.png)
$$
\begin{gathered}
f(A,B,C,D) &&=&& B\cdot\overline{C} \cdot \overline{D}  && + && A\cdot \overline{B} && + && C \cdot A  \\
&&&& \mathrm{žlutá} &&&& \mathrm{fialová} &&&& \mathrm{modrá}
\end{gathered}
$$
