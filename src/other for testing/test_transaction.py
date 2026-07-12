from maritime_service import create_voyage_with_cargo

voyage_id = create_voyage_with_cargo(

    vessel_id=1,
    departure_port_id=1,
    arrival_port_id=2,
    departure_date="2026-07-10",
    arrival_date="2026-07-20",
    status="Active",

    cargo_type="Coal",
    weight_tons=5000

)

print(voyage_id)