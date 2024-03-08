if __name__ == "__main__":
    # Create an instance of the Local class
    local1 = Local(True, 1, "123 Main St")

    # Check if the local is available
    if local1.is_available():
        print(f"The local {local1.get_id()} at {local1.get_address()} is available.")
    else:
        print(f"The local {local1.get_id()} at {local1.get_address()} is not available.")

    # Set the local's availability to False
    local1.set_available(False)

    # Check again
    if local1.is_available():
        print(f"The local {local1.get_id()} at {local1.get_address()} is available.")
    else:
        print(f"The local {local1.get_id()} at {local1.get_address()} is not available.")