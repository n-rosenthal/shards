---
doctype: definition
title: Linguagem `arith`
tags:
  - compsci/formal-semantics
  - compsci/formal-languages
  - compsci/programming-languages
reference: Pierce, Benjamin C. Types and Programming Languages.
keywords:
---
# Linguagem `arith`
A linguagem de programação `arith` é a primeira descrita em [[Pierce, Benjamin C. Types and Programming Languages]]. É uma linguagem simples que implementa cálculo não-tipado sobre números e booleanos. É uma linguagem de [[Expressões e Termos em Semântica Formal|termos]] `t` que pode ser definida pela [[Gramática Formal|gramática]] seguinte:

```grammar
t ::=                           termos:
  true                   constante True
  false                  constante False
  if t then t else t         condicional
  0                       constante zero
  succ t                  (fn.) sucessor
  pred t               (fn.) predecessor
  iszero t               teste se é zero
  ```

A primeira linha acima, `t ::=` quer dizer que estamos definindo um *conjunto* de **termos**, e que utilizaremos `t` para *iterar sobre* termos. 

> [!info] Metavariáveis e variáveis
> Dizemos que `t` não é uma variável da **linguagem objeto** da gramática que estamos definindo, isto é, da implementação em si da linguagem; ao contrário, `t` é uma variável da **metalinguagem** que estamos definindo. A metalinguagem é a *notação*, é a *formalização* da linguagem objeto.

Em [[Pierce, Benjamin C. Types and Programming Languages]], a linguagem `arith` não possui parênteses (mas sua implementação, talvez possua). Entretanto, para melhor leitura, os parênteses serão escritos sempre que necessário. Também podemos, a fim de manter a legibilidade, abreviar a composição de `succ(t)`: por exemplo, ao invés de escrevermos `succ(succ(succ(0)))`, escreveremos `3`.

> [!warning] O que são os termos `t` de `arith`?
> Os termos `t` de `arith` *não são* strings ou literais, mas sim [[Árvores de Sintaxe Abstrata|árvores de sintaxe abstrata]].

É importante ressaltar que todas as construções possíveis sobre a definição da gramática de `arith` são possíveis, mesmo que não possuírem uma interpretação clara ou se sua avaliação não possuir um próximo passo. São formas normais de `arith` expressões como `succ true` ou `if 0 then 0 else 0`, apesar de não haver semântica definida para o sucessor de verdadeiro, nem para a interpretação de números enquanto condições *booleanas*.

---
## Outras definições de `arith`
Devemos notar que a definição dos termos por indução e a definição por regras de inferência **caracterizam** o conjunto dos termos $\mathcal{T}$ de `arith`, enquanto a definição concreta permite **construir** os termos de `arith`

> The definitions we have seen characterize the same set of terms from different directions [indução, regras de inferência] simply **characterize** the set as the smallest set satisfying certain *closure properties*; [definição concreta] shows how to actually **construct** the set as the limit of a sequence.
> [[Pierce, Benjamin C. Types and Programming Languages]], pp. 27-28, cap. 3

---
### Definição da linguagem dos termos de `arith` por indução
Seja $\mathcal{T}$ o conjunto dos *termos* de `arith` tal que $\mathcal{T}$ é o **menor** conjunto tal que:
1. $\{\text{true}, \text{false}\} \subseteq \mathcal{T}$
2. $\text{if } t_1 \in \mathcal{T}, \text{then } \{\text{succ } t_1, \text{pred } t_1, \text{iszero } t_1\} \subseteq \mathcal{T}$
3. $\text{if } t_1 \in \mathcal{T}, t_2 \in \mathcal{T}, \text{ and } t_3 \in \mathcal{T} \text{ then if } t_1 \text{ then } t_2 \text{ else } t_3$

> [!info] O *menor* conjunto que define uma propriedade
> Quando dizemos que um conjunto é o menor conjunto que define uma propriedade, estamos buscando afirmar que:
> 1. o conjunto não possui, em primeira análise, nenhuma outra propriedade além daquelas que demonstramos; e
> 2. não existe outro conjunto tão pequeno quanto este e que tenha todas as propriedades que este tem, simultaneamente.
> portanto, este é o menor conjunto para o qual tais propriedades são verdadeiras; se pudesse existir outro conjunto *menor* que este, então este conjunto seria o menor.

