import time 
from prob_functions import *
from help_functions import *

class Menus():
    def __init__(self):
         self.main_nodes = main_nodes
         self.route_length = 10

    def route_menu(self):
        while True:
            try:
                main_route = input('Please enter the route separated by comas or write "exit" to exit: ')
                if main_route.lower() == 'exit':
                     time.sleep(2)
                     help_functions.clear_screen()
                     break
                else:
                    route = main_route.split(",")
                    if len(route) >= self.route_length:
                         print(f'Error: Input lenght needs to be smaller than {self.route_length}')
                         time.sleep(2)
                         help_functions.clear_screen()
                    else:
                         int_nodes = []
                         for node in route:
                              node = node.strip()
                              if not node.isdigit():
                                   print('Error: Input contains non-numeric characters.')
                                   time.sleep(2)
                                   help_functions.clear_screen()
                                   return None  
                              node = int(node)                          
                              if not node in self.main_nodes:
                                   print('Error: There is one or more elements that are not on the main nodes.')
                                   time.sleep(2)
                                   help_functions.clear_screen()
                                   return None
                              int_nodes.append(node)
                         route = int_nodes
                         prob_functions.prob_calculator(route)
                         while True:
                                   add_option = input('Would you like to enter another node to the route? [Y/N]')
                                   if add_option.upper() == "Y":
                                        try:
                                             help_functions.clear_screen()
                                             new_node = int(input('Enter the new node: '))
                                             if new_node not in self.main_nodes:
                                                  print("The element is not on the main nodes.")
                                                  time.sleep(2)
                                                  help_functions.clear_screen()
                                                  break
                                             else:
                                                  route.append(new_node)
                                                  prob_functions.prob_calculator(route)
                                                  input("Press ENTER to return.")
                                                  help_functions.clear_screen()
                                        except:
                                             print('ERROR...')
                                   elif add_option.upper() == "N":
                                        help_functions.clear_screen()
                                        break
                                   else:
                                        print("Invalid option.")
            except:
                 print('ERROR...')
    

    def main_menu(self):
            while True:
                selected_option, exit_option = help_functions.menu("Main menu","Please select one of the following options", 1, ['Enter a route'])
                if selected_option == exit_option:
                     help_functions.clear_screen()
                     break
                elif selected_option == 1:
                     help_functions.clear_screen()
                     self.route_menu()
                else:
                     print("ERROR, invalid input...")
                     

if __name__ == "__main__":           
     menus = Menus()
     main_menu = menus.main_menu()
