# Semântica Formal de Pares Ordenados
1. Os pares ordenados são a primeira estrutura de dados não-atômica (`int`, `bool` etc) que surge nas [[Linguagem S1|linguagens S_i]];
2. **Operador vírgula** ( $\text{,}$ ): construtor de pares: $e_1, e_2$ ou $(e_1, e_2)$.
3. Expansão na *linguagem de termos* para aceitar o **construtor** de pares $(e_1, e_2)$ e os **destruidores** do primeiro e do segundo elementos, `fst e` e `snd e`.
	1. Outras sintaxes possíveis para os destruidores: `#1(e_1, e_2)` e `(e_1, e_2).snd`

## Sintaxe de Termos e Valores
```ocaml
valores ::= ... | (v_1, v_2)

termos  ::= ... | (e_1, e_2)    (* construtor de pares  *)
				| fst e         (* destruidor 1o. elem. *)
				| snd e         (* destruidor 2o. elem. *)

```
---
## Sistema de Tipos
### Sintaxe de Tipos
```ocaml
t       ::= nat | bool | t * t	
```

Notar que
1. os construtores `nat` e `bool` são construtores de tipo de aridade 0, enquanto o construtor de tipo para pares ordenados é de aridade 2.
2. **operador ponto** ( $\cdot$ ) para produzir **produtos de tipos**:
	1. $(\text{nat} \cdot \text{nat})$ , $(\text{nat} \cdot \text{(nat} \cdot \text{bool))}$
	2. $\cdot : (\text{t} \times \text{t}) \to \text{t}$
	
---
### Esquemas de Regras de Inferência de Tipos
$$
\newcommand{\inference}[3][]{\dfrac{ #2 }{ #3 } \mathrel{\scriptstyle #1}} % Rule name as optional argument
\newcommand{\kw}[1]{\text{ #1}} % Upright text in math mode

\inference[\kw{[TPar]}]{\vdash e_1 : \kw{T} \quad \vdash e_2 : \kw{T'}}{(e_1, e_2) : \kw{T} \cdot \kw{T'}}
\quad
\inference[\kw{[TParFst]}]{\vdash e : \kw{T} \cdot \kw{T'}}{\kw{fst e} : \kw{T}}
\quad
\inference[\kw{[TParSnd]}]{\vdash e : \kw{T} \cdot \kw{T'}}{\kw{snd e} : \kw{T'}}
$$
- São somente três regras para a expansão da inferência de tipos;
- $\kw{[TPar]}$: dado que o primeiro elemento é tipado em $\kw{T}$, e que o segundo elemento é tipado em $\kw{T'}$ , então o par formado por estes elementos será tipado em $\kw{T} \cdot \kw{T'}$;
- $\kw[TPairFst]$: dado um par tipado em $\kw{T} \cdot \kw{T'}$, $\kw{fst e}$ será tipado em $\kw{T}$.
- $\kw[TPairSnd]$: dado um par tipado em $\kw{T} \cdot \kw{T'}$, $\kw{snd e}$ será tipado em $\kw{T'}$.

---
### Implementação do Inferidor de Tipos para Pares
Dado uma linguagem de termos $\kw{L}$ sobre uma sintaxe de `termo`s e `tipo`s, temos

```ocaml
(* dado um termo `e`, tenta inferir seu tipo `t` *)
let rec typeinfer (e: termo) : tipo option = (match e with
	...
	| Pair (e1, e2) 
) 
``` 

---
---

## Implementação
### Implementação dos Destruidores
Há uma observação a ser feita em favor de uma sintaxe `fst e` e `snd e`, e contrária à  `fst (e_1, e_2)` ou `snd (e_1, e_2)`:
- favorece-se a sintaxe mais abrangente, por razões de [[Ortogonalidade em Linguagens Formais|ortogonalidade]] e de manter a linguagem menos restritiva;
- $\text{e.g. }$ não seria aceitável, usando `(e_1, e_2)`, a expressão abaixo:

```ocaml
(fst
	(if (iszero 0)
		then (0, true)
		else (0, false)
	)
)
```

