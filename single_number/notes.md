# [XOR Commutativity and Associativity](https://math.stackexchange.com/questions/293793/prove-xor-is-commutative-and-associative)
## Associativity
$\begin{align*}
\left( a \oplus b \right) \oplus c &= \left( a \oplus b \right) \cdot \overline{c} + \overline{\left( a \oplus b \right) } \cdot c
\\
&= \left( a \cdot \overline{b} + b \cdot \overline{a} \right) \cdot \overline{c} + \overline{\left( a \cdot \overline{b} + b \cdot \overline{a} \right) } \cdot c
\\
&= \left( a \cdot \overline{b} + b \cdot \overline{a} \right) \cdot \overline{c} + \left( \left(\overline{a} + b\right) \cdot \left( \overline{b} + a\right) \right) \cdot c
\\
&= \left( a \cdot \overline{b} + b \cdot \overline{a} \right) \cdot \overline{c} + \left( \left( \overline{a} + b \right) \cdot \overline{b} + \left( \overline{a} + b \right) \cdot a \right) \cdot c
\\
&= \left( a \cdot \overline{b} + b \cdot \overline{a} \right) \cdot \overline{c} + \left( \overline{a} \cdot \overline{b} + b \cdot a \right) \cdot c
\end{align*}$

$\begin{align*}
a \oplus \left( b \oplus c \right) &= a \cdot \overline{\left(b \oplus c\right)} + \overline{a} \cdot \left( b \oplus c \right) 
\\
&= a \cdot \left( \overline{b} \cdot \overline{c} + b \cdot c \right) + \overline{a} \cdot \left( b \cdot \overline{c} + \overline{b} + c \right) 
\end{align*}$

$\therefore \left( a \oplus b \right) \oplus c = a \oplus \left( b \oplus c \right)$
