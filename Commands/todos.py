def showItems(args):
    cnt = 0
    help_file = open('todo.txt', 'r+')
    todo = help_file.readlines()
    numTodo = len(todo)
    print(numTodo)
    for i in range(numTodo):
        todo[i]

def addItem(args):
    RemTodo = open('todo.txt', 'a+')
    todoAdd = " ".join(args)
    RemTodo.write(todoAdd)
    RemTodo.write('\n')
    print('Added todo: "', todoAdd, '"')

def deleteItem(args):
    int(args[0])


def completeItem(args):
    print(args)


def usage(args):
    print(args)


def stats(args):
    print(args)
