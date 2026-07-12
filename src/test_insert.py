from maritime_service import add_voyage

rows = add_voyage(
    1,
    1,
    2,
    "2026-07-01",
    "2026-07-10",
    "Active"
)

print(rows)