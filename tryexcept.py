#ÖRNEK 1
"""try:
    a = int("bu yanlış1234")

except ValueError:
    print("Bir Hata oluştu")
print("Bloklar sona erdi")"""


#ÖRNEK 2
"""try:
    
    a = int(input("Sayı1:"))
    b = int(input("Sayı2:"))
    print(a/b)

    
except ValueError:
    print("Lütffen inputu doğru girin")

except ZeroDivisionError:
    print("Bir sayı 0'a bölünemez")
print("Bloklar sona erdi")"""


# FİNALLY
"""try:
    
    a = int(input("Sayı1:"))
    b = int(input("Sayı2:"))
    print(a/b)

    
except ValueError:
    print("Lütffen inputu doğru girin")

except ZeroDivisionError:
    print("Bir ssayı 0'a bölünemez")2

finally:
    print("Burası da çalıştı")

print("Bloklar sona erdi")"""


# HATA FIRLATMA
def terscevir(s):
    if (type(s)!=str):
        raise ValueError("Lütfen string bir değer gönderin.")
    else:
        return s[::-1]

print(terscevir(12))






