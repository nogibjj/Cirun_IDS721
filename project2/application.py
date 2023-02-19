from flask import Flask

application = Flask(__name__)


@application.route("/")
def hello_world():
    return "hello world from docker!"


@application.route("/cal/<formula_str>")
def calculator(formula_str: str):
    PLUS = "+"
    MINUS = "-"
    TIMES = "*"
    DIVIDE = "|"
    stack = []

    prevOperator = PLUS
    i = 0
    while i < len(formula_str):
        if formula_str[i] == " ":
            i += 1
            continue
        if not formula_str[i].isdigit():
            prevOperator = formula_str[i]
            i += 1
        else:
            num = 0
            while i < len(formula_str) and formula_str[i].isdigit():
                num *= 10
                num += (int)(formula_str[i])
                i += 1
            if prevOperator == PLUS:
                stack.append(num)
            if prevOperator == MINUS:
                stack.append(-num)
            if prevOperator == TIMES:
                stack.append(num * stack.pop())
            if prevOperator == DIVIDE:
                stack.append(stack.pop() / num)

    ans = 0
    while len(stack) > 0:
        ans += stack.pop()
    word = "<h1><center>Solving " + formula_str + "\n\n</center></h1>"
    word += "<h1><center>answer: " + str(ans) + "</center></h1>"
    return word


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=3000)
    # print(calculator('3+2*6'))
    # print(calculator('3+2*6/2-1'))
