from behave import step


@step('User login with correct credentials')
def step_impl(context):
    context.login_page.login_to_app()
