from flask_restx import fields, Model


index_model = Model(
    "Health-Status",
    {
        "service": fields.String(
            description="Service name"
        ),
        "version": fields.String(
            description="API version"
        )
    }
)
