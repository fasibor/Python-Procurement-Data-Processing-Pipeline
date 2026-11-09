"""
1. The business scenario
You are a Junior Data Analyst working for a company that purchases materials from different suppliers.

The procurement manager has noticed three problems:
1. Some suppliers deliver fewer items than ordered.
2. Some procurement records contain incorrect or missing values.
3. Management doesn't know which suppliers offer the best purchasing performance.
Your responsibility is to build a Python-based procurement analysis tool.

Your final deliverables:
- A validated procurement dataset.
- A cleaned and transformed dataset.
- Supplier performance report.
- Procurement cost analysis.
- A summary report saved to a text file.

"""
procurement_data = [
    ["PO001", "Supplier A", "Laptop", 10, 450000, 10, "Delivered"],
    ["PO002", "Supplier B", "Mouse", 50, 5000, 45, "Delivered"],
    ["PO003", "Supplier A", "Keyboard", 20, 12000, 20, "Delivered"],
    ["PO004", "Supplier C", "Monitor", 15, 95000, 12, "Pending"],
    ["PO005", "Supplier B", "Laptop", 5, 455000, 5, "Delivered"],
    ["PO006", "Supplier A", "Mouse", 30, 4800, 30, "Delivered"],
    ["PO007", "Supplier C", "Keyboard", 25, 11500, 20, "Pending"],
    ["PO008", "Supplier B", "Monitor", 10, 98000, 10, "Delivered"],
    ["PO009", "Supplier A", "Laptop", 8, 450000, 7, "Pending"],
    ["PO010", "Supplier C", "Mouse", 40, 5000, 40, "Delivered"],
    ["PO011", "Supplier B", "Keyboard", 15, 12000, 15, "Delivered"],
    ["PO012", "Supplier A", "Monitor", 12, 95000, 10, "Pending"],
    ["PO013", "Supplier C", "Laptop", -2, 460000, 2, "Delivered"],
    ["PO014", "Supplier B", "Mouse", 20, -5000, 20, "Delivered"],
    ["PO015", "Supplier A", "Keyboard", 10, 12000, 12, "Delivered"],
    ["PO016", "Supplier C", "Monitor", 5, 95000, 5, "Delivered"],
    ["PO017", "Supplier B", "Laptop", 4, 455000, 4, "Delivered"],
    ["PO018", "Supplier A", "Mouse", 25, 4800, 25, "Delivered"],
    ["PO019", "Supplier C", "Keyboard", 30, 11500, 28, "Pending"],
    ["PO020", "Supplier B", "Monitor", 8, 98000, 8, "Delivered"]
]

"""
Each record contains:
Position	Column	        Description
0	PO_ID	                Purchase order ID
1	Supplier	            Supplier name
2	Product	                Purchased product
3	Quantity_Ordered	    Quantity requested
4	Unit_Price	            Price per unit
5	Quantity_Delivered	    Quantity received
6	Status	                Delivery status
"""


import os
import csv


def is_purchase_order_valid(po_id,supplier,product,quantity_ordered,unit_price,quantity_delivered=0):

    #1. Texts Validation
    clean_po = po_id is not None and po_id != ""
    clean_supplier = supplier is not None and supplier != ""
    clean_product = product is not None and product != ""

    #2. Numerical Validation and Cleanup
    clean_qty_ordered = quantity_ordered is not None and quantity_ordered > 0
    clean_unit_price = unit_price is not None and unit_price > 0
    clean_qty_delivered = quantity_delivered is not None and quantity_delivered >= 0

    #3. Boolean checks
    if clean_qty_delivered and clean_qty_ordered:
        qty_delivered_validation = quantity_delivered <= quantity_ordered

    else:
        qty_delivered_validation = False

    #4. Group all Conditions
    conditions = [
            clean_po,
            clean_supplier,
            clean_product,
            clean_qty_ordered,
            clean_unit_price,
            clean_qty_delivered,
            qty_delivered_validation
        ]

    if all(conditions):
        return "Valid"

    else:
        return "Invalid"


