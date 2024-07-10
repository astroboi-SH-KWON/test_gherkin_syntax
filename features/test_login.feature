# # behave -f plain --no-capture features/test_login.feature

Feature: 사용자 로그인

   Scenario: 유효한 자격 증명으로 로그인
     Given 사용자가 로그인 페이지에 있다
     When 사용자가 유효한 이메일 "onyuser@example.com"을 입력한다
     And 사용자가 유효한 비밀번호 "password123"을 입력한다
     And 사용자가 로그인 버튼을 클릭한다
     Then 사용자는 홈페이지로 리다이렉트된다
     And 사용자는 로그인 상태를 확인할 수 있다

   Scenario: 유효하지 않은 자격 증명으로 로그인
     Given 사용자가 로그인 페이지에 있다
     When 사용자가 유효하지 않은 이메일 "invalid@example.com"을 입력한다
     And 사용자가 유효하지 않은 비밀번호 "wrongpassword"을 입력한다
     And 사용자가 로그인 버튼을 클릭한다
     Then 사용자는 로그인 페이지에 그대로 있다
     And 사용자는 에러 메시지를 볼 수 있다