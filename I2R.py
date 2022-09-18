#Integer to Roman conversion
class Solution:
    def intToRoman(self, num: int) -> str:
        num1=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        rom=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        rom_num=""
        i=0
        while num>0:
            for _ in range(num//num1[i]):
                rom_num=rom_num+rom[i]
                num=num-num1[i]
            i=i+1
        return rom_num