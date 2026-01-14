def tower_of_hanoi(n, source, target, auxiliary_towers):
    global count
    if n == 0:
        return
    if len(auxiliary_towers) == 0:
        count += 1
        print(f"Move disk {n} from {source} to {target}")
        return
    temp_target = auxiliary_towers[0]
    remaining_auxiliary = auxiliary_towers[1:]
    tower_of_hanoi(n - 1, source, temp_target, remaining_auxiliary + [target])
    count += 1
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, temp_target, target, remaining_auxiliary + [source])
    
if __name__ == "__main__":
    num_disks = int(input("Enter the number of disks: "))
    num_towers = int(input("Enter the number of towers (minimum 3): "))

    towers = [chr(65 + i) for i in range(num_towers)]
    source_tower = towers[0]
    target_tower = towers[1]
    auxiliary_towers = towers[2:]
    count = 0
    tower_of_hanoi(num_disks, source_tower, target_tower, auxiliary_towers)
    print(f"\nTotal number of moves: {count}")
