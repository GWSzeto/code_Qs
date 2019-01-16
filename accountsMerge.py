import collections

def accountsMerge(accounts):
    email_graph = collections.defaultdict(set)
    email_to_name = {}
    for account in accounts:
        name = account[0]
        for email in account[1:]:
            email_graph[account[1]].add(email)
            email_graph[email].add(account[1])
            email_to_name[email] = name

    seen = set()
    solution = []
    for email in email_graph:
        if email not in seen:
            seen.add(email)
            stack = [email]
            component = []
            while stack:
                node = stack.pop()
                component.append(node)
                for neighbour in email_graph[node]:
                    if neighbour not in seen:
                        seen.add(neighbour)
                        stack.append(neighbour)
            solution.append([email_to_name[email]] + sorted(component))

    return solution

print(accountsMerge([["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]))
