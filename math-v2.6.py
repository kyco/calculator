# -*- coding: utf-8 -*-
#Maths
import math
import sys

#Financial Maths
i = 0.00
def compound_interest():
  print ' '
  P = input('  The starting value: ')
  i = input('  Interest rate:      ')
  r = input('  Compounded:         1: Monthly\n                      2: Yearly\n                   => ')  
  if r in (1,2):
    n = input('  Number of years:    ')
    if i >= 1:
      i = i/100.00
    if r == 1:
      i = i/12.00
      n = n*12
      return P*(1+i)**n
    elif r == 2:
      return P*(1+i)**n
  else:
    print'\n  [E]\n  Please insert 1 or 2'
    return
  

def simple_interest():
        print ' '
        P = input('  The starting value: ')
        i = input('  Interest rate:      ')
        n = input('  Number of years:    ')
        if i >= 1:
                i = i/100.00
        return P*(1+n*i)

def future_value():
        print ' '
        x = input('  Payment per period: ')
        n = input('  Number of payments: ')
        i = input('  Interest rate:      ')
        if i >= 1:
                i = i/100.00
        return x*(((1+i)**n)-1)/i

def present_value():
        print ' '
        x = input('  Payment per period: ')
        n = input('  Number of payments: ')
        i = input('  Interest rate:      ')
        if i >= 1:
                i = i/100.00
        return x*(1-((1+i)**-n))/i

#Financial Maths Menu
def Financial_Maths_Menu():
  options =  '''
  -----------------------------------
  1: Financial Maths
  -----------------------------------
  1: Calculate amount as per compound interest
  2: Calculate amount as per simple interest
  3: Calculate future values
  4: Calculate present value
  0: Return to main menu
  -----------------------------------'''
  while True:
    print options
    try:
      command = raw_input('\n  Please select an option: ')
    except (IOError, KeyboardInterrupt):
      print '\n  [E] Going back to main menu...'
      return
    try:
      if command in '12340':
        if command == '1':
          print '\n  Result: %0.2f' %  compound_interest(),raw_input('    Continue?'),
        if command == '2':
          print '\n  Result: %0.2f' % simple_interest(),raw_input('    Continue?'),
        if command == '3':
          print '\n  Result: %0.2f' % future_value(),raw_input('    Continue?'),
        if command == '4':
          print '\n  Result: %0.2f' % present_value(),raw_input('    Continue?'),
        if command == '0':
          print '\n  [*] Returning to main menu...'
          return
      else:
        print '\n  [-] Invalid option'
    except:
      print '\n  [-] Invalid option'

#Trigonometry
def trig():
  options = '''
  -----------------------------------
              Trigonometry
  -----------------------------------
  1: Sine                   [radians]
  2: Cosine                 [radians]
  3: Tangent                [radians]
  4: Arcsine                [radians]
  5: Arccosine              [radians]
  6: Arctangent             [radians]
  7: Hyberbolic of sine     [radians]
  8: Hyperbolic of cosine   [radians]
  9: Hyberbolic of tangent  [radians]
  0: Return to main menu    [radians]
  -----------------------------------'''
  while True:
    print options
    try:
      command = raw_input('\n  Please select an option: ').strip()
    except (IOError, KeyboardInterrupt):
      print '\n  [E] Going back to menu'
      return
    if command in '1234567890':
      if command == '1':
        a = input('\n  Angle: ')
        print '\n  Result: '+str(math.sin(a)),raw_input('    Continue?'),
      if command == '2':
        a = input('\n  Angle: ')
        print '\n  Result: '+str(math.cos(a)),raw_input('    Continue?'),
      if command == '3':
        a = input('\n  Angle: ')
        print '\n  Result: '+str(math.tan(a)),raw_input('    Continue?'),
      if command == '4':
        a = input('\n  Inverse of sin: ')
        print '\n  Result: '+str(math.asin(a)),raw_input('    Continue?'),
      if command == '5':
        a = input('\n  Inverse of cos: ')
        print '\n  Result: '+str(math.acos(a)),raw_input('    Continue?'),
      if command == '6':
        a = input('\n  Inverse of tan: ')
        print '\n  Result: '+str(math.atan(a)),raw_input('    Continue?'),
      if command == '7':
        a = input('\n  Enter: ')
        print '\n  Result: '+str(math.sinh(a)),raw_input('    Continue?'),
      if command == '8':
        a = input('\n  Angle: ')
        print '\n  Result: '+str(math.cosh(a)),raw_input('    Continue?'),
      if command == '9':
        a = input('\n  Angle: ')
        print '\n  Result: '+str(math.tanh(a)),raw_input('    Continue?'),
      if command == '0':
        print '\n [*] Returning to main menu...'
        return
    else:
      print '\n [-] Invalid command'

#Trig Identities
def sinp():
  a = input('\n  Please enter the alpha value: ')
  b = input('\n  Please enter the beta value: ')
  print ' '
  r = (math.sin(math.degrees(a))*math.cos(math.degrees(b)))+(math.cos(math.degrees(a))*math.sin(math.degrees(b)))
  c = raw_input('\n  sin('+`a`+')cos('+`b`+')'+'+'+'cos('+`a`+')sin('+`b`+')'+'\n'+`r`+'\n  Is this correct (y/n): ')
  if c == 'n':
    print '\n  [-] Please try again...'
    sinp()
  print r

