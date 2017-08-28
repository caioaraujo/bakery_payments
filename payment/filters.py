import coreapi
from rest_framework.filters import BaseFilterBackend


class PaymentFilterBackend(BaseFilterBackend):
    def get_schema_fields(self, view):
        return [coreapi.Field(
            name='expiration_date',
            required=False,
            type='date',
            description='Expiration date. Format yyyy-mm-dd'
        ),
            coreapi.Field(
                name='branch',
                required=False,
                type='integer',
                description='Branch ID'
            )
        ]