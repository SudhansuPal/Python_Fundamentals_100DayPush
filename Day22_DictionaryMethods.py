inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 8
}


print("Initial Inventory:")
for item, quantity in inventory.items():
    print(f"{item}: {quantity} in stock")

print("\nAdding new stock...")

inventory.update({"banana": inventory["banana"] + 3, "grape": 12})


print("\nChecking stock of mango (doesn't exist):")
print("Mango stock:", inventory.get("mango", 0))  # returns 0 if mango not found


print("\nBanana sold out. Removing it from inventory.")
inventory.pop("banana")

print("\nDo we have oranges?")
if "orange" in inventory:
    print("Yes, we have oranges.")

print("\nAvailable items:")
print("Items:", list(inventory.keys()))
print("Quantities:", list(inventory.values()))


print("\nUpdated Inventory:")
for item, quantity in inventory.items():
    print(f"{item}: {quantity} in stock")
