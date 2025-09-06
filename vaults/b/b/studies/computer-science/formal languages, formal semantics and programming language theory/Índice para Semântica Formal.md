
### $\S 0$ Templates, genéricos
#### [[Typeset LaTeX para definir regras de inferência]]

$$
\newcommand{\inference}[2]{\dfrac{ #1 }{ #2 }}
\newcommand{\kw}[1]{\text{ #1}} % Upright text in math mode

\inference{t_1 \in T}{\kw{succ } t_1 \in T}
$$

### $\S 1$ Conceitos
- [[Gramática Formal]] (gramáticas formais, forma padrão BNF, sintaxe abstrata), [[Variáveis e Metavariáveis|variáveis e metavariáveis]], [[Definição Indutiva|definição indutiva]]
- [[Expressões e Termos em Semântica Formal|Termos e Expressões]] (formas simples, valores)
- [[Sistemas Tipados e Não-Tipados]] (tipos, )

### $\S 1$ Linguagens
- Linguagens $S_i$: [[Linguagem S1|Linguagem S1 ou L0]].
	- Expansões de $L_0$:
	- [[Semântica Formal de Pares Ordenados|S2: pares ordenados]]
	- [[Semântica Formal de Let (e1, e2)|S3: Let e1 in e2]]
	- [[Semântica Formal para Funções e Aplicações|S4 e S5: funções e aplicações]]
	- [[Semântica Formal para Ponto Fixo|S6: pontos fixos]]
	- [[Semântica Form para Funções Recursivas|S7: funções recursivas]]
- [[Linguagem L1]]: $L_0$ expandida sobre construções imperativas



### $\S 2$ Sistemas Tipados e Não-Tipados