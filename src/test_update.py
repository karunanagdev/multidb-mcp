from maritime_service import update_voyage_status

rows = update_voyage_status(
    105,
    "Flying"
)

print(rows)