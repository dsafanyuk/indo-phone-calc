has_npwp = False
device_value_usd = float(input("What is your device value (USD): "))
tax_deduction_value_usd = 500.00
product_val_taxed = device_value_usd - tax_deduction_value_usd
import_tax = product_val_taxed * 0.1
total_import_val = import_tax + product_val_taxed
vat = total_import_val * 0.1
income_tax_npwp = total_import_val * 0.1
income_tax_without_npwp = total_import_val * 0.2
total_taxes = 0.00
if has_npwp:
    total_taxes = import_tax + vat + income_tax_npwp
else:
    total_taxes = import_tax + vat + income_tax_without_npwp

print("Total Taxes: " + str(total_taxes))

