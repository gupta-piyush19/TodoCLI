from datetime import date
today = date.today()
RemTodo = open('todo.txt', 'r+')
CompTodo = open('done.txt', 'r+')


def showItems(args):
    RemTodo = open('todo.txt', 'r+')
    Todos = RemTodo.readlines()
    numTodo = len(Todos)
    cnt = numTodo
    for todo in Todos:
        if(todo != " "):
            print(f"[{cnt}] {todo[:-1]}")
            cnt -= 1


def addItem(args):
    RemTodo = open('todo.txt', 'r+')
    todoAdd = " ".join(args)
    content = RemTodo.read()
    RemTodo.seek(0, 0)
    RemTodo.write(todoAdd.rstrip('\r\n') + '\n' + content)
    print(f'Added todo: "{todoAdd}"')


def deleteItem(args):
    delTodo = int(args[0])

    RemTodo = open('todo.txt', 'r')
    Todos = RemTodo.readlines()
    numTodo = len(Todos)
    RemTodo.close()

    if delTodo > numTodo:
        print(delTodo - numTodo)
        print(f"Error: todo #{delTodo} does not exist.")
    else:
        RemTodo = open('todo.txt', 'w+')
        print(f"Deleted todo #{delTodo}")
        oppIdx = numTodo - delTodo
        Todos.pop(oppIdx)
        Todos = "".join(Todos)
        RemTodo.write(Todos)
        RemTodo.close()


def completeItem(args):
    print(args)


def stats(args):
    pending = len(RemTodo.readlines())
    completed = len(CompTodo.readlines())
    print(f"${today} Pending : {pending} Completed : {completed}")
