def isBalanced(str):
    all_parentesis = [ p for p in str if p == "(" or p == ")"]
    s = ''
    s = s.join(all_parentesis)
    if s == "()()" or s == "(())":
        return True
    else:
        return False

if __name__ == "__main__": # entry point o punto de entrada ---> inicia la función cuando ejecutamos el archivo
    isBalanced( "(aaa)(b)")

