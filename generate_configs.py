VLAN_MAP = {
    10: "ENGINEERING",
    20: "FINANCE",
    30: "HR_OPERATIONS",
    99: "NOC_MANAGEMENT"
}

def generate_vlan_cli():
    print("! Generated Cisco IOS VLAN Commands")
    for vid, name in VLAN_MAP.items():
        print(f"vlan {vid}")
        print(f" name {name}")
    print("!")

if __name__ == "__main__":
    generate_vlan_cli()
