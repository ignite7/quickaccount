"""
CLI
"""

from main import CreateRamdonAccount, CreateManuallyAccount

def create_option():
    """
    Introduction what the user wants.
    """
    
    print('Welcome, please select one option:')
    print('What do you want to do?')
    print(
        '1- Create random account\n'
        '2- Create manual account\n'
    )    
    
    option = input('Option: ')
    
    while option != '1' and option != '2':
        option = input('Select correct option: ')
                    
        if option == '1' or option == '2':
            return option
 
    return option


def service_option():
    pass

if __name__ == '__main__':
    selected_option = create_option()
    selected_service = service_option()
    
    if selected_option == '1':
        CreateRamdonAccount(selected_service)
        
    elif selected_option == '2':
        CreateManuallyAccount(selected_service)