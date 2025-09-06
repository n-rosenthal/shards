```latex
\newcommand{\inference}[2]{\dfrac{ #1 }{ #2 }}
\newcommand{\kw}[1]{\text{ #1}} % Upright text in math mode

\inference{t_1 \in T}{\kw{succ } t_1 \in T}
```

Com o nome da regra ao lado:

```latex
\newcommand{\inference}[3][]{\dfrac{ #2 }{ #3 } \mathrel{\scriptstyle #1}} % Rule name as optional argument
\newcommand{\kw}[1]{\text{ #1}} % Upright text in math mode

\inference[Succ]{t_1 \in T}{\kw{succ } t_1 \in T} % Example usage with rule name
```