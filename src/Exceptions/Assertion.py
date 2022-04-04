def KelvinToFahrenheit(Temperature):
   assert (Temperature >= 0),'Temperature can not be colder than absolute zero!'
   return ((Temperature-273)*1.8)+32

print(int(KelvinToFahrenheit(273)))
print(int(KelvinToFahrenheit(505.78)))
print(KelvinToFahrenheit(-5))