def sinm():
  a = input('\nPlease enter the alpha value: ')
  b = input('\nPlease enter the beta value: ')
  print ' '
  r = (math.sin(math.degrees(a))*math.cos(math.degrees(b)))-(math.cos(math.degrees(a))*math.sin(math.degrees(b)))
  c = raw_input('\nsin('+`a`+')cos('+`b`+')'+'-'+'cos('+`a`+')sin('+`b`+')'+'\n'+'\nIs this correct (y/n): ')
  if c == 'n':
    print '\n[-] Please try again...'
    sinm()
  print r

def cosp():
  a = input('\nPlease enter the alpha value: ')
  b = input('\nPlease enter the beta value: ')
  print ' '
  r = (math.cos(math.degrees(a))*math.cos(math.degrees(b)))-(math.sin(math.degrees(a))*math.sin(math.degrees(b)))
  c = raw_input('\ncos('+`a`+')cos('+`b`+')'+'-'+'sin('+`a`+')sin('+`b`+')'+'\n'+'\nIs this correct (y/n): ')
  if c == 'n':
    print '\n[-] Please try again...'
    cosp()
  print r

def cosm():
  a = input('\nPlease enter the alpha value: ')
  b = input('\nPlease enter the beta value: ')
  print ' '
  r = (math.cos(math.degrees(a))*math.cos(math.degrees(b)))+(math.sin(math.degrees(a))*math.sin(math.degrees(b)))
  c = raw_input('\ncos('+`a`+')cos('+`b`+')'+'+'+'sin('+`a`+')sin('+`b`+')'+'\n'+'\nIs this correct (y/n): ')
  if c == 'n':
    print '\n[-] Please try again...'
    sinm()
  print r

def sin2a():
  a = input('\nPlease enter the alpha value: ')
  print ' '
  r = 2*(math.sin(math.degrees(a)))*(math.cos(math.degrees(a)))
  c = raw_input('\n2sin('+`a`+')cos('+`a`+')'+'\n'+'\nIs this correct (y/n): ')
  if c == 'n':
    print '\n[-] Please try again...'
  print r

def cosinesine():
  a = input('\nPlease enter the alpha value: ')
  formula = (math.sqrt(math.cos(math.degrees(a))))-(math.sqrt(math.sin(math.degrees(a))))
  output = '\ncos**2('+`a`+')-'+'sin**2('+`a`+')'
  print output
  print ' '
  correction = raw_input('\nIs this correct (y/n): ')
  if correction == 'n':
    print '\n[-] Try again...'
    cosinesine()
  print formula

def cossquared():
  a = input('\nPlease enter the alpha value: ')
  formula = 2*(math.sqrt(math.cos(math.degrees(a))))-1
  output = '\n2cos**2('+`a`+')-1'
  print output
  print ' '
  correction = raw_input('\nIs this correct (y/n): ')
  if correction == 'n':
    print '\n[-] Try again...'
    print cossquared()
  print formula

def sinesquared():
        a = input('\nPlease enter the alpha value: ')
        forumla = 1-2*(math.sqrt(math.sin(math.degrees(a))))
        output = '\n1-2sin**2('+`a`+')'
        print output
        print ' '
        correction = raw_input('\nIs this correct (y/n): ')
        if correction == 'n':
	  print '\n[-] Try again...'
	  print sinesquared()
	print forumla

def cos2a_options():
  options = '''
  
  1: cos**2(x)-sin**2(x)
  2: 2cos**2(x)-1
  3: 1-2sin**2(x)
  
  '''
  return options

def cos2a():
  print cos2a_options()
  while True:
    try:
      command = raw_input('\nWhat would you like to use? ').strip()
    except (IOError, KeyboardInterrupt):
      print '\nReturning to main menu...'
      return
      
    if command == '1':
      cosinesine()
    if command == '2':
      cossquared()
    if command == '3':
      sinesquared()
    else:
      print '[-] Invalid command...'
      cos2a()

def trig_ident_menu():
  options = '''
  -----------------------------------
        Trigonometry Identities
  -----------------------------------
  1: sin(a+b)
  2: sin(a-b)
  3: cos(a+b)
  4: cos(a-b)
  5: sin2a
  6: cos2a
  0: Return to main menu
  -----------------------------------
  '''
  while True:
    print options
    try:
      command = raw_input('  What would you like to do? ')
    except (IOError, KeyboardInterrupt):
        print '\n  [*] Returning to main menu...'
        return 
    if command in'1234567890':
      if command == '1':
        sinp()
      if command == '2':
        sinm()
      if command == '3':
        cosp()
      if command == '4':
        cosm()
      if command == '5':
        sin2a()
      if command == '6':
       cos2a()
      if command == '0':
        print '\n  [*] Returning to main menu...'
        return
    else:
      return

#Introduction
def intro():
  return('''
  ###################################
  #                                 #
  #  Welcome to this maths program  #
  #   Please select an option to    #
  #            continue             #
  #                                 #
  #  Author:    Kyluke(FNB)         #
  #  Edited by: BigSlimDave         #
  #                                 #
  ###################################''')
 
def rules():
  return ('''
  -----------------------------------
                Main Menu
  -----------------------------------
  1: Financial Maths
  2: Trigonometry
  3: Trigonometry Identities
  9: Display options
  0: Exit Program
  -----------------------------------''')
  

# Main Menu
def main():
  while True:
    print rules()
    try:
      command = raw_input('\n  What would you like to do? ').strip()
    except (IOError, KeyboardInterrupt):
      print '\n  [*] Cheers Bro'
      sys.exit()
      
    if command in '12390':
      if command == '1':
        Financial_Maths_Menu()
      if command == '2':
        trig()
      if command == '3':
        trig_ident_menu()
      if command == '9':
        print rules()
      if command == '0':
        print '\n [+] Thanks for using this software...'
        sys.exit()
    else:
      print '\n  [-] Invalid option'

print intro()
main()