def generate_procurement_report(imported_procurement, filename="procurement_report.txt"):
    if not imported_procurement:
        return "Error: No procurement data available."

    else:
        try:
            #Purchase orders
            total_purchase_orders = len({x["po_id"] for x in imported_procurement})

            #unique suppliers
            unique_suppliers = len({x["supplier"] for x in imported_procurement})

            #total quantities ordered
            total_qty_ordered = sum(int(x["quantity_ordered"]) for x in imported_procurement)

            #total quantities delivered
            total_qty_delivered = sum(int(x["quantity_delivered"]) for x in imported_procurement)

            #total procurement cost
            total_procurement_cost = sum(int(x["quantity_ordered"]) * int(x["unit_price"]) for x in imported_procurement)

            #Calculations done. Let us write the data in txt
            with open(filename,mode="w",newline="", encoding="utf-8") as report_file:
                report_file.write("========================================\n")
                report_file.write("       PROCUREMENT ANALYSIS REPORT\n")
                report_file.write("========================================\n\n")
                report_file.write("DATASET OVERVIEW\n\n")
                report_file.write(f"Total Purhase Orders: {total_purchase_orders}\n")
                report_file.write(f"Unique Suppliers: {unique_suppliers}\n\n")
                report_file.write("PROCUREMENT METRICS\n\n")
                report_file.write(f"Total Purhase Orders: {total_purchase_orders}\n")
                report_file.write(f"Total Quantity Ordered: {total_qty_ordered}\n")
                report_file.write(f"Total Quantity Delivered: {total_qty_delivered}\n")
                report_file.write(f"Total Procurement Cost: ${total_procurement_cost:,}\n\n")
                report_file.write("========================================\n")
                report_file.write("       END OF REPORT\n")
                report_file.write("========================================\n\n")

                #Return a success message
                return f"Success: Report successfully saved to {filename}"

        except KeyError as ke:
            return f"Error: Missing expected dictionary key - {ke}"
        except ValueError as ve:
            return f"Error: Invalid datatype encountered from numerical calculation: {ve}"
        except Exception as e:
            return f"Error: An error occurred. Couldn't generate report: {e}"



input_file = "raw_procurement.csv"

def load_procurement_records(input_file):
    """Load procurement records from csv file as a list of dicts"""
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"File not found: {input_file}")
    with open(input_file,mode="r",newline="",encoding="utf-8") as file:
        return list(csv.DictReader(file))

def validate_and_clean(record):
    """
    Convert numeric fields, then validate with is_purchase_order_valid().
    Returns (cleaned_record, None) if valid, or (None, reason) if invalid.
    """
    try:
        quantity_ordered = int(record["quantity_ordered"])
        quantity_delivered = int(record["quantity_delivered"])
        unit_price = float(record["unit_price"])

    except (KeyError, ValueError, TypeError):
        return None,"missing or non-numeric quantity or price"

    verdict = is_purchase_order_valid(
        record.get("po_id"),
        record.get("supplier"),
        record.get("product"),
        quantity_ordered,
        unit_price,
        quantity_delivered,
    )
    if verdict != "Valid":
        return None, "failed validation rules"

    return {
        **record,
        "quantity_ordered": quantity_ordered,
        "quantity_delivered": quantity_delivered,
        "unit_price": unit_price,
    }, None


def run_procurement_pipeline(input_file, output_file):
    """Orchestrates: load -> validate -> separate -> transform -> report -> summary."""

    # 1. Load
    try:
        records = load_procurement_records(input_file)
    except Exception as e:
        return {
            "error": f"Could not load records: {e}",
            "total_records_processed": 0,
            "valid_records": 0,
            "invalid_records": 0,
            "total_procurement_cost": 0,
            "report_filename": None,
        }

    # 2 & 3. Validate and separate
    valid_records, invalid_records = [], []
    for row_number, record in enumerate(records, start=2):  # row 1 is the header
        cleaned, reason = validate_and_clean(record)
        if cleaned:
            valid_records.append(cleaned)
        else:
            invalid_records.append(
                {"row": row_number, "po_id": record.get("po_id"), "reason": reason}
            )

    # 4. Add total_cost to valid records
    valid_records = list(map(
        lambda x: {**x, "total_cost": x["quantity_ordered"] * x["unit_price"]},
        valid_records,
    ))

    # 5. Generate the report (valid records only)
    report_status = generate_procurement_report(valid_records, filename=output_file)
    report_ok = report_status.startswith("Success")

    # 6. Summary
    return {
        "total_records_processed": len(records),
        "valid_records": len(valid_records),
        "invalid_records": len(invalid_records),
        "total_procurement_cost": round(sum(r["total_cost"] for r in valid_records), 2),
        "report_filename": output_file if report_ok else None,
        "report_status": report_status,
        "invalid_details": invalid_records,
    }


summary = run_procurement_pipeline("raw_procurement.csv", "procurement_report.txt")
for key, value in summary.items():
    print(f"{key}: {value}")
