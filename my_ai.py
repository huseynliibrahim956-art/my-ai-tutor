import numpy as np
import time as t
import pandas as pd
#--------------------------------
runnin=True
rng=np.random.default_rng()
worker='AI'              
array_action=np.array(['working on','handling','doing','thinking','fixing'])
objectives=np.array(['the data','the dash board','the problem','the issue'])
greeting=np.array(['hi','hello','hey'])
friendlies=np.array(['i hope u r doing great :)','i m glad that u r good :)','how is your day?:)'])
questions=np.array(['what sort of problems do u wanna solve if u want?','how do you find about solving some problems?','i will helpp you to get better at math'])
def my_ai(func):
    def wrapper():
        func()
        sentence=f'{rng.choice(array_action)} {rng.choice(objectives)}'
        print(sentence)
    return wrapper
def friendly(func):
   def wrapper():
      func()
      sentence=f'{rng.choice(friendlies)}'
      print(sentence)
   return wrapper
t.sleep(1)
@my_ai
def math_ques():
   def tutor():
      df2=pd.read_csv('tutor.csv',index_col='ID')
      print('--------TUTORIAL-------')
      print(reader['Question'].to_string())
      print('-----------------------------')
      print('*****************************')
      ambitious=input('enter the difficulty of the question that you were looking for.').lower()
      if ambitious == 'easy':
         print(df2.loc['easy'].to_string())
         print('#############################')
         try:
          spotter=int(input('enter the index of the question that you were looking for'))
         except ValueError:
            t.sleep(1)
            print('you should have entered a num bro')
      elif ambitious == 'medium':
         print('-----------------------------')
         print(reader.loc['medium','Question'])
         print('##############################')
      elif ambitious=='hard':
         print('-----------------------------')
         print(reader.loc['medium','Question'])
         print('##############################')
      else:
         t.sleep()
         print('wdym gng?')
         pass
   reader=pd.read_csv("math_questions.csv",index_col='Difficulty')
   def easy():
      array1=np.array([reader.loc['easy']])
      guesser=rng.choice(reader.loc['easy','Question'])
      print(guesser)
      print('-------------------------')
      try:
       response=float(input('Answer:'))
       if response==reader.loc[reader['Question']==guesser,'Answer'].iloc[0]:
          print('YOU ARE AWESOME....')
       else:
          print(f'NOOOOO THE ANSWER WAS {reader.loc[reader['Question']==guesser,'Answer'].iloc[0]}')
          learner=input('oh it is wrong but no problem at all dontcha wanna know why? print y if u want :) ').lower()
          if learner=='y':
             tutor()
      except ValueError:
         t.sleep(1)
         print('you should have entered a number :(...')
   def medium():
      array1=np.array([reader.loc['medium']])
      guesser=rng.choice(reader.loc['medium','Question'])
      print(guesser)
      print('-------------------------')
      try:
       response=float(input('Answer:'))
       if response==reader.loc[reader['Question']==guesser,'Answer'].iloc[0]:
          print('YOU ARE AWESOME....')
       else:
          print(f'NOOOOO THE ANSWER WAS {reader.loc[reader['Question']==guesser,'Answer'].iloc[0]}')
          learner=input('oh it is wrong but no problem at all dontcha wanna know why? print y if u want :) ').lower()
          if learner=='y':
             tutor()
      except ValueError:
         t.sleep(1)
         print('you should have entered a number :(...)')
   def hard():
      xy=reader.loc['hard','Question']
      print(f'{xy}')
      print('--------------------------------')
      try:
       response=float(input('Answer:'))
       if response==reader.loc[reader['Question']==xy,'Answer'].iloc[0]:
          print('RIGHTTTTTTTTTTTTT')
       else:
          learner=input(f'the answer was {reader.loc[reader['Question']==xy,'Answer'].iloc[0]} but nb at all would u like to learn why??').lower()
          if learner=='y':
             tutor()
      except ValueError:
         print('you were expected to print a num :(')
   hardship=['easy','medium','hard']
   series2=pd.Series(hardship)
   print(series2)
   try:
      user=int(input('enter the index'))
      match user:
         case 0:
            easy()
         case 1:
            medium()
         case 2:
            hard()
         case val if val>2 or val<0:
            t.sleep(1)
            print('ok...')
   except ValueError:
      t.sleep(1)
      @my_ai
      def sad():
       print('i was expecting u to print a num :(')
      sad()
