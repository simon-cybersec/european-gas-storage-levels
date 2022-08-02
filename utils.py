import colorama

def gaslevel_bar(percent):

    # Set color of bar
    if percent >= 90:
        color=colorama.Fore.GREEN
    elif percent <= 10:
        color=colorama.Fore.RED
    else:
        color=colorama.Fore.YELLOW
        
    # Calculate bar
    bar = '█' * int(percent/2) + '-' * (int(100/2) - int(percent/2))
    print(colorama.Fore.RESET + "|", end="")
    print(color + f"{bar}", end="")
    print(colorama.Fore.RESET + f"| {percent:.2f}%", end="\r")    
    print()
