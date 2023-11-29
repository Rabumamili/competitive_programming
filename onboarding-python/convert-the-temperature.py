class Solution(object):
    def convertTemperature(self, celsius):
         farenheit =  1.80*celsius + 32
         Kelvin = celsius + 273.15
         return[Kelvin, farenheit]