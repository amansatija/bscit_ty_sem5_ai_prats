print("Ahmed Shaikh 323")
def tower_of_hanoi(n, left, middle, right):
    print(f"called tower_of_hanoi({n},:  {left}, : {middle},:  {right})")
    if n == 1:
        print(f"Move disk 1 from {left} to {right}")#this is the actual move 
        return
    source = left
    target = middle
    tempstorage = right

    print(f"before Moving total disks {n-1} from {source} to {target} using {tempstorage}")
    tower_of_hanoi(n - 1, source, tempstorage, target)
    print(f"after Moving disk {n-1} from {source} to {target} using {tempstorage}")

    print(f"Move disk {n} from {left} to {right} ... note this is the actul move not just he print statement ....")# this too is the actual move ...!!!

    source = middle
    target = right
    tempstorage = left
    print(f"before Moving disk {n-1} from {source} to {target} using {tempstorage}")
    tower_of_hanoi(n - 1, source, tempstorage, target)
    print(f"after Moving disk {n-1} from {source} to {target} using {tempstorage}")
# Number of disks
n = 3

# Names of the pegs
left = 'A'
middle = 'B'
right = 'C'

# Call the function
tower_of_hanoi(n, left, middle, right)