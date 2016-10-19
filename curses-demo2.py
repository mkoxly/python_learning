#!/usr/bin/python
# coding:utf-8
import curses
stdscr = curses.initscr()
def test_move(stdscr):
  KEY_UP = 259
  KEY_DOWN = 258
  KEY_RIGHT = 261
  KEY_LEFT = 260  
  QUIT = ord('q')
  key_list=[ KEY_UP,KEY_DOWN,KEY_RIGHT,KEY_LEFT,QUIT ]
  y = 0
  x = 0
  while True:
    key = stdscr.getch()
    if (key == QUIT):
       break
    elif (key == KEY_UP):
       y = y - 1
    elif (key == KEY_DOWN):
       y = y + 1
    elif (key == KEY_RIGHT):
       x = x + 1
    elif (key == KEY_LEFT):
       x = x - 1
    else : continue
    if (x<0): x = x + 1
    if (y<0): y = x + 1
    stdscr.clear()
    stdscr.addstr(y,x,'@',curses.A_BLINK)  
          
       
  print 'test'
def test_getkey(stdscr):
  q = ord('q')
  action = 'a'
  while action != 'q' :
     asci = stdscr.getch()
     if (asci<255):
       action = chr(asci)
     else:
       action = 'ER'
     stdscr.addstr(action+':'+str(asci)+'\n') 
def main(stdscr):
  #test_getkey(stdscr)
  test_move(stdscr)
curses.wrapper(main)
