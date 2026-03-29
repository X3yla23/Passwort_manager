import os

# Colors for CMD
BLUE = '\033[94m'
CYAN = '\033[96m'
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'

# ASCII Logo
logo = """
****     ** **             **                           **      **** 
/**/**   /**//             //                           ***     *///**
/**//**  /** ** *******     **  ******         **    **//**    /*  */*
/** //** /**/**//**///**   /** //////**       /**   /** /**    /* * /*
/**  //**/**/** /**  /**   /**  *******       //** /**  /**    /**  /*
/**   //****/** /**  /** **/** **////**        //****   /**  **/*   /*
/**    //***/** ***  /**//*** //********        //**    ****//*/ **** 
//      /// // ///   //  ///   ////////          //    ////  /  ////             
"""

# Default folder to save passwords
VAULT_FOLDER = "NinjaVault"


def ensure_vault():
    """Create the vault folder if it does not exist"""
    if not os.path.exists(VAULT_FOLDER):
        os.makedirs(VAULT_FOLDER)
        print(GREEN + f"Vault folder '{VAULT_FOLDER}' created!" + RESET)


def print_header():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(BLUE + "*" * 70 + RESET)
    print(BLUE + logo + RESET)
    print(BLUE + "*" * 70 + RESET)
    print(BLUE + "Ninja v1.0".center(70) + RESET)
    print(BLUE + "Great by !Xyla".center(70) + RESET)
    print(BLUE + "*" * 70 + RESET)
    print()


def create_password_file():
    print(CYAN + "\n[ADD NEW PASSWORD]" + RESET)
    filename = input("Enter the file name to save passwords (without extension): ").strip() + ".txt"
    filepath = os.path.join(VAULT_FOLDER, filename)

    email = input("Enter your email: ").strip()
    password = input("Enter your password: ").strip()

    if not email or not password:
        print(RED + "Email and password cannot be empty!" + RESET)
        return

    with open(filepath, "a") as f:
        f.write(f"Email: {email}\nPassword: {password}\n---\n")

    print(GREEN + f"\nSaved successfully in '{filepath}'!" + RESET)
    print("-" * 70)


def view_passwords():
    print(CYAN + "\n[VIEW PASSWORDS]" + RESET)
    filename = input("Enter the file name to view passwords (without extension): ").strip() + ".txt"
    filepath = os.path.join(VAULT_FOLDER, filename)

    if not os.path.exists(filepath):
        print(RED + "File not found!" + RESET)
        return

    print(GREEN + f"\nPasswords stored in '{filepath}':" + RESET)
    print("-" * 70)
    with open(filepath, "r") as f:
        print(f.read())
    print("-" * 70)


def main():
    ensure_vault()
    print_header()

    while True:
        print(YELLOW + "[1]" + RESET + " Add new password")
        print(YELLOW + "[2]" + RESET + " View saved passwords")
        print(YELLOW + "[3]" + RESET + " Exit")
        choice = input("\nChoose an option: ").strip()
        if choice == "1":
            create_password_file()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            print(BLUE + "\nExiting Ninja... Stay stealthy!" + RESET)
            break
        else:
            print(RED + "\nInvalid option! Try again.\n" + RESET)


if __name__ == "__main__":
    main()
