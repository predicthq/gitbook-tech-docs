import csv
import os
import re
import sys

# Fetches the current list of event labels from the PredictHQ API, stores both
# label fields as CSVs in assets/, and regenerates the PHQ Label values table
# in the Labels page. Run daily by .github/workflows/fetch-labels.yaml, which
# commits only when something changed.
#
# The page update replaces everything between the PAGE_HEADING line and the
# next markdown heading in LABELS_PAGE. If the heading is missing or the API
# call fails, the script exits non-zero so the workflow run fails visibly.
#
# Usage:
#   python3 scripts/fetch-labels.py             # fetch from API (needs PHQ_API_TOKEN)
#   python3 scripts/fetch-labels.py --offline   # re-render the page from existing CSVs

LEGACY_CSV = "assets/legacy-labels.csv"
PHQ_CSV = "assets/phq-labels.csv"
LABELS_PAGE = "docs/tech-docs/getting-started/predicthq-data/labels.md"
PAGE_HEADING = "#### All PHQ Label values"
PHQ_CSV_URL = "https://raw.githubusercontent.com/predicthq/gitbook-tech-docs/main/assets/phq-labels.csv"
TABLE_COLUMNS = 4


def fetch_labels():
    import requests
    from dotenv import load_dotenv

    load_dotenv()
    response = requests.get(
        "https://api.predicthq.com/v1/events/count/",
        headers={"Authorization": f"Bearer {os.getenv('PHQ_API_TOKEN')}"},
    )
    if response.status_code != 200:
        sys.exit(f"Failed to fetch labels, status code: {response.status_code}")
    data = response.json()
    return sorted(data["labels"].keys()), sorted(data["phq_labels"].keys())


def read_csv_labels(path):
    with open(path, newline="") as file:
        return [row[0] for row in csv.reader(file) if row]


def write_csv_labels(path, labels):
    with open(path, "w", newline="") as file:
        writer = csv.writer(file)
        for label in labels:
            writer.writerow([label])


def render_section(phq_labels):
    lines = [
        PAGE_HEADING,
        "",
        f"The full list of {len(phq_labels)} PHQ Label values, refreshed daily "
        f"from the live API. Prefer a CSV? Download [phq-labels.csv]({PHQ_CSV_URL}).",
        "",
    ]
    header = "| " + " | ".join([" "] * TABLE_COLUMNS) + " |"
    divider = "| " + " | ".join(["---"] * TABLE_COLUMNS) + " |"
    lines.append(header)
    lines.append(divider)
    for i in range(0, len(phq_labels), TABLE_COLUMNS):
        row = phq_labels[i : i + TABLE_COLUMNS]
        row += [""] * (TABLE_COLUMNS - len(row))
        cells = [f"`{label}`" if label else " " for label in row]
        lines.append("| " + " | ".join(cells) + " |")
    lines.append("")
    return "\n".join(lines)


def update_labels_page(phq_labels):
    with open(LABELS_PAGE) as file:
        page = file.read()

    pattern = re.compile(
        rf"^{re.escape(PAGE_HEADING)}\n.*?(?=^#{{1,6}} )", re.M | re.S
    )
    if not pattern.search(page):
        sys.exit(
            f"Could not find the '{PAGE_HEADING}' section followed by another "
            f"heading in {LABELS_PAGE} - not modifying the page."
        )

    page = pattern.sub(render_section(phq_labels) + "\n", page, count=1)
    with open(LABELS_PAGE, "w") as file:
        file.write(page)


def main():
    if "--offline" in sys.argv:
        phq_labels = read_csv_labels(PHQ_CSV)
    else:
        legacy_labels, phq_labels = fetch_labels()
        write_csv_labels(LEGACY_CSV, legacy_labels)
        write_csv_labels(PHQ_CSV, phq_labels)
    update_labels_page(phq_labels)
    print(f"Success: {len(phq_labels)} PHQ Labels")


if __name__ == "__main__":
    main()