---
### Definição da linguagem dos termos de `arith` por regras de inferência (esquemas de regras)
Podemos definir `arith` por regras de inferência (esquemas de regras, ou *rule schemas* propriamente, uma vez que suas premissas ou conclusões podem conter metavariáveis) sobre (sua linguagem de) seus termos `t`:

$$
\newcommand{\inference}[2]{\dfrac{ #1 }{ #2 }}
\newcommand{\kw}[1]{\text{ #1}} % Upright text in math mode

\text{true} \in \mathcal{T} \quad \text{false} \in \mathcal{T} \quad 0 \in \mathcal{T}
$$
$$
\newcommand{\inference}[2]{\dfrac{ #1 }{ #2 }}
\newcommand{\kw}[1]{\text{ #1}} % Upright text in math mode

\inference{t_1 \in \mathcal{T}}{\kw{succ } t_1 \in \mathcal{T}} \quad
\inference{t_1 \in \mathcal{T}}{\kw{pred } t_1 \in \mathcal{T}} \quad
\inference{t_1 \in \mathcal{T}}{\kw{iszero } t_1 \in \mathcal{T}}
$$
$$
\newcommand{\inference}[2]{\dfrac{ #1 }{ #2 }}
\newcommand{\kw}[1]{\text{ #1}} % Upright text in math mode

\inference
{{t_1 \in \mathcal{T}} \quad {t_2 \in \mathcal{T}} \quad {t_3 \in \mathcal{T}}}
{\kw{if } t_1 \kw{ then } t_2 \kw{ else } t_3 \in \mathcal{T}}
$$

As três primeiras regras são *axiomas*, pois são regras sem premissas. Tomamos estas regras por verdadeiras. Note que estas regras definem os **valores** de `arith`.

Como notado acima, na maioria das regras, existem metavariáveis `t` ou nas premissas, ou na conclusão. Portanto, não se trata de regras de inferência, mas esquemas de regras (*rule schemas*). Para cada esquema, existem infinitas possibilidades de *regras concretas*, obtidas através da substituição da metavariável por algum objeto da categoria adequada (isto é, substituir `t` por qualquer um dos termos que compõem, recursivamente, `t`).

---
### Definição concreta da linguagem `arith`
Para cada número natural $i$, defina um conjunto $S_i$ tal que

$S_0 \quad = \quad \emptyset$
$S_1 \quad = \quad \quad \{\text{true}, \text{false}, 0\}$
$\quad \quad \quad \quad \cup \quad \{\text{succ } t_1, \text{pred } t_1, \text{iszero } t_1, \quad | \quad t_1 \in S_1\}$
$\quad \quad \quad \quad \cup \quad \{\text{if } t_1 \text{ then } t_2 \text{ else } t_3 \quad | \quad t_1, t_2, t_3 \in S_1\}$
$S \quad = \quad \bigcup_{i} S_i$

> $S_0$ is empty; $S_1$ contains just the constants; $S_2$ contains the constants plus the phrases that can be built with constants and just one `succ`, `pred`, `iszero`, or `if`; $S_3$ contains these and all phrases that can be built using `succ`, `pred`, `iszero`, or `if` on phrases in S2; and so on. $S$ collects together all the phrases that can be built in this way—i.e., all phrases built by some finite number of arithmetic and conditional operators, beginning with just constants.
> [[Pierce, Benjamin C. Types and Programming Languages]] p.  27, cap. 3

- [[Quantos elementos S_3 tem?]]
- [[Comutatividade dos conjuntos S_i]]
---

## Indução sobre os termos de `arith`
A caracterização explícita dos termos `t` $\in \mathcal{T}$ de `arith` permite que possamos
1. estabelecer *definições indutivas* sobre os termos, ou de funções sobre termos, e
2. escrever *provas indutivas* de propriedades sobre os termos.

Algumas funções simples sobre os termos de `arith` são `Consts(t)`, que recupera o conjunto de constantes que aparecem em `t`; `size(t)`, que é o número de nós na [[Árvores de Sintaxe Abstrata]] `t`; e `depth(t)`.

> [!warning] Problema
> Por que `depth(t)` é o menor $i$ tal que $t \in S_i$, conforme a definição construtiva da linguagem de termos de `arith`.

### Funções sobre termos da linguagem `arith`
#### `Consts(t)`
$\text{def. }$ `Consts(t)`: o *conjunto de constantes* que aparecem em `t`, escrito `Consts(t)`, é definido por:

```
                        constantes (valores)
Consts(true)                       = {true}
Consts(false)                      = {false}
Consts(0)                          = {0}
                        
                        expressões
Consts(succ t)                     = Consts(t)
Consts(pred t)                     = Consts(t)
Consts(iszero t)                   = Consts(t)
Consts(if t_1 then t_2 else t_3)   = Consts(t_1) || Consts(t_2) || Consts(t_3)
```

---
#### `size(t)`
$\text{def. }$ `size(t)`: o *tamanho* de um termo `t`, escrito `size(t)`, é definido como a quantidade de nós na sua [[Árvores de Sintaxe Abstrata]].

```
                        constantes (valores)
size(true)                       = 1
size(false)                      = 1
size(0)                          = 1
                        
                        expressões
size(succ t)                     = size(t) + 1
size(pred t)                     = size(t) + 1
size(iszero t)                   = size(t) + 1
size(if t_1 then t_2 else t_3)   = size(t_1) + size(t_2) + size(t_3) + 1
```

---
#### `depth(t)`
$\text{def. }$ `depth(t)`: a *profundidade* de um termo `t`, escrito depth(t)`, é definido como sua profundidade máxima de sua [[Árvores de Sintaxe Abstrata]].

```
                        constantes (valores)
depth(true)                       = 1
depth(false)                      = 1
depth(0)                          = 1
                        
                        expressões
depth(succ t)                     = depth(t) + 1
depth(pred t)                     = depth(t) + 1
depth(iszero t)                   = depth(t) + 1
depth(if t_1 then t_2 else t_3)   = max(depth(t_1), depth(t_2), depth(t_3)) + 1
```

##### Profundidade de um termo e os conjuntos $S_i$
Nota-se que

$$\text{depth}(t) = i$$
tal que $i$ é o menor inteiro tal que
$$\text{t} \in S_i$$

---
### Provas por indução sobre os termos de `arith`
Podemos utilizar *indução sobre os termos* de uma linguagem formal como `arith` para provar propriedades sobre esta linguagem.

#### O número de constantes distintas em um termo é, no máximo, o seu tamanho
$\text{Lema: }$ o número de constantes distintas (`Consts(t)`) em um termo `t` é, no máximo, seu tamanho `size(t)`. Isto é,

$$|\text{Consts(t)}| \leq \text{size(t)}$$
$\text{Prova: }$ (por indução sobre a profundidade de `t`). **Assuma** a propriedade para todos os termos **menores que** `t`, então prove para `t` em si. Considere os **três casos**:

$\text{Caso I: }$ `t` é uma constante (valor).
A prova é imediata: `|Consts(t)| = |{t}| = 1 = size(t)`

$\text{Caso II: }$ `t = succ t_1` ou `t = pred t_1` ou `t = iszero t_1`
Pela **hipótese de indução**, temos que $|\text{Consts(t)}| \leq \text{size(t)}$. A partir disso, e lançando mão da **definição de** `depth(t)`, fazemos:

$$|\text{Consts(t)}| \leq \text{size(t)}$$
$$|\text{Consts(t)}| = |\text{Consts}(t_1)| \leq \text{size(t)} < \text{size}(t_1)$$
$$\quad \quad \quad \quad \quad \quad \quad \quad \implies |\text{Consts(t)}| \leq \text{size(t)}$$

Case: t = if t1 then t2 else t3
By the induction hypothesis, |Consts(t1)| ≤ size(t1), |Consts(t2)| ≤ size(t2),
and |Consts(t3)| ≤ size(t3). We now calculate as follows:
|Consts(t)| = |Consts(t1) ∪ Consts(t2) ∪ Consts(t3)|
≤ |Consts(t1)| + |Consts(t2)| + |Consts(t3)|
≤ size(t1) + size(t2) + size(t3)
< size(t). 

---
#### Princípios para Indução sobre Termos de uma Linguagem
$\text{Th. }$ \[Princípios de Indução sobre Termos\]: seja $P$ um **predicado** sobre termos de uma linguagem formal, então:

#### Indução sobre profundidade (*induction on depth*)

---
#### Indução sobre tamanho (*induction on size*)

---
#### Indução estrutural (*structural induction*)

---