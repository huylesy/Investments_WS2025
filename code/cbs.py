ask = int(input("Nhap 1 de tinh bai toan BA Merchant, nhap 2 de tinh bai toan Merchant: "))
CF = int(input("Nhap CF"))
r = float(input("Nhap r"))
g = -0.02
opex = int(input("Nhap opex"))
capex = int(input("Nhap capex"))

def bamerchant(CF, r, g):
    Tolling = ((CF - opex) / (r - g)) * (1 - ((1 + g) / (1 + r))**15) - (capex * 0.20)
    Floor = ((CF - opex) / (r+0.02 - g)) * (1 - ((1 + g) / (1 + r+0.02))**15) - (capex * 0.35)
    Merchant = ((CF - opex) / (r+0.03 - g)) * (1 - ((1 + g) / (1 + r+0.03))**15) - (capex * 0.50)

    print (Tolling, Floor, Merchant)


bamerchant(CF, r, g)

def merchant(CF, r, g):
    all = ((CF - opex) / (r - g)) * (1 - ((1 + g) / (1 + r))**15) - (capex * 0.50)
    

    print (all)

if ask == 2:
    merchant(CF, r, g)
elif ask == 1:
    bamerchant(CF, r, g)