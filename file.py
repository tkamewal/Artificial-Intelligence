def reverse_content(content):
    return content[::-1]

def main():
    try:
        user_input = input("Enter the content you want to save to a file: ")
        with open('input.txt', 'w') as file:
            file.write(user_input)
        print("Content saved to 'input.txt'.")

        with open('input.txt', 'r') as file:
            content = file.read()
            reversed_content = reverse_content(content)

        with open('output.txt', 'w') as file:
            file.write(reversed_content)
        print(f"Reversed content saved to 'output.txt'.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
