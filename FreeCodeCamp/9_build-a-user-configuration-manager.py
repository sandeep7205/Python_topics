# ** start of main.py **

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

# ** end of main.py **

