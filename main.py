#Installed in linux but for win and macOS specififyhow to install it
import curses
from curses import wrapper

def main(stdscr):
    #Helps us get colors for the txt in terminal
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    #clears the terminal before exec
    stdscr.clear()
    #The int before the str is the co-ordinate of where the text will be placed
    stdscr.addstr(1 , 0 ,"Hello World")
    stdscr.refresh()
    #Waits for input
    stdscr.getkey()

wrapper(main)   
