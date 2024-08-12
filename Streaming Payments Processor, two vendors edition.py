# Define stream_payments first
def stream_payments(callback_fn):
    for i in range(10):
        callback_fn(i)


# Define store_payments
def store_payments(amount_iterator):
    for i in amount_iterator:
        print(i)


# Define process_payments_2
def process_payments_2():
    payments = []

    def payment_callback(amount):
        payments.append(amount)

    stream_payments(payment_callback)

    def payment_generator():
        for payment in payments:
            yield payment

    store_payments(payment_generator())


# Call the function to run the process
process_payments_2()