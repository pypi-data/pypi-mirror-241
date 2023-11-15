from typing import Dict, List, Optional, Tuple

class ReactionSystem:
    def __init__(self, bg_size: int) -> None:
        ...

    
    def from_cycle(cycle: List[List[int]], bg_size: Optional[int] = None) -> ReactionSystem:
        """
        Creates a new ReactionSystem from a cycle using maximally inhibited reactions.
        Does not check for repeated states.
        Any state not in the cycle must map to the empty set.

        :param cycle: List of states in the cycle
        :param bg_size: The bg_size of the rsfunction. 
        Defaults to the smallest bg_size that contains every element of the cycle, which errors if the only element is empty.
        :return: An RsFunction containing the cycle
        """
        ...

    def push(*args) -> bool:
        """
        Adds a reaction to the reaction system. 
        Returns false if the reaction contains a contradiction (reactants and inhibitors share an element)

        The function signature allows both of the following usages:
        - push(reactants: List[int], inhibitors: List[int], products: List[int]) -> bool
        - push(reaction: Reaction) -> bool
        """
        ...
    
    def push_state(self, state: List[int], products: List[int]) -> None:
        """
        Adds a maximally inhibited reaction to the reaction system.
        Therefore, self.result(state) will contain products but need not equal products.
        """
        ...

    def remove(*args) -> None:
        """
        Removes a reaction from the reaction system.

        The function signature allows both of the following usages:
        - remove(reactants: List[int], inhibitors: List[int], products: List[int])
        - remove(reaction: Reaction)
        """
        ...

    def result(self, state: List[int]) -> List[int]:
        ...

    def reactions(self) -> List[Reaction]:
        ...

    def enabled(self, state: List[int]) -> bool:
        ...

    def degree(self) -> int:
        ...

    def rank(self) -> int:
        ...

    def minimize_rank(self) -> 'ReactionSystem':
        ...

    def minimize_rank_exact(self) -> 'ReactionSystem':
        ...

    def minimize_degree(self) -> 'ReactionSystem':
        ...

    def complement(self) -> 'ReactionSystem':
        ...

    def primes(self) -> 'ReactionSystem':
        ...

    def essential_primes(self) -> 'ReactionSystem':
        ...

    def achieve_rank_degree(self, rank_bound: Optional[int] = None, degree_bound: Optional[int] = None) -> Optional['ReactionSystem']:
        """
        Achieve a reaction system with specified rank and degree bounds.

        :param rank_bound: Maximum rank for the resulting reaction system. None for looking for a reaction system with minimum rank.
        :param degree_bound: Maximum degree for the resulting reaction system. None for looking for a reaction system with minimum degree.
        :return: Result containing either the resulting reaction system or None.
        """
        ...

    def __str__(self) -> str:
        ...

    def __repr__(self) -> str:
        ...

class Reaction:
    def __init__(self, reactants: List[int], inhibitors: List[int], products: List[int]) -> None:
        ...

    def enabled(self, state: List[int]) -> bool:
        ...

    def reactants(self) -> List[int]:
        ...

    def inhibitors(self) -> List[int]:
        ...

    def products(self) -> List[int]:
        ...

    def min_bg_size(self) -> int:
        """
        Returns the largest element used in the reaction.

        :return: The maximum value among the elements in the reactants, inhibitors, and products of the reaction.
        """
        ...

    def deconstruct(self) -> Tuple[List[int], List[int], List[int]]:
        """
        Deconstructs the reaction into its components.

        :return: A tuple containing three lists representing the reactants, inhibitors, and products of the reaction.
        """
        ...

    def result(self, state: List[int]) -> List[int]:
        ...

    def __str__(self) -> str:
        ...

    def __repr__(self) -> str: 
        ...

class RsFunction:
    def __init__(self, bg_size: int) -> None:
        ...

    def from_cycle(cycle: List[List[int]], bg_size: Optional[int] = None) -> RsFunction:
        """
        Creates a new RsFunction from a cycle.
        Does not check for repeated states.

        :param cycle: List of states in the cycle
        :param bg_size: The bg_size of the rsfunction. 
        Defaults to the smallest bg_size that contains every element of the cycle, which errors if the only element is empty.
        :return: An RsFunction containing the cycle
        """
        ...

    def add(self, input: List[int], output: List[int]) -> Optional[List[int]]:
        ...

    def remove(self, input: List[int]) -> Optional[List[int]]:
        ...

    def minimize_rank(self) -> ReactionSystem:
        ...

    def minimize_rank_exact(self) -> ReactionSystem:
        ...

    def minimize_degree(self) -> ReactionSystem:
        ...

    def complement(self) -> ReactionSystem:
        ...

    def primes(self) -> ReactionSystem:
        ...

    def essential_primes(self) -> ReactionSystem:
        ...

    def achieve_rank_degree(self, rank_bound: Optional[int] = None, degree_bound: Optional[int] = None) -> Optional[ReactionSystem]:
        """
        Achieve a reaction system with specified rank and degree bounds.

        :param rank_bound: Maximum rank for the resulting reaction system. None for looking for a reaction system with minimum rank.
        :param degree_bound: Maximum degree for the resulting reaction system. None for looking for a reaction system with minimum degree.
        :return: Result containing either the resulting reaction system or None.
        """
        ...


    def map(self) -> Dict[Tuple[int], List[int]]:
        """
        Returns a mapping of input states to output states in the function.

        :return: A dictionary where keys are input vectors and values are corresponding output vectors.
        """
        ...

    def support(self) -> List[List[int]]:
        """
        Returns the support of the function, i.e., the set of input states that map to a non-empty set.

        :return: A list of input vectors in the support of the function.
        """
        ...

    def mapped_domain(self) -> List[List[int]]:
        """
        Returns the mapped domain of the function, i.e., the set of input vectors that map to any set.

        :return: A list of input vectors in the mapped domain of the function.
        """
        ...


    def __str__(self) -> str:
        ...

    def __repr__(self) -> str: 
        ...
    
    def __len__(self) -> int:
        ...

