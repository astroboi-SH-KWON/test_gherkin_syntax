from behave import given, when, then


@given('사용자가 로그인 페이지에 있다')
def step_impl(context):
    print("[ACTION] Search login page")


@when('사용자가 유효한 이메일 "{email}"을 입력한다')
def step_impl(context, email):
    print(f"[INPUT] email : {email}")


@when('사용자가 유효한 ID "{user_id}"를 입력한다')
def step_impl(context, user_id):
    print(f"[INPUT] user_id : {user_id}")


@when('사용자가 유효한 비밀번호 "{pw}"을 입력한다')
def step_impl(context, pw):
    print(f"[INPUT] password : {pw}")


@when('사용자가 유효하지 않은 이메일 "{email}"을 입력한다')
def step_impl(context, email):
    print(f"[INPUT] email : {email}")


@when('사용자가 유효하지 않은 비밀번호 "{pw}"을 입력한다')
def step_impl(context, pw):
    print(f"[INPUT] password : {pw}")


@when('사용자가 로그인 버튼을 클릭한다')
def step_impl(context):
    print(f"[ACTION] Click login button")


@then('사용자는 홈페이지로 리다이렉트된다')
def step_impl(context):
    print(f"[RESPONSE] Redirect to Home")


@then('사용자는 로그인 상태를 확인할 수 있다')
def step_impl(context):
    print(f"[RESPONSE] USER's personal page")


@then('사용자는 로그인 페이지에 그대로 있다')
def step_impl(context):
    print(f"[RESPONSE] Stay in Login page")


@then('사용자는 에러 메시지를 볼 수 있다')
def step_impl(context):
    print(f"[RESPONSE] ERROR POP-UP")