import csv 
import os

csvFilename = 'data_contact.csv'

def clear_screen():
    """Clear the terminal screen dynamically based on the OS ['Windows', 'Linux', or 'Darwin(mac)']"""
    os.system('cls' if os.name == 'nt' else 'clear')
def show_menu():
    clear_screen()
    print("=== Data Contact ===")
    print("[1] View Contact")
    print("[2] Create Contact")
    print("[3] Edit Contact")
    print("[4] Delete Contact")
    print("[5] Search Contact")
    print("[0] Exit")
    print("===================")
    selected_menu = input("Menu No => ")

    if (selected_menu == '1'):
        show_contact()
    if (selected_menu == '2'):
        create_contact()
    if (selected_menu == '3'):
        edit_contact()
    if (selected_menu == '4'):
        delete_contact()
    if (selected_menu == '5'):
        search_contact()
    if (selected_menu == '0'):
        exit()
    else:
        print("Menu is Wrong!!!")
        back_to_menu()

    