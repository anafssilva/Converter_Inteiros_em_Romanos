
def converter_romano(num):
     
 m = ['', 'M', 'MM', 'MMM']
 c = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC','DCC','DCCC', 'CM']
 d = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
 u = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']


 resposta = m [num // 1000]
 resposta += c [num // 100 % 10]
 resposta += d [num // 10 % 10]
 resposta += u [num // 1 % 10]
 return resposta


num= input('Digite um número: ')
num= int(num)
if num > 0 and num < 4000:
   print(converter_romano(num))



def converter_numero(romano):
  
 d1 = {
    'M': 1000, 'C': 100, 'D': 500, 'L':50, 'X':10, 'V':5, 'I':1
      }
 
 resultado = 0
 numero_anterior = 0
 for i in romano:
  numero = d1[i]
  if  numero_anterior == 0 or numero <= numero_anterior:  
    resultado += numero
  else:
    resultado += numero
    resultado -= (numero_anterior*2)
  numero_anterior = numero
 return resultado

romano = input('Digite um número em algarismo romano: ')
print(converter_numero(romano))