t.sleep(1)
@my_ai
def physics_ques():
   @my_ai
   def tutorial():
      for  ques in asker1.questions:
         print('--------------------')
         print(f'{ques}')
      print('**************************')
      series1=pd.Series(asker1.questions)
      try:
         learner=int(input('so which question would you like to learn??enter the index of them(starts with 0)'))
         if learner>=0 and learner<5:
            print('************************')
            print(series1.iloc[learner])
            print('************************')
            print(f'the answer is {aligning_dict.get(series1.iloc[learner])},lemme tell you why')
            print('----------------------------------------------------------')
            print(f'{teaching.get(series1.iloc[learner])}')
            print('-----------------------------------------------------------')
      except ValueError:
         print(f'you should have entered an index of the question')
         print('-------------------------------------------------')
#center of dictionaries------         
   class questions:
      def __init__(self,questions):
         self.questions=questions
   asker1=questions(questions=np.array(['what is the main difference between speed and velocity?',
                         'mass=200,initial velocity=20,force=-400,find the values a,stopping d,stopping t(time)',
                         'is r direct proportional with v in the circular motion?(prit yes or no)',
                         'what are g and G dont forget to use and between g and G or it will be considered wrong??',
                         'what is d which has no direction?']))
   nums_of_task={
      asker1.questions[0]:1,
      asker1.questions[1]:4,
      asker1.questions[2]:2,
      asker1.questions[3]:2,
      asker1.questions[4]:1,
   }
   helper_checker=pd.Series(nums_of_task)
   class checking(questions):
            def __init__(self, questions,check):
               super().__init__(questions)
               self.check=check
   checker=checking(check=[helper_checker.loc[asker1.questions[0]],
                           helper_checker.loc[asker1.questions[1]],
                           helper_checker.loc[asker1.questions[2]],
                           helper_checker.loc[asker1.questions[3]],
                           helper_checker.loc[asker1.questions[4]]],
                           questions=asker1.questions)
   another_useless={
      asker1.questions[0]:helper_checker.loc[asker1.questions[0]],
      asker1.questions[1]:helper_checker.loc[asker1.questions[1]],
      asker1.questions[2]:helper_checker.loc[asker1.questions[2]],
      asker1.questions[3]:helper_checker.loc[asker1.questions[3]],
      asker1.questions[4]:helper_checker.loc[asker1.questions[4]]
   }
   teaching={
      asker1.questions[0]:'the main difference between speed and velocity is velocity is speed with direction velocity is a vector quantity however speed isnt velocity can be negative or positive but speed can merely become positive',
      asker1.questions[1]:'so to find a(acceleration) we use newton"s 2th law which is F=ma F/m=a m=200 F=-400 so the answer of a is -2 then we use v0*t+(a*t**2)/2 to find displacement and v-v0/a for t v is 0 cuz it says stopping time so the answers are 10 and 100',
      asker1.questions[2]:'yes cuz v=(2*pi*r(radius))/T so when r increases v increases so that is why r is directly proportional',
      asker1.questions[3]:'g is gravitational acceleration G is universal gravitational constant,g means how much does the object increases its velocity at a second g is -9.8 ',
      asker1.questions[4]:'it is distance cuz distance is scalar quantity which means it has no direction so answer is distance.'
   }
#--------------------------------------------------
   #the formulas for question[1]
   m=200
   v0=20
   vf=0
   F=-400
   a=round(F/m,3)
   t=abs(round((vf-v0)/a,2))
   d=v0*t+((a*pow(t,2))/2)
   #----------------------------
   class answers(questions):
      def __init__(self, questions,answer):
         super().__init__(questions)
         self.questions=questions
         self.answer=answer
   answers_of_questions=answers(questions=asker1.questions,answer=['velocity has a direction but speed doesnt',
                                                                     f'{a},{t},{d}',
                                                                     'yes',
                                                                     'gravitational acceleration and universal gravitational constant',
                                                                     'distance'])
   aligning_dict={
      answers_of_questions.questions[0]:answers_of_questions.answer[0],
      answers_of_questions.questions[1]:answers_of_questions.answer[1],
      answers_of_questions.questions[2]:answers_of_questions.answer[2],
      answers_of_questions.questions[3]:answers_of_questions.answer[3],
      answers_of_questions.questions[4]:answers_of_questions.answer[4]
   }
