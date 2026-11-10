
# Python Procurement Data Processing Pipeline

## Project Overview

This project demonstrates how Python can be used to automate procurement data processing through a structured pipeline.

The solution loads procurement records from a CSV file, validates and cleans the data, separates valid and invalid purchase orders, calculates procurement costs, and generates an automated procurement analysis report.

The project focuses on reusable functions, data validation, exception handling, data transformation, and function orchestration.

<img width="1536" height="1024" alt="data processing pipeline" src="https://github.com/user-attachments/assets/1ebfa446-9c23-4729-afd3-51d7e60d4086" />


## Project Objectives

1. Automate procurement data ingestion from CSV files.
2. Validate purchase order records using predefined business rules.
3. Identify and separate valid and invalid records.
4. Clean and standardize numerical data.
5. Calculate total procurement costs for individual purchase orders.
6. Generate an automated procurement analysis report.
7. Return a summary of pipeline execution.

## Technologies Used

- Python
- CSV
- OS

### Python Concepts Practiced

- Functions and function composition
- Positional and keyword arguments
- Default arguments
- Lists, dictionaries, and sets
- Dictionary unpacking
- List comprehensions
- `map()` and `lambda`
- `enumerate()`
- Exception handling (`try/except`)
- File handling
- CSV data processing
- Data validation and transformation
- Function orchestration

## Pipeline Architecture

The project follows a modular data-processing workflow:

1. **Data Ingestion:** Load procurement records from a CSV file using `csv.DictReader`.
2. **Data Validation:** Check purchase order IDs, suppliers, products, quantities, and unit prices.
3. **Data Cleaning:** Convert numerical fields into appropriate data types.
4. **Record Separation:** Separate valid purchase orders from invalid records and capture rejection reasons.
5. **Data Transformation:** Calculate the total cost of each valid purchase order.
6. **Report Generation:** Generate a procurement analysis report using validated records.
7. **Pipeline Summary:** Return execution metrics, including processed records, valid records, invalid records, and total procurement cost.

## Validation Rules

| Field | Validation Rule |
|---|---|
| PO ID | Must not be empty |
| Supplier | Must not be empty |
| Product | Must not be empty |
| Quantity Ordered | Must be greater than zero |
| Unit Price | Must be greater than zero |
| Quantity Delivered | Must be zero or greater |
| Quantity Delivered | Must not exceed quantity ordered |

Records that fail validation are excluded from the valid procurement dataset.

## Key Calculations

**Total Purchase Order Cost**

`Total Cost = Quantity Ordered × Unit Price`

**Total Procurement Cost**

`Total Procurement Cost = Sum of all valid purchase order costs`

## Project Structure

```text
python-procurement-pipeline/
│
├── raw_procurement.csv
├── procurement_pipeline.py
├── procurement_report.txt
└── README.md
```

## Pipeline Execution

The orchestrator function coordinates the entire processing workflow.

```python
summary = run_procurement_pipeline(
    "raw_procurement.csv",
    "procurement_report.txt"
)

for key, value in summary.items():
    print(f"{key}: {value}")
```

## Expected Output

The pipeline returns a summary dictionary containing:

```python
{
    "total_records_processed": 9,
    "valid_records": 7,
    "invalid_records": 2,
    "total_procurement_cost": 2500000.0,
    "report_filename": "procurement_report.txt"
}
```

*Note: These figures are illustrative and not verified execution results.*

## Generated Procurement Report

The report contains:

- Total purchase orders
- Number of unique suppliers
- Total quantity ordered
- Total quantity delivered
- Total procurement cost

## Error Handling

The pipeline incorporates exception handling to manage common data-processing issues, including:

- Missing CSV files
- Missing dictionary keys
- Invalid numerical values
- Unexpected data types
- Report generation errors

Invalid records are also tracked with their CSV row numbers, purchase order IDs, and rejection reasons.

## Learning Outcomes

Through this project, I strengthened my understanding of how individual Python functions can work together to solve practical data-processing problems.

Key takeaways include:

1. Breaking complex tasks into smaller, reusable functions.
2. Separating data validation from data transformation.
3. Using Python's built-in libraries to automate CSV workflows.
4. Handling invalid data without interrupting the entire pipeline.
5. Using an orchestrator function to coordinate multiple processing stages.
6. Generating structured outputs from raw datasets.

## Future Improvements

- Export rejected purchase orders into a separate CSV file.
- Introduce more comprehensive data-quality checks.
- Add supplier-level procurement performance analysis.
- Generate visual procurement dashboards using Power BI.
- Introduce automated testing with Python's `unittest` or `pytest`.
- Add logging to monitor pipeline execution.

## Conclusion

This project demonstrates how Python can be used to move beyond basic data manipulation and build a reusable data-processing workflow.

It combines data ingestion, validation, cleaning, transformation, and reporting into a single orchestrated pipeline.

The broader objective is to develop practical Python skills for real-world data analytics and automation challenges.
