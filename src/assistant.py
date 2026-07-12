from router import execute_command

while True:

    question = input("Ask: ")

    if question.lower() == "exit":
        break

    result = execute_command(question)

    print(result)

    