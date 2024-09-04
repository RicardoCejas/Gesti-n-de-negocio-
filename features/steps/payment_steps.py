from behave import given, when, then
from payment_system import PaymentSystem  # Importa tu clase PaymentSystem

# Inicializamos el sistema de pago
@given('the buyer is at the checkout page')
def step_impl(context):
    context.payment_system = PaymentSystem()

@when('the system shows the available payment methods')
def step_impl(context):
    context.available_methods = context.payment_system.show_payment_methods()

@then('the buyer should see a list of available payment methods')
def step_impl(context):
    assert context.available_methods == ["Credit Card", "Debit Card", "PayPal", "Bank Transfer"]

@when('the buyer selects "{method}" as the payment method')
def step_impl(context, method):
    context.selected_method = context.payment_system.select_payment_method(method)

@then('the system should confirm that "{method}" is selected')
def step_impl(context, method):
    assert context.selected_method == f"Payment method {method} selected."

@given('the buyer wants to save a payment method')
def step_impl(context):
    pass  # No hay acción adicional necesaria en este paso

@when('the buyer saves "{method}" as a payment method')
def step_impl(context, method):
    context.saved_method = context.payment_system.save_payment_method(method)

@then('the system should confirm that "{method}" is saved for future use')
def step_impl(context, method):
    assert context.saved_method == f"Payment method {method} saved."
    assert method in context.payment_system.get_saved_methods()

@when('the buyer selects an invalid payment method')
def step_impl(context):
    context.invalid_method = context.payment_system.select_payment_method("Invalid Method")

@then('the system should show an error message')
def step_impl(context):
    assert context.invalid_method == "Invalid payment method."

@given('the buyer has selected a valid payment method')
def step_impl(context):
    context.payment_system.select_payment_method("Credit Card")

@when('the buyer confirms the payment')
def step_impl(context):
    context.payment_confirmation = context.payment_system.confirm_payment()

@then('the system should confirm the payment and proceed with the purchase')
def step_impl(context):
    assert context.payment_confirmation == "Payment confirmed."
    assert context.payment_system.payment_confirmed is True
