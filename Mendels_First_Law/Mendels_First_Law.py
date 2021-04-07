# Code for Mendel's First Law Problem

def homozygous_prob(k: int, m: int, n: int) -> float:
"""
Calculates the oddds of two random organisms from a population producing an offspring with a dominant allele for a certain gene when the population is composed of k organisms who are homozygous dominant, m organisms who are heterozygous and n organisms who are homozygous recessive
"""
# if the first organism in the pair is homozygous dominant, the offspring will have a dominant allele
prob_first_homo_dom = k/(k + m + n)

# if the first organism is heterozygous and it passes on its dominant allele,  the offspring will have a dominant allele
prob_first_hetero_dom = m/(k + m + n) * 0.5

# if the first organism is heterozygous and it passes on its recessive allele or the first organism is recessive and the second organism is homozygous dominant, the offspring will have a dominant allele
prob_second_homo_dom = (m/(k + m + n) * 0.5 + n/(k + m + n)) * k/(k + m + n - 1)

# if the first organism is homozygous recessive and the second organism is heterozygous and it passes on its dominant allele, the offspring will have a dominant allele
prob_first_homo_rec_second_hetero_dom = n/(k + m + n) * m/(k + m + n - 1) * 0.5

# if the first organism is heterozygous and the second organism is heterozygous and only the second passes on its dominant allele, the offspring will have a dominant allele
prob_hetero_second_dom = m/(k + m + n) * 0.5 * (m-1)/(k + m + n - 1) * 0.5

# The total probability that the offspring has a dominant gene is equal to the sum of all the possible scenarios that lead to the offspring having a dominant gene
return(prob_first_homo_dom + prob_first_hetero_dom + prob_second_homo_dom + prob_first_homo_rec_second_hetero_dom + prob_hetero_second_dom)
