class PaymentNotFoundException(Exception):
    def __init__(self, message=None, errors=None):
        super(PaymentNotFoundException, self).__init__(message)
        self.errors = errors


class PaymentAlreadyPaidException(Exception):
    def __init__(self, message=None, errors=None):
        super(PaymentAlreadyPaidException, self).__init__(message)
        self.errors = errors