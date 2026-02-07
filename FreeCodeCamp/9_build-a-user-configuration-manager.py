# ============================================================
# Build a User Configuration Manager
# ============================================================
#
# In this lab, you will build a User Configuration Manager that
# allows users to manage their settings such as theme, language,
# and notifications.
#
# You will implement functions to add, update, delete, and view
# user settings.
#
# ------------------------------------------------------------
# Objective
# ------------------------------------------------------------
# Fulfill the user stories below and get all the tests to pass
# to complete the lab.
#
# ------------------------------------------------------------
# User Stories
# ------------------------------------------------------------
#
# ------------------------------------------------------------
# add_setting Function
# ------------------------------------------------------------
#
# - You should define a function named add_setting with two
#   parameters representing:
#       - a dictionary of settings
#       - a tuple containing a key-value pair
#
# add_setting function should:
#
# - Convert the key and value to lowercase.
#
# - If the key setting exists, return:
#       Setting '[key]' already exists! Cannot add a new setting
#       with this name.
#
# - If the key setting doesn't exist:
#       - add the key-value pair to the given dictionary of
#         settings
#       - return:
#         Setting '[key]' added with value '[value]' successfully!
#
# - The messages returned should have the key and value in
#   lowercase.
#
# ------------------------------------------------------------
# update_setting Function
# ------------------------------------------------------------
#
# - You should define a function named update_setting with two
#   parameters representing:
#       - a dictionary of settings
#       - a tuple containing a key-value pair
#
# update_setting function should:
#
# - Convert the key and value to lowercase.
#
# - If the key setting exists:
#       - update its value in the given dictionary of settings
#       - return:
#         Setting '[key]' updated to '[value]' successfully!
#
# - If the key setting doesn't exist, return:
#       Setting '[key]' does not exist! Cannot update a
#       non-existing setting.
#
# - The messages returned should have the key and value in
#   lowercase.
#
# ------------------------------------------------------------
# delete_setting Function
# ------------------------------------------------------------
#
# - You should define a function named delete_setting with two
#   parameters representing:
#       - a dictionary of settings
#       - a key
#
# delete_setting function should:
#
# - Convert the key passed to lowercase.
#
# - If the key setting exists:
#       - remove the key-value pair from the given dictionary
#         of settings
#       - return:
#         Setting '[key]' deleted successfully!
#
# - If the key setting does not exist, return:
#       Setting not found!
#
# - The messages returned should have the key in lowercase.
#
# ------------------------------------------------------------
# view_settings Function
# ------------------------------------------------------------
#
# - You should define a function named view_settings with one
#   parameter representing a dictionary of settings.
#
# view_settings function should:
#
# - Return:
#       No settings available.
#   if the given dictionary of settings is empty.
#
# - If the dictionary contains any settings:
#       - return a string displaying the settings
#       - the string should start with:
#         Current User Settings:
#       - followed by key-value pairs, each on a new line
#       - the key should be capitalized
#
# Example:
#
# view_settings({
#     'theme': 'dark',
#     'notifications': 'enabled',
#     'volume': 'high'
# })
#
# should return:
#
# Current User Settings:
# Theme: dark
# Notifications: enabled
# Volume: high
#
# ------------------------------------------------------------
# Testing Setup
# ------------------------------------------------------------
#
# - For testing the code, you should create a dictionary named
#   test_settings to store some user configuration preferences.
#
# ------------------------------------------------------------
# Tests
# ------------------------------------------------------------
#
# Waiting: 1. You should create a dictionary named test_settings
#             and add some values to it.
#
# Waiting: 2. You should define a function named add_setting.
#
# Waiting: 3. The add_setting function should have two
#             parameters.
#
# Waiting: 4. add_setting should convert the key to lowercase.
#
# Waiting: 5. add_setting should convert the value to lowercase.
#
# Waiting: 6. add_setting({'theme': 'light'}, ('THEME', 'dark'))
#             should return the error message:
#             Setting 'theme' already exists! Cannot add a new
#             setting with this name.
#
# Waiting: 7. add_setting({'theme': 'light'}, ('volume', 'high'))
#             should add a new key-value pair and return the
#             success message:
#             Setting 'volume' added with value 'high'
#             successfully!.
#
# Waiting: 8. add_setting should correctly add the given
#             key-value pair to the dictionary.
#
# Waiting: 9. You should define a function named update_setting.
#
# Waiting: 10. The update_setting function should have two
#              parameters.
#
# Waiting: 11. The update_setting function should convert key
#              to lowercase.
#
# Waiting: 12. The update_setting function should convert value
#              to lowercase.
#
# Waiting: 13. update_setting({'theme': 'light'}, ('theme',
#              'dark')) should update an existing key and return
#              the success message:
#              Setting 'theme' updated to 'dark' successfully!.
#
# Waiting: 14. update_setting({'theme': 'light'}, ('volume',
#              'high')) should return the error message:
#              Setting 'volume' does not exist! Cannot update a
#              non-existing setting.
#
# Waiting: 15. update_setting should correctly update the given
#              key-value pair in the dictionary.
#
# Waiting: 16. You should define a function named delete_setting.
#
# Waiting: 17. The delete_setting function should have two
#              parameters.
#
# Waiting: 18. delete_setting should convert the key to
#              lowercase.
#
# Waiting: 19. delete_setting({'theme': 'light'}, 'theme')
#              should remove the existing key and return the
#              success message:
#              Setting 'theme' deleted successfully!.
#
# Waiting: 20. delete_setting should return the error message:
#              Setting not found!
#              when the key doesn't exist.
#
# Waiting: 21. delete_setting should correctly remove the given
#              key from the dictionary.
#
# Waiting: 22. You should define a function named view_settings.
#
# Waiting: 23. The view_settings function should have one
#              parameter.
#
# Waiting: 24. view_settings should return the message:
#              No settings available.
#              if the given dictionary is empty.
#
# Waiting: 25. view_settings should return formatted settings
#              for non-empty dictionary.
#
# Waiting: 26. view_settings should capitalize the first letter
#              of each setting name.
#
# Waiting: 27. view_settings should display the correct results
#              and end with a newline character.
#
# ============================================================

test_settings = {
'theme': 'dark',
'notifications': 'enabled',
}

def view_settings(test_settings):
    if len(test_settings) <= 0:
        return "No settings available."
    else:
        view_user_settings = "Current User Settings:\n"
        for key, value in test_settings.items():
            view_user_settings += f"{key.title()}: {value}\n"
        return view_user_settings 

print(view_settings(test_settings))


add_new_settings = ('Volume', 'high')

def add_setting(test_settings, add_new_settings):
    key = add_new_settings[0].lower()
    value = add_new_settings[1].lower()

    if key in test_settings.keys():
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    test_settings[key] = value
    
    return f"Setting '{key}' added with value '{value}' successfully!"

print(add_setting(test_settings, add_new_settings))
print(view_settings(test_settings))

update_exists_settings = ('theme', 'Light')
def update_setting(test_settings, update_exists_settings):
    key = update_exists_settings[0].lower()
    value = update_exists_settings[1].lower()

    if key in test_settings.keys():
        test_settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

print(update_setting(test_settings, update_exists_settings))
print(view_settings(test_settings))

delete_exists_settings = 'theme'
def delete_setting (test_settings, delete_exists_settings):
    key = delete_exists_settings.lower()

    if key in test_settings.keys():
        del test_settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting not found!"
    
print(delete_setting (test_settings, delete_exists_settings))
print(view_settings(test_settings))


