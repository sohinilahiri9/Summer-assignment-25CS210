# Salary Management System
print("--- Salary Management ---")
basic = int(input("Enter basic salary: "))

hra = basic * 0.20 # 20% of basic
da = basic * 0.10 # 10% of basic
pf = basic * 0.12 # 12% of basic

gross = basic + hra + da
net = gross - pf

print("\n--- Salary Slip ---")
print("Basic Salary:", basic)
print("HRA:", hra)
print("DA:", da)
print("Gross Salary:", gross)
print("PF Deduction:", pf)
print("Net Salary:", net)