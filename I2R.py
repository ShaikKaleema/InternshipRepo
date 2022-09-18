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