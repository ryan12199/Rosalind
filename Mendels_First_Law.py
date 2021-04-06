# Code for Mendel's First Law Problem

def mendel(k: int, m: int, n: int) -> float:
"""
Calculates the probability that two randomly selected mating pairs will produce an offspring with a dominant allele given a population with k homozygous dominant organisms for a certain factor, m heterozygous organisms and n homozygous recessive organisms. k,m and n are all positive integers.
"""
# Divide
dominant_ways = k* (k + m + n - 1) + n * (k + m/2)