import time
def final_message():
    print("""\
                     _             _           
                    (_)           (_)          
     _ __   __ _ _ __ _  __ _ _   _ _ _ __  ___ 
    | '_ \ / _` | '__| |/ _` | | | | | '_ \/ __|
    | | | | (_| | |  | | (_| | |_| | | | | \__ |
    |_| |_|\__,_|_|  |_|\__, |\__,_|_|_| |_|___/
                        __/ |                  
                        |___/                   
      __ _       _     _              _         
     / _(_)     (_)   | |            | |        
    | |_ _ _ __  _ ___| |__   ___  __| |        
    |  _| | '_ \| / __| '_ \ / _ \/ _` |        
    | | | | | | | \__ \ | | |  __/ (_| |        
    |_| |_|_| |_|_|___/_| |_|\___|\__,_|        
                                                
                                                
                                                                                    
                                                                                    """)


def wait_message(number_of_waits):
    for counter in range( 0, number_of_waits):
        print('...')
        time.sleep(1)