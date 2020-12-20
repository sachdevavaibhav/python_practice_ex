import random
import pygame.mixer
import time
#----------------------------MINUTE AND HOUR-----------------------------------------------

tm = time.time()
local_tm = time.localtime(tm)
format_tm = time.asctime(local_tm)
minute_tm = local_tm[4]
hour_tm = local_tm[3]

#----------------------------MINUTE AND HOUR-----------------------------------------------
pygame.mixer.init()

def water():
    water_sound = "water.mp3"
    print("\nHELLO FRIEND! YOU SHOULD DRINK SOME WATER")
    pygame.mixer.music.load(water_sound)
    pygame.mixer.music.play(-1)
    water_input = input("ENTER DRANK TO STOP: ")
    water_input = water_input.upper()
    write_water = f"[ {format_tm} ]: {water_input} \n"
    if water_input == "DRANK":
        pygame.mixer.music.stop()
        water_log = open("Water_record.txt", "a")
        water_log.write(write_water)
        water_log.close
        time.sleep(60)

def physical():
    physical_sound = "physical.mp3"
    print("\nHELLO FRIEND! YOU SHOULD DO SOME EXERCISE")
    pygame.mixer.music.load(physical_sound)
    pygame.mixer.music.play(-1)
    physical_input = input("ENTER EXDONE TO STOP: ")
    physical_input = physical_input.upper()
    write_physical = f"[ {format_tm} ]: {physical_input} \n"
    if physical_input == "EXDONE":
        pygame.mixer.music.stop()
        physical_log = open("Physical_record.txt", "a")
        physical_log.write(write_physical)
        physical_log.close
        time.sleep(60)

def eyes():
    eyes_sound = "eyes.mp3"
    print("\nHELLO FRIEND! GIVE SOME REST TO YOUR EYES")
    pygame.mixer.music.load(eyes_sound)
    pygame.mixer.music.play(-1)
    eyes_input = input("ENTER EYDONE TO STOP: ")
    eyes_input = eyes_input.upper()
    write_eyes = f"[ {format_tm} ]: {eyes_input} \n"
    if eyes_input == "EYDONE":
        pygame.mixer.music.stop()
        eyes_log = open("Eyes_record.txt", "a")
        eyes_log.write(write_eyes)
        eyes_log.close
        time.sleep(60)

health_quotes = ["GOOD HEALTH IS THE BEST WEALTH", "HEALTH IS THE GREATEST POSSESSION"
        , "A HEALTHY OUTSIDE STARTS FROM THE INSIDE"
        , "TAKE CARE OF YOUR BODY IT IS THE ONLY PLACE YOU HAVE TO LIVE"]
x = random.choice(health_quotes)
print(x)

try:
 while(hour_tm>=9 and hour_tm<=17):
# ----------------------------MINUTE AND HOUR-----------------------------------------------
  tm = time.time()
# print(tm)
  local_tm = time.localtime(tm)
# print(local_tm)
  format_tm = time.asctime(local_tm)
  minute_tm = local_tm[4]
# print(minute_tm)
  hour_tm = local_tm[3]
# print(hour_tm)
# ----------------------------MINUTE AND HOUR-----------------------------------------------

  if minute_tm == 25 or minute_tm == 55:
      water() #Assuming 1 glass of water = 220 ml
  elif minute_tm == 30:
        eyes()
  elif minute_tm == 45:
        physical()
  else:
        continue
except:
    print("Unexpected Error Occured!!")





















