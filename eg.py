invoice_data = {
    "header": {
        "invoice_no": "72346654",
        "invoice_date": "10/25/2015",
        "seller": "Malone-Lopez 851 Hall Extensions Apt. 554 Port Yolandaland, WY 20517",
        "client": "Perez Group 480 Destiny Ridge Suite 247 Port Laura, IL 30520",
        "seller_tax_id": "955-96-9323",
        "client_tax_id": "927-90-3514",
        "iban": "GB98THYE24829931003032"
    },
    "items": [
        {
            "item_desc": "NWT Women's MAX EDITION Classy Gray Knit Stretch Dress side bow tie 3/4 sleeve XL",
            "item_qty": "3,00",
            "item_net_price": "12,50",
            "item_net_worth": "37,50",
            "item_vat": "10%",
            "item_gross_worth": "41,25"
        },
        {
            "item_desc": "Rebecca Minkoff Black Polyester Fringe and Lambskin Dress Sz 12",
            "item_qty": "2,00",
            "item_net_price": "9,99",
            "item_net_worth": "19,98",
            "item_vat": "10%",
            "item_gross_worth": "21,98"
        },
        {
            "item_desc": "balmain dress 36",
            "item_qty": "4,00",
            "item_net_price": "1550,00",
            "item_net_worth": "6200,00",
            "item_vat": "10%",
            "item_gross_worth": "6820,00"
        },
        {
            "item_desc": "sandro dress",
            "item_qty": "5,00",
            "item_net_price": "80,00",
            "item_net_worth": "400,00",
            "item_vat": "10%",
            "item_gross_worth": "440,00"
        },
        {
            "item_desc": "Kate Spade NY Sleeveless Ponte Fit & Flare Solid Black Dress Size 6",
            "item_qty": "2,00",
            "item_net_price": "49,99",
            "item_net_worth": "99,98",
            "item_vat": "10%",
            "item_gross_worth": "109,98"
        }
    ],
    "summary": {
        "total_net_worth": "$6757,46",
        "total_vat": "$ 675,75",
        "total_gross_worth": "$7433,21"
    }
}

# Verify and print header information
header = invoice_data.get('header', {})
print("Header Information:")
print(f"Invoice Number: {header.get('invoice_no', 'N/A')}")
print(f"Invoice Date: {header.get('invoice_date', 'N/A')}")
print(f"Seller: {header.get('seller', 'N/A')}")
print(f"Client: {header.get('client', 'N/A')}")
print(f"Seller Tax ID: {header.get('seller_tax_id', 'N/A')}")
print(f"Client Tax ID: {header.get('client_tax_id', 'N/A')}")
print(f"IBAN: {header.get('iban', 'N/A')}")

# Verify and print item details
items = invoice_data.get('items', [])
print("\nItems:")
for index, item in enumerate(items):
    print(f"Item {index + 1}:")
    print(f"  Description: {item.get('item_desc', 'N/A')}")
    print(f"  Quantity: {item.get('item_qty', 'N/A')}")
    print(f"  Net Price: {item.get('item_net_price', 'N/A')}")
    print(f"  Net Worth: {item.get('item_net_worth', 'N/A')}")
    print(f"  VAT Rate: {item.get('item_vat', 'N/A')}")
    print(f"  Gross Worth: {item.get('item_gross_worth', 'N/A')}")

# Verify and print summary information
summary = invoice_data.get('summary', {})
print("\nSummary:")
print(f"Total Net Worth: {summary.get('total_net_worth', 'N/A')}")
print(f"Total VAT: {summary.get('total_vat', 'N/A')}")
print(f"Total Gross Worth: {summary.get('total_gross_worth', 'N/A')}")
