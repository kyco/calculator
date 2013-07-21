# -*- coding: utf-8 -*-
#Maths
import math
import sys

#Financial Maths
i = 0.00
def compound_interest():
        monthly = 0
        Monthly = 0
        Month = 0
        month = 0
        Yearly = 0
        yearly = 0
        Year = 0
        year = 0
        print ' '
        P = input('The starting value: ')
        i = input('Interest rate: ')
        ir = input('Compounded monthly or yearly: ')
        n = input('Number of years: ')
        print ' '
        if i >= 1:
                i = i/100.00
        if ir == 'Monthly' or 'monthly' or 'month' or 'Monthly':
                i = i/12.00
                n = n*12
                A = P*(1+i)**n
        elif ir == 'Yearly' or 'yearly' or 'year' or 'Yearly':
                A = P*(1+i)**n
        return A

def simple_interest():
        print ' '
        P = input('The starting value: ')
        i = input('Interest rate: ')
        n = input('Number of years: ')
        print ' '
        if i >= 1:
                i = i/100.00
        A = P*(1+n*i)
        return A

def future_value():
        print ' '
        x = input('Payment per period: ')
        n = input('Number of payments: ')
        i = input('Interest rate: ')
        print ' '
        if i >= 1:
                i = i/100.00
        F = x*(((1+i)**n)-1)/i
        return F

def present_value():
        print ' '
        x = input('Payment per period: ')
        n = input('Number of payments: ')
        i = input('Interest rate: ')
        print ' '
        if i >= 1:
                i = i/100.00
        P = x*(1-((1+i)**-n))/i
        return P

#Financial Maths Options
def f_m_o():
  a = '''
  ---------------------------------
  1: Calculate amount as per compound interest
  2: Calculate amount as per simple interest
  3: Calculate future values
  4: Calculate present value
  0: Return to main menu
  '''
  return a

#Financial Maths Menu
def Financial_Maths_Menu():
  print f_m_o()
  while True:
    try:
      command = raw_input('\n Please select an option: ')
    except (IOError, KeyboardInterrupt):
      print '\n[*] Going back to main menu...'
      print rules()
      return

    if command in '1234567890':
        if command == '1':
         print '%0.2f' %  compound_interest()
        if command == '2':
          print '%0.2f' % simple_interest()
        if command == '3':
          print '%0.2f' % future_value() 
        if command == '4':
          print '%0.2f' % present_value()
        if command == '0':
          print '\n[*] Returning to main menu...'
          print rules()
          return
    else:
      print '\n[-] Invalid command'
      return

#Trigonometry

def cosine():
        print ' '
        b = input("angle: ")
        y = 90*math.pi/180
        x = math.cos(y)
        print ' '
        return x
def sine():
        print ' '
        b = input('angle: ')
        x = math.sin(b)
	y = b*(2*math.pi/360)
        print ' '
        return y
def tangent():
        print ' '
        b = input('angle: ')
        x = math.tan(math.degrees(b))
        print ' '
        return x
def arccosine():
        print ' '
        b = input('inverse of cos: ')
        x = math.acos(math.degrees(b))
        print ' '
        return x
def arcsine():
        print ' '
        b = input('inverse of sine: ')
        x = math.asin(math.degrees(b))
        print ' '
        return x
def arctangent():
        print ' '
        b = input('inverse of tan: ')
        x = math.atan(math.degrees(b))
        print ' '
        return x
def hcosine():
        print ' '
        b = input('enter value: ')
        x = math.cosh(math.degrees(b))
        print ' '
        return x
def hsine():
        print ' '
        b = input('enter value: ')
        x = math.sinh(math.degrees(b))
        print ' '
        return x
def htangent():
        print ' '
        b = input('enter value: ')
        x = math.tanh(math.degrees(b))
        print ' '
        return x

#Options
def t_o():
  o = '''
  ---------------------------
  1: Cosine
  2: Sine
  3: Tangent
  4: Arccosine
  5: Arcsine
  6: Arctangent
  7: Hyberbolic of cosine
  8: Hyperbolic of sine
  9: Hyberbolic of tangent
  0: Return to main menu
  
  *(cosine values in radians)
  *(Arc 'meaning the inverse of')
  '''
  return o

#Trig Menu

def trig():
  print t_o()
  while True:
    try:
      command = raw_input('\nPlease select an option: ').strip()
    except (IOError, KeyboardInterrupt):
      print '\n[*] Going back to menu'
      print rules()
      return
    
    if command in '1234567890':
      if command == '1':
        print cosine()
      if command == '2':
        print sine()
      if command == '3':
        print tangent()
      if command == '4':
        print arccosine()
      if command == '5':
        print arcsine()
      if command == '6':
        print arctangent()
      if command == '7':
        print hcosine()
      if command == '8':
        print hsine()
      if command == '9':
        print htangent()
      if command == '0':
        print '\n [*] Returning to main menu...'
        print rules()
        return
    else:
      print '\n [-] Invalid command'

#Trig Identities
def sinp():
  a = input('\nPlease enter the alpha value: ')
  b = input('\nPlease enter the beta value: ')
  print ' '
  r = (math.sin(math.degrees(a))*math.cos(math.degrees(b)))+(math.cos(math.degrees(a))*math.sin(math.degrees(b)))
  c = raw_input('\nsin('+`a`+')cos('+`b`+')'+'+'+'cos('+`a`+')sin('+`b`+')'+'\n'+`r`+'\nIs this correct (y/n): ')
  if c == 'n':
    print '\n[-] Please try again...'
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
    print_sin2a
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
      command = raw_input('\nWhat would you like to use?: ').strip()
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

#trig Ident menu
def trig_ident_menu_info():
  a = '''
  1: sin(a+b)
  2: sin(a-b)
  3: cos(a+b)
  4: cos(a-b)
  5: sin2a
  6: cos2a
  '''
  return a

def trig_ident_menu():
  print trig_ident_menu_info()
  while True:
    try:
      command = raw_input('\nWhat would you like to do?: ')
    except (IOError, KeyboardInterrupt):
        print '\n[*] Returning to main menu...'
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
    else:
      return

#Introduction
def intro():
  a = '''
  ##################################
  #                                #
  # Welcome to this maths program  #
  # Please select an option to     #
  # Continue                       #
  #                                #
  # Author: Kyluke(FNB)            #
  #                                #
  ##################################
 '''
  return a
 
def rules():
  r = '''
  ------------------------------
  1: Financial Maths
  2: Trigonometry
  3: Trigonometry Identities
  0: Exit Program
  9: Display options
  '''
  return r
  

# Main Menu
def main():
  print rules()
  while True:
    try:
      command = raw_input('\nWhat would you like to do?: ').strip()
    except (IOError, KeyboardInterrupt):
      print '\n[*] Cheers Bra'
      sys.exit()
      
    if command in '1234567890':
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
      print '\n [-] Invalid command'

print intro()
main()
