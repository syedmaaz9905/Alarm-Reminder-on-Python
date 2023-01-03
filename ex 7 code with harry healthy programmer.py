from pygame import mixer
from datetime import datetime
from time import time

def water_music(file, stopper):
      mixer.init()
      mixer.music.load(file)
      mixer.music.play()
      while True:            
            a=input()
            a.lower()
            if a==stopper:
                  mixer.music.stop()
                  break
def log(msg):
      with open("my_fitness.txt","a") as f:
            f.write(f"{msg} {datetime.now()}\n")         

if __name__=='__main__':
      init_water=time()
      init_eyes=time()
      init_exercise=time()
      water=5
      eyes=10
      exercise=15
      while True:
            if time()-init_water > water:
                  print("Drink Water. If drank then write 'done' to stop the music.\nEnter Here: ",end='')
                  water_music("water.mp3","done")
                  init_water=time()
                  log("Drank water, at")
            if time()-init_eyes > eyes:
                  print("Work for your eyes. If yu are done then write 'done' to stop the music.\nEnter Here: ",end='')
                  water_music("eyes.mp3","done")
                  init_eyes=time()
                  log("Done with eyes check, at")
            if time()-init_exercise > exercise:
                  print("Work for your body. If yu are done then write 'done' to stop the music.\nEnter Here: ",end='')
                  water_music("exercise.mp3","done")
                  init_exercise=time()
                  log("Done with exercise, at")
            
