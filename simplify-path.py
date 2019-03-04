def simplifyPath(path):
    path_list = [dir for dir in path.split("/") if dir != "" and dir != "."]
    path_stack = []
    for dir in path_list:
        if dir == "..":
            path_stack:
            path_stack.pop()
        else:
            path_stack.append(dir)

    return "/" + "/".join(path_stack)

print(simplifyPath("/a//b////c/d//././/.."))
