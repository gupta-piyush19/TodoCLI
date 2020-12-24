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
            print("[", cnt, "]", todo[:-1])
            cnt -= 1


def addItem(args):
    RemTodo = open('todo.txt', 'r+')
    todoAdd = " ".join(args)
    content = RemTodo.read()
    RemTodo.seek(0, 0)
    RemTodo.write(todoAdd.rstrip('\r\n') + '\n' + content)
    print('Added todo: "', todoAdd, '"')


def deleteItem(args):
    int(args[0])


def completeItem(args):
    print(args)


def stats(args):
    pending = len(RemTodo.readlines())
    completed = len(CompTodo.readlines())
    print(today, "Pending :", pending, "Completed :", completed)
