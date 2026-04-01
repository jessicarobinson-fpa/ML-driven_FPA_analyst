"""
Paths, constants, and department mappings for the HC variance project.
"""
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_INTERIM = PROJECT_ROOT / "data" / "interim"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"
REPORTS_DIR = PROJECT_ROOT / "reports"

CLOSE_FILE_PATH = Path.home() / "Desktop" / "Cursor Files" / "Headcount Project" / "Close File - Master.xlsx"
OUTPUT_DIR = Path.home() / "Desktop" / "Cursor Files" / "Headcount Project"

SEED = 42

HC_TABS = ["HC", "HC-US", "HC-India", "HC-RD", "HC-Colleen"]

ENTITIES = ["US", "India", "RD", "Colleen"]

DEPARTMENT_HIERARCHY = {
    "Entrata": {
        "COR": [
            "COR Only",
            "Fulfillment",
            "ResidentUtility",
            "UEM",
            "Invoice Processing",
            "Implementation",
            "Leasing Center",
            "ResidentInsure",
            "Site Reliability",
            "Support",
            "Training",
            "Digital Marketing",
            "ResidentVerify",
        ],
        "S&M": [
            "Sales",
            "Marketing",
            "Customer Success",
        ],
        "R&D": [
            "Engineering",
            "Product",
        ],
        "G&A": [
            "Finance",
            "Executive",
            "Legal",
            "People & Places",
            "IT",
            "SBO",
            "Payments",
        ],
    }
}

ZERO_HC_ROWS = [
    "COR Only",
    "COR Only - US",
    "COR Only - India",
    "COR Only - ResidentInsure",
    "COR Only - Digital Marketing",
    "COR Only - RD",
    "COR Only - Support RD",
    "COR Only - Colleen",
    "COR Only (Only)",
]
