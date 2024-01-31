from sys import stdin

lines = stdin.read().splitlines()

projects = {}


def checkValues(projects):
    seen = set()
    remove = set()

    for project, user_ids in projects.items():
        updated_user_ids = []
        seen_in_project = set()  

        for user_id in user_ids:
            if user_id not in seen:
                seen.add(user_id)
                updated_user_ids.append(user_id)
            elif user_id not in seen_in_project:
                seen_in_project.add(user_id)
                updated_user_ids.append(user_id)
                remove.add(user_id)

        projects[project] = updated_user_ids

    for project, user_ids in projects.items():
        updated_user_ids = [user_id for user_id in user_ids if user_id not in remove]
        projects[project] = updated_user_ids

    return projects





def process_lines(i):
    global projects

    while i < len(lines):
        line = lines[i]
        i += 1

        if line.isupper():  # Project
            project = line
            projects[project] = [] 

            while i < len(lines) and not lines[i].isupper():
                to_check = lines[i]

                
                if to_check[0].islower():
                    projects[project].append(to_check)

                i += 1

    
    projects = checkValues(projects)
    printP(projects)

    return i

def printP(projects):
    sorted_projects = sorted(projects.items(), key=lambda x: (-len(x[1]), x[0]))

    for project, user_ids in sorted_projects:
        print(f'{project} {len(user_ids)}')

index = 0
while index < len(lines):
    index = process_lines(index)
    if index < len(lines) and lines[index] == '0':
        break
