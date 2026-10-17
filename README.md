[![CI](https://github.com/projectashutosh02/mandi-ingest/actions/workflows/ci.yml/badge.svg)](https://github.com/projectashutosh02/mandi-ingest/actions/workflows/ci.yml)

# mandi-ingest

Clean and validate Indian mandi (wholesale market) crop-price data from Agmarknet.

## What it does
- Cleans market names (`normalize_name`): removes extra spaces and fixes capitalisation.
- Converts prices from ₹ per quintal to ₹ per kg (`quintal_to_kg`).
- Checks that a price row makes sense (`is_price_consistent`): all prices above 0 and min ≤ modal ≤ max.

## Data
Agmarknet prices published on data.gov.in. Prices are in ₹ per quintal (1 quintal = 100 kg).

## Run the tests
```bash
uv run pytest
```

## Status
Early stage. This is the first building block of a crop-price forecasting project.
