''' Question no. 10
In a town, the percentage of men is 52. The percentage of total literacy is 48.
If total percentage of literate men is 35 of the total population, write a program
to find the total number of illiterate men and women if the population of the
town is 80,000
'''

#Program to find the number of illiterate men and women in a town

TOTAL_POPULATION=80000
print("Total population of a town = ",TOTAL_POPULATION)
TOTAL_LITERACY=48/100*TOTAL_POPULATION
print("The percentage of total literacy is 48% which is : ",TOTAL_LITERACY)
TOTAL_ILLITERACY=TOTAL_POPULATION-TOTAL_LITERACY
print("Therefore total illiterate persons in town are : ",TOTAL_ILLITERACY)

MEN_POPULATION=52/100*TOTAL_POPULATION
WOMEN_POPULATION=TOTAL_POPULATION-MEN_POPULATION

print("Population of men = ",MEN_POPULATION)
print("Population of women = ",WOMEN_POPULATION)


LITERATE_MEN=35/100*TOTAL_POPULATION
LITERATE_WOMEN=WOMEN_POPULATION-LITERATE_MEN

print("Population of literate men : ",LITERATE_MEN)
print("Population of literate womwn : ",LITERATE_WOMEN)


ILLITERATE_MEN = MEN_POPULATION-LITERATE_MEN
ILLITERATE_WOMEN =WOMEN_POPULATION-LITERATE_WOMEN
print("\n")

print("Total number of illiterate men : ",ILLITERATE_MEN)
print("Total number  of illiterate women : ",ILLITERATE_WOMEN)
