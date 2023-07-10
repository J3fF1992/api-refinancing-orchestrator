from flask_restx import fields, Model


create_offers_model = Model(
    "Create-Offers",
    {
        "id": fields.String(
            description="Offer id",
            required=True,
            example="5071345b63ee4e358a39-27cce2d9c170"
        ),
        "user_uuid": fields.String(
            description="User id",
            required=True,
            example="77afba47e9784b839bfc42804cf5db95"
        ),
        "offered_at": fields.String(
            description="Offer date",
            required=True,
            example="2023-07-10"
        ),
        "expiration_at": fields.String(
            description="Offer expiration date",
            required=True,
            example="2023-07-11"
        ),
        "date_base_at": fields.String(
            description="Base date",
            required=True,
            example="2023-07-10"
        ),
        "iof_amount_cents": fields.Integer(
            description="IOF amount in cents",
            required=True,
            example=3814
        ),
        "cet_am": fields.Float(
            description="Tax cet am",
            required=True,
            example=5.7822506279127
        ),
        "cet_aa": fields.Float(
            description="Tax cet aa",
            required=True,
            example=98.1238172632
        ),
        "tax_am": fields.Float(
            description="Monthly interest rate",
            required=True,
            example=4.43227378462
        ),
        "tax_aa": fields.Float(
            description="Yearly interest rate",
            required=True,
            example=69.8796234963
        ),
        "grace_period": fields.Integer(
            description="Grace period",
            required=True,
            example=30
        ),
        "deposit_amount_cents": fields.Integer(
            description="Deposit amount in cents",
            required=True,
            example=1000000
        ),
        "installments": fields.Integer(
            description="Number of installments",
            required=True,
            example=12
        ),
        "monthly_amount_cents": fields.Integer(
            description="Monthly amount in cents",
            required=True,
            example=43567
        ),
        "refinanced_amount_cents": fields.Integer(
            description="Refinanced amount in cents",
            required=True,
            example=1200000
        ),
        "previous_contract_id": fields.String(
            description="Previous contract id",
            required=True,
            example="L09525188UI"
        ),
        "previous_partner_contract_id": fields.String(
            description="Previous partner contract id",
            required=True,
            example="123867123"
        ),
        "product_type": fields.String(
            description="Product type",
            required=True,
            enum=("REFIN",),
            example="REFIN"
        ),
        "previous_deposit_at": fields.String(
            description="Estimated deposit date",
            required=True,
            example="2023-07-14"
        ),
        "with_discount": fields.Boolean(
            description="If the offer has a discount",
            required=True,
            example=False
        ),
        "trigger_at": fields.Boolean(
            description="Date to send communication to the client",
            required=True,
            example="2023-7-10"
        )
    }
)


create_offers_response_model = Model(
    "Create-Offers-Response",
    {
        "id": fields.String(
            description="Offer id",
            required=True,
            example="5071345b63ee4e358a39-27cce2d9c170"
        )
    }
)
