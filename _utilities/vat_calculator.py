orig = int(input("Enter the original amount: "))

vat_rate = 0.20
vat_amount = orig * vat_rate
total_with_vat = orig + vat_amount

print(f"The total amount plus VAT is £{total_with_vat:.2f}")