#-----------------------------------------------------------------------------   
   @my_ai
   def easy_parts():
    matching_questions = [quesion for quesion, val in another_useless.items() if val == 1]
    if matching_questions:
        x = rng.choice(matching_questions)
        print('-----------------------')
        print(x)
        print('-------------------------')
        answerr=input('enter the answer:').lower()
        if answerr==aligning_dict.get(x) or answerr=='velocity is speed with direction':
           print('CORRRREEEEEEEEEECCCCCCCTTTT')
        else:
           wanter=input(f'no the answer was {aligning_dict.get(x)} but do you wanna learn why?:)press y if u want').lower()
           if wanter=='y':
              tutorial()
         
   @my_ai 
   def average_parts():
      average=[quesion for quesion,val in another_useless.items() if val>1 and val<3]
      if average:
         y=rng.choice(average)
         print('-----------------------')
         print(y)
         print('-------------------------')
         answerr=input('enter the answer:')
         if answerr==aligning_dict.get(y):
            print('correct!!!')
         else:
            print(f'no the answer was {aligning_dict.get(y)}')
            ambitiousness=input('incorrect however would you like to learn why??press y if u want').lower()
            if ambitiousness=='y':
               tutorial()
   @my_ai       
   def hard_parts():
      hard=[quesion for quesion,val in another_useless.items() if val>3]
      if hard:
         z=rng.choice(hard)
         print('-----------------------')
         print(z)
         print('-------------------------')
         answerr=input('enter the answer:pls dont forget to add the .0 if ti is to print 2.0'
         'and the queu must be a,t,d')
         if answerr==aligning_dict.get(z) or answerr==f'{a} {t} {d}':
            print('CORREEEEEEECCCCCCTTTTTTTT')
         else:
            print(f'no the answer was {aligning_dict.get(z)}')
            ambitious=input('incorrect however would you like to learn why?? press y if u want:)').lower() 
            if ambitious=='y':
               tutorial()
   lists=['easy','hard','average']
   sup_pd=pd.Series(lists)
   print(sup_pd)
   try:
    user=int(input('enter the num'))
    match user:
       case 0:
          easy_parts()
       case 1:
           hard_parts()
       case 2:
          average_parts()
   except ValueError:
      print('the num was expected to be between 1-3 included or an int not a float or str')
def python_ques():
   class questions:
      def __init__(self,question):
         self.question=question
   class asnwers(questions):
      def __init__(self, question,answer):
         super().__init__(question)
         self.answer=answer
   array1_python_q=np.array(['what r the booleans?','x=2 if x<3:print(lesser!) what is gonna happen?',
                             'what do we use to add things to lists?'])
   answers_dict={
      array1_python_q[0]:'true false',
      array1_python_q[1]:'lesser',
      array1_python_q[2]:'append',
   }
   series=pd.Series(answers_dict)
   ques1=questions(question=rng.choice(array1_python_q))
   answer1=asnwers(question=ques1.question,answer=series.loc[ques1.question])
   @my_ai
   def learning():
      while runnin:
       try:
        num=int(input('pick a number between 1-3 4 to exit'))
        if num>0 and num<5:
         learning_dict={
            ques1.question:answer1.answer
         }
         series1=pd.Series(learning_dict)
         print(ques1.question,'=',series1.loc[ques1.question])
         array_exp=np.array(['booleans consist of only true and false we mainly use them to know if the variable is correct'
         'or some similar things','that will output the word lesser vuz the variable x is 2 if x<3 means if x is lesser '
         'than 3 print the word lesser so x was 2 which means x is lesser than 3 so it will output the word lesser',
         'we use append to add things to lists however there is a catch append add things to lists'
         'but the index of the things (that were added) will be last '])
         lists_for_arrays=[array1_python_q[0],array1_python_q[1],array1_python_q[2]]
         i=lists_for_arrays.index(ques1.question)
         print(array_exp[i])
        elif num==4:
          break
       except ValueError:
          print('no')
   while runnin:
    user=input('pick a random number between 1-3,4 to exit')
    if user.isdigit():
       user=int(user)
       if user==3 or user==1 or user==2:
        response=input(ques1.question).lower()
        if response==answer1.answer:
           t.sleep(1)
           @my_ai
           def truee():
            t.sleep(1)
            print('TRUE!')
           truee()
        elif response!=answer1.answer:
           t.sleep(1)
           @my_ai
           def falsee():
            print('wrong :(')
           falsee()
       elif user==4:
          users=input('just to ask do you wanna learn those python questions???press y if u want press any button if dont').lower()
          if users=='y':
             learning()
          else:
             break
    else:
       print('i said pick a number!!!')
@friendly
def main():
    while runnin:
        print(rng.choice(greeting),f'i m an {worker} made by python')
        user=input(f'{rng.choice(questions)} press y if u want').lower()
        if user=='y':
            print('1.math')
            print('2.physics')
            print('3.python')
            try:
             users=int(input('enter the num of which part do u wanna learn by solving problems??'))
             match users:
                case 1:
                   math_ques()
                case 2:
                   physics_ques()
                case 3:
                   python_ques()
            except ValueError:
               @my_ai
               def m():
                t.sleep(1)
                print('this is against the laws :( quitting...')
               m()
               break
        else:
            break
main()