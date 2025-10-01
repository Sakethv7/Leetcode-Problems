class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        #numexchange value gives us 1 full bottle
        res = 0
        empty = 0 #track empty bottles separately

        while numBottles > 0:
            res += numBottles
            empty += numBottles # filled become emoty after drinking
            numBottles =  empty // numExchange #calculate drinkable water after exchange by inter division of empty and exchange rate
            empty  = empty % numExchange
        
        return res





