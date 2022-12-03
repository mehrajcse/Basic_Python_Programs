''' Question no. 10
In a town, the percentage of men is 52. The percentage of total literacy is 48.
If total percentage of literate men is 35 of the total population, write a program
to find the total number of illiterate men and women if the population of the
town is 80,000
'''

#Program to find the number of illiterate men and women in a town

total_population=80000
print("Total population of a town = ",total_population)
total_literacy=48/100*total_population
print("The percentage of total literacy is 48% which is : ",total_literacy)
total_illiteracy=total_population-total_literacy
print("Therefore total illiterate persons in town are : ",total_illiteracy)

men_population=52/100*total_population
women_population=total_population-men_population

print("Population of men = ",men_population)
print("Population of women = ",women_population)


literate_men=35/100*total_population
literate_women=women_population-literate_men

print("Population of literate men : ",literate_men)
print("Population of literate womwn : ",literate_women)


illiterate_men = men_population-literate_men
illiterate_women =women_population-literate_women
print("\n")

print("Total number of illiterate men : ",illiterate_men)
print("Total number  of illiterate women : ",illiterate_women)

