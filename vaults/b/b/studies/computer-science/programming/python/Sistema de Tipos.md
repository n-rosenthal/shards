## Boas Práticas para Tipagem
### Anotações de parâmetros em funções devem ser tão abrangentes quanto a implementação permitir
> In general, a function input parameter should be annotated with the widest possible type supported by the implementation. For example, if the implementation requires the caller to provide an iterable collection of strings, the parameter should be annotated as `Iterable[str]`, not as `List[str]`. The latter type is narrower than necessary, so if a user attempts to pass a tuple of strings (which is supported by the implementation), a type checker will complain about a type incompatibility.
> As a specific application of the “use the widest type possible” rule, libraries should generally use immutable forms of container types instead of mutable forms (unless the function needs to modify the container). Use `Sequence` rather than `List`, `Mapping` rather than `Dict`, etc. Immutable containers allow for more flexibility because their type parameters are covariant rather than invariant. A parameter that is typed as `Sequence[Union[str, int]]` can accept a `List[int]`, `Sequence[str]`, and a `Sequence[int]`. But a parameter typed as `List[Union[str, int]]` is much more restrictive and accepts only a `List[Union[str, int]]`.
> [Typing Python Libraries @ typing.python.org](https://typing.python.org/en/latest/guides/libraries.html) : "Wide vs. Narrow Types"

---
### Tipagem de funções que retornam mais do que um tipo
> If a function or method can return multiple different types and those types can be determined based on the presence or types of certain parameters, use the `@overload` mechanism defined in [PEP 484](https://www.python.org/dev/peps/pep-0484/#id45). When overloads are used within a “.py” file, they must appear prior to the function implementation, which should not have an `@overload` decorator.
> [Typing Python Libraries @ typing.python.org](https://typing.python.org/en/latest/guides/libraries.html) : "Overloads"

---


