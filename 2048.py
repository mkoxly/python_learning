#!/usr/bin/python
# coding:utf-8
import curses
import sys
from random import choice,randrange
scr = curses.initscr()
def main(scr):
  global data
  data=[[0 for i in range(4)] for i in range(4)]
  step = [1]
  win = [2048]
  #######tool##################
  def row_move_left(row):
    #temp =[ int(j) for j in  ' '.join([str(i) for i in row]).replace('0','').split() ]
    temp = [ row[i] for i in range(len(row)) if row[i]!=0 ]
    l = len(temp)
    if (l>1):  
       i = 0
       while (i< (l-1)):
         if (temp[i] == temp[i+1]):
           temp[i+1]=temp[i+1]*2
           temp[i]=0
           i+=2
         else : i+=1 
    temp = [ temp[i] for i in range(len(temp)) if temp[i]!=0 ] 
    if (len(temp)<4):
      for i in range(4-len(temp)):
        temp.append(0)
    return temp
  def row_move_right(row):
    a=row
    a.reverse()
    b=row_move_left(a)
    b.reverse()
    return b
  def array_rotate_left(arr):
    return  [[ arr[i][j] for i in range(len(arr)) ] for j in range(len(arr[0])-1,-1,-1) ]
  def array_rotate_right(arr):
   return  [[ arr[i][j] for i in range(len(arr)-1,-1,-1)] for j in range(len(arr[0])) ] 
  def array_move_left(arr):
    return [ row_move_left(arr[i]) for i in range(len(arr))]
  def array_move_right(arr):
    return [ row_move_right(arr[i]) for i in range(len(arr))]
  def array_move_up(arr):
    return  array_rotate_right(array_move_left(array_rotate_left(arr)))
  def array_move_down(arr):
    temp = array_rotate_right(arr)
    temp = array_move_left(temp)
    temp = array_rotate_left(temp)
    return temp  
  #############tool############
  def check_win():
   return any(any(i>=win[0] for i in row) for row in data)
  def move_up():
    global data
    step[0] += 1 
    data = array_move_up(data)
  def move_down():
    global data
    step[0] += 1 
    data = array_move_down(data)
  def move_right():
    global data
    step[0] += 1 
    data = array_move_right(data)
  def move_left():
    global data
    step[0] += 1
    data = array_move_left(data)	
  def reset():
    global data
    data=[[0 for i in range(4)] for i in range(4)]
    step[0] = 1
  def exit_game():
    sys.exit(0)
  def gen_2():
    try: 
      (i,j)=choice([(i,j) for i in range(4) for j in range(4) if data[i][j]==0])
      data[i][j] = 2 if randrange(100)<85 else 4 
    except  IndexError:
      pass
  def repaint():
    scr.clear()
    gen_2()
    x=8
    y=8
    scr.addstr(y,x,' '*10+'2 0 4 8'+' '*10+'\n')
    scr.addstr(y+1,x,('+'+'-'*7)*4+'+\n')
    scr.addstr(y+2,x,''.join([ '| '+'{:5d} '.format(i) if i>0 else '|       ' for i in data[0] ])+'|\n')
    scr.addstr(y+3,x,('+'+'-'*7)*4+'+\n')
    scr.addstr(y+4,x,''.join([ '| '+'{:5d} '.format(i) if i>0 else '|       ' for i in data[1] ])+'|\n')
    scr.addstr(y+5,x,('+'+'-'*7)*4+'+\n')
    scr.addstr(y+6,x,''.join([ '| '+'{:5d} '.format(i) if i>0 else '|       ' for i in data[2] ])+'|\n')
    scr.addstr(y+7,x,('+'+'-'*7)*4+'+\n')
    scr.addstr(y+8,x,''.join([ '| '+'{:5d} '.format(i) if i>0 else '|       ' for i in data[3] ])+'|\n')
    scr.addstr(y+9,x,('+'+'-'*7)*4+'+\n')
    scr.addstr(y+10,x,'UP,DOWN,RIGHT,LEFT,Reset(r),Quit(q) Step:'+str(step[0])+'\n')	 
  repaint()
  while not check_win():
    key = scr.getch()
    if (key == curses.KEY_UP):
       move_up()
    elif (key == curses.KEY_DOWN):
       move_down()
    elif (key == curses.KEY_RIGHT):
       move_right()
    elif (key == curses.KEY_LEFT):
       move_left()
    elif (key == ord('q')):
       exit_game()
    elif (key == ord('r')):
       reset()
    repaint()
  scr.clear()
  scr.addstr(10,5,"You are WINNER!!")
  scr.getch()
curses.wrapper(main)

