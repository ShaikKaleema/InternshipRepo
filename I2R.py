#Integer to Roman conversion
class Solution:
    def intToRoman(self, num: int) -> str:
        num1=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        rom=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        rom_num=""
        i=0
        while num:
            div=num//num1[i]
            num%=num1[i]
            while div:
                rom_num+=rom[i]
                div-=1
            i+=1
        return rom_num
    


#Created a list of dictionary Elements Instead Of Two array.
#def intToRoman(num: int) -> str:
#        defaultList= [
#          {"romanSymbl":"M","NumericalValue":1000},
#          {"romanSymbl":"CM","NumericalValue":900},
#          {"romanSymbl":"D","NumericalValue":500},
#          {"romanSymbl":"CD","NumericalValue":400},
#          {"romanSymbl":"C","NumericalValue":100},
#          {"romanSymbl":"XC","NumericalValue":90},
#          {"romanSymbl":"L","NumericalValue":50},
#          {"romanSymbl":"XL","NumericalValue":40},
#          {"romanSymbl":"X","NumericalValue":10},
#          {"romanSymbl":"IX","NumericalValue":9},
#          {"romanSymbl":"V","NumericalValue":5},
#          {"romanSymbl":"IV","NumericalValue":4},
#          {"romanSymbl":"I","NumericalValue":1},
#        ] 
#        rom_num=""
#        i=0
#        while num:
#            div=num//int(defaultList[i]["NumericalValue"])
#            num%=int(defaultList[i]["NumericalValue"])
#            while div:
#                rom_num+=defaultList[i]["romanSymbl"]
#                div-=1
#            i+=1
#        return rom_num
#print(intToRoman(50))



    
