import random
from typing import List, Tuple

ALPHABET: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
POPULATION_SIZE: int = 40
MUTATION_RATE: float = 0.1
# GENERATIONS: int = 1000
TARGET: str = "GENETIC"

def random_token(alphabet=ALPHABET) -> str:
    return random.choice(alphabet)

def select_parents(mating_pool: List[str]) -> Tuple[str, str]:
    parent1: str = random.choice(mating_pool)
    parent2: str = random.choice(mating_pool)
    while parent1 == parent2:
        parent2: str = random.choice(mating_pool)
        
    return parent1, parent2

def fitness(target: str, organism: str) -> int:
    return sum([1 for ct, co in zip(target, organism) if ct == co])

def create_organism(length: int) -> str:
    return "".join([random_token() for _ in range(length)])

def create_population(length: int, x: int=POPULATION_SIZE) -> List[str]:
    return [create_organism(length) for _ in range(x)]

def selection(scores: List[Tuple[str, int]]) -> List[str]:
    return [organism for organism, _ in scores[: POPULATION_SIZE // 2]]

def crossover(parent1: str, parent2: str) -> str:
    split: int = random.randint(0, len(TARGET) - 1)
    return parent1[:split] + parent2[split:]

def mutate(organism: str) -> str:
    if random.random() < MUTATION_RATE:
        mutated_gene: int = random.randint(0, len(TARGET))
        organism = f"{organism[:mutated_gene]}{random_token()}{organism[mutated_gene + 1:]}"
    return organism

if __name__ == "__main__":
    population: List[str] = create_population(len(TARGET))
    
    # for gidx in range(GENERATIONS):
    while True:
        scores = sorted([(organism, fitness(TARGET, organism)) for organism in population],
                        key=lambda x: x[1],
                        reverse=True)
        print(scores)

        if scores[0][0] == TARGET:
            break

        mating_pool: List[str] = selection(scores)

        population = []
        while (len(population) < POPULATION_SIZE):
            parent1, parent2 = select_parents(mating_pool)
            
            population.append(mutate(crossover(parent1, parent2)))
