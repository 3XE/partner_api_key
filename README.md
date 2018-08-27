# partner_api_key
Primitive Odoo module to add a field to the Partner model for use as an API key
in partner-facing middleware APIs.

## Security
Makes no assumptions about read/write permissions on field.

## Technical
`res.partner` model is extended by `ApiPartner` class to add `api_key` field.

## Demo
Demo data is empty but left there as a placeholder.
