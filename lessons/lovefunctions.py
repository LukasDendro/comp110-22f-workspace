"""Some tender, loving functions"""
def love(subject: str) -> str:
    return f"I love you {subject} !"

ur_name: str = input("What is your name? ")
print(love(ur_name))  