import subprocess
import pyttsx3
import webbrowser
import pymysql
import subprocess
import speech_recognition as sr
import datetime
import webbrowser
import os
import winshell
import pyjokes
import smtplib
import ctypes
import time
import requests
import shutil
import win32com.client as wincl
from urllib.request import urlopen


conn = pymysql.connect(host ="localhost", user="root", passwd="", db="healthcare")
myCursor = conn.cursor()

'''myCursor.execute("""CREATE TABLE doctor
(
t_no int(10),  
name varchar(20),     
doctor varchar(20),                             
date DATE             
)
""")'''

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir !")

    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

    assname =("Healthcare Assistant")
    speak("I am your ")
    speak(assname)

def usrname():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))


def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognizing your voice.")
        return "None"

    return query

def menu():
    columns = shutil.get_terminal_size().columns
    speak("The menu is given below select one of the above")

    print("#####################".center(columns))
    print("Menu".center(columns))
    print("1.Disease".center(columns))
    print("2.Doctor".center(columns))
    print("3.Normal assistant".center(columns))
    print("#####################".center(columns))
    while True:

        query = takeCommand().lower()

        if 'disease' in query:
            disease()

        elif 'doctor' in query:
            doctor()

        elif 'normal' in query or 'assistant' in query:
            assis()

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop assistant from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        else:
            speak("invalid option")

def assis():

    while True:

        query = takeCommand().lower()

        if "Good Morning" in query:
            speak("A warm" +query)
            speak("How are you sir")

        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")

        elif "how are you" in query:
            speak("I'm fine, glad you me that")

        elif "i love you" in query:
            speak("It's hard to understand")

        elif "fine" in query:
            speak("Good to hear that")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop assistant from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")

        elif "who i am" in query:
            speak("If you talk then definately your human.")

        elif 'search' in query or 'play' in query:

            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")
            speak(f"Sir, the time is {strTime}")

        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'menu' in query or 'back' in query:
            speak("redirecting to menu")
            menu()

        else:
            speak("sorry i can't do that")

def disease():

    speak("Tell me your symptoms")

    while True:
        query = takeCommand().lower()

        if 'lack of energy' in query or 'weakness' in query and 'weight loss' in query and 'increased thirst' in query:
            speak("There ia a possibility that you have Addison’s disease")
            speak("Addison’s disease is a rare disorder of the adrenal glands.The adrenal glands are two small glands that sit on top of the kidneys. They produce essential hormones: cortisol, aldosterone and adrenaline.In Addison's disease, the adrenal gland is damaged, and not enough cortisol and aldosterone are produced.")
            print("There ia a possibility that you have Addison’s disease")
            print("Addison’s disease is a rare disorder of the adrenal glands.The adrenal glands are two small glands that sit on top of the kidneys. They produce essential hormones: cortisol, aldosterone and adrenaline.In Addison's disease, the adrenal gland is damaged, and not enough cortisol and aldosterone are produced.")


        elif 'sneezing' in query or 'wheezing and coughing' in query and 'blocked nose' in query and 'watery eyes' in query or 'itchy eyes' in query or 'red eyes' in query and 'rashes' in query:
            speak("There is a possibility that you have allergies")
            speak("An allergy is a reaction the body has to a particular food or substance.")
            speak("They are particularly common in children. Some allergies go away as a child gets older, although many are lifelong. Adults can develop allergies to things they weren't previously allergic to.")
            print("There is a possibility that you have allergies")
            print("An allergy is a reaction the body has to a particular food or substance.")
            print("They are particularly common in children. Some allergies go away as a child gets older, although many are lifelong. Adults can develop allergies to things they weren't previously allergic to.")


        elif 'whistling sound in breathe' in query and 'tight chest' in query and 'coughing' in query and 'shortness of breath' in query:
            speak("There is a possibility that you have Asthma")
            speak("Asthma is a common long-term condition that can cause coughing, wheezing, chest tightness and breathlessness.The severity of these symptoms varies from person to person. Asthma can be controlled well in most people most of the time, although some people may have more persistent problems.")
            print("There is a possibility that you have Asthma")
            print("Asthma is a common long-term condition that can cause coughing, wheezing, chest tightness and breathlessness.The severity of these symptoms varies from person to person. Asthma can be controlled well in most people most of the time, although some people may have more persistent problems.")


        elif 'feeling sick' in query or 'nausea' in query or 'being sick' in query and 'loss of appetite' in query and 'flushed face' in query:
            speak("There is a possibility that you have Appendicitis")
            speak("Appendicitis is a painful swelling of the appendix. The appendix is a small, thin pouch about 5-10cm  long. It's connected to the large intestine, where stools are formed.")
            print("There is a possibility that you have Appendicitis")
            print("Appendicitis is a painful swelling of the appendix. The appendix is a small, thin pouch about 5-10cm  long. It's connected to the large intestine, where stools are formed.")


        elif 'weakness' in query and 'red skin' in query and 'cannot move' in query:
            speak("There is a possibility that you have Arthritis")
            speak("Arthritis is a common condition that causes pain and inflammation in a joint.")
            print("There is a possibility that you have Arthritis")
            print("Arthritis is a common condition that causes pain and inflammation in a joint.")


        elif 'pain' in query and 'feeling sick' in query or 'feeling unwell' in query and 'diarrhoea' in query or 'loss of appetite' in query:
            speak("There is a possibility that you have Alcohol-related liver disease")
            speak("Alcohol-related liver disease (ARLD) refers to liver damage caused by excess alcohol intake. There are several stages of severity and a range of associated symptoms.")
            print("There is a possibility that you haveAlcohol-related liver disease")
            print("Alcohol-related liver disease (ARLD) refers to liver damage caused by excess alcohol intake. There are several stages of severity and a range of associated symptoms.")


        elif 'getting lost' in query or 'confusion' in query and 'getting lost' in query or 'problem in language' in query and 'change in personality' in query:
            speak("There is a possibility that you have Alzheimer's disease")
            speak("Alzheimer's disease is the most common type of dementia. The exact cause of Alzheimer's disease is unknown, although a number of things are thought to increase your risk of developing the condition")
            print("There is a possibility that you have Alzheimer's disease")
            print("Alzheimer's disease is the most common type of dementia. The exact cause of Alzheimer's disease is unknown, although a number of things are thought to increase your risk of developing the condition")


        elif 'painful sensation' in query and 'swelling in throat' in query and 'stomach pain' in query:
            speak("There is a possibility that you have Angioedema")
            speak("The main sign of angioedema is swelling that develops below the skin's surface")
            print("There is a possibility that you have Angioedema")
            print("The main sign of angioedema is swelling that develops below the skin's surface")


        elif 'hungry' in query or 'eat a lot' in query and 'faster' in query:
            speak("There is a possibility that you have Binge eating disorder")
            speak("Binge eating is an eating disorder where a person feels they have to overeat through regular binges.People who binge eat consume very large amounts of food over a short period of time, even when they’re not hungry.")
            print("There is a possibility that you have Binge eating disorder")
            print("Binge eating is an eating disorder where a person feels they have to overeat through regular binges.People who binge eat consume very large amounts of food over a short period of time, even when they’re not hungry.")


        elif 'lack of energy' in query or 'sad' in query or 'suicidal thoughts' in query or 'irritated' in query or 'not eating' in query:
            speak("There is a possibility that you have Bipolar disorder")
            speak("Bipolar disorder, formerly known as manic depression, is a condition that affects your moods, which can swing from one extreme to another")
            print("There is a possibility that you have Bipolar disorder")
            print("Bipolar disorder, formerly known as manic depression, is a condition that affects your moods, which can swing from one extreme to another")


        elif 'toe' in query and 'pain' in query or 'stiffness' in query and 'swelling' in query:
            speak("There is a possibility that you have Bunion")
            speak("A bunion is a deformity caused by the base joint of the big toe developing sideways. This pushes the bones of the big toe towards the smaller toes.")
            print("There is a possibility that you have Bunion")
            print("A bunion is a deformity caused by the base joint of the big toe developing sideways. This pushes the bones of the big toe towards the smaller toes.")


        elif 'overeating' in query or 'food' in query and 'purging' in query:
            speak("There is a possibility that you have Bulimia")
            speak("Bulimia nervosa is an eating disorder and mental health condition. People with bulimia are very anxious about their weight and focused on having the right body shape. They also spend a lot of time thinking about food")
            print("There is a possibility that you have Bulimia")
            print("Bulimia nervosa is an eating disorder and mental health condition. People with bulimia are very anxious about their weight and focused on having the right body shape. They also spend a lot of time thinking about food")


        elif 'sore throat' in query and 'headache' in query and 'pain in nose' in query:
            speak("There is a possibility that you have Bronchitis")
            speak("Bronchitis is an infection of the main airways of the lungs , causing them to become irritated and inflamed.The main symptom is a cough, which may bring up yellow-grey mucus . Bronchitis may also cause a sore throat and wheezing.")
            print("There is a possibility that you have Bronchitis")
            print("Bronchitis is an infection of the main airways of the lungs , causing them to become irritated and inflamed. The main symptom is a cough, which may bring up yellow-grey mucus . Bronchitis may also cause a sore throat and wheezing.")


        elif 'breath' in query and 'blood' in query and 'pain' in query or 'clubbing' in query:
            speak("There is a possibility that you have Bronchiectasis")
            speak("Bronchiectasis is a long-term condition where the airways of the lungs become abnormally widened, leading to a build-up of excess mucus that can make the lungs more vulnerable to infection.")
            print("There is a possibility that you have Bronchiectasis")
            print("Bronchiectasis is a long-term condition where the airways of the lungs become abnormally widened, leading to a build-up of excess mucus that can make the lungs more vulnerable to infection.")


        elif 'male' in query and 'nipple' in query and 'fluid' in query and 'hard' in query:
            speak("There is a possibility that you have Breast cancer")
            speak("Breast cancer is often thought of as a condition that only affects women, but men can also develop it.")
            print("There is a possibility that you have Bronchiectasis")
            print("Breast cancer is often thought of as a condition that only affects women, but men can also develop it.")


        elif 'female' in query and 'nipple' in query and 'rashes' in query and 'swelling' in query:
            speak("There is a possibility that you have Breast cancer")
            speak("Breast cancer is the most common type of cancer. Most women who get it are over 50, but younger women, and in rare cases, men, can also get breast cancer. If it's treated early enough, breast cancer can be prevented from spreading to other parts of the body.")
            print("There is a possibility that you have Breast cancer")
            print("Breast cancer is the most common type of cancer. Most women who get it are over 50, but younger women, and in rare cases, men, can also get breast cancer. If it's treated early enough, breast cancer can be prevented from spreading to other parts of the body.")


        elif 'headaches' in query and 'seizures' in query or 'fits' in query and 'nausea' in query or 'vomiting' in query and 'weakness' in query and 'vision' in query:
            speak("There is a possibility that you have Brain tumours")
            speak("A brain tumour is a growth of cells in the brain that multiplies in an abnormal, uncontrollable way. It can either be cancerous or non-cancerous.")
            print("There is a possibility that you have Brain tumours")
            print("A brain tumour is a growth of cells in the brain that multiplies in an abnormal, uncontrollable way. It can either be cancerous or non-cancerous.")


        elif 'bone' in query and 'weak' in query and 'swelling' in query or 'redness' in query and 'lump' in query:
            speak("There is a possibility that you have Bone cancer")
            speak("Primary bone cancer is a rare type of cancer that begins in the bones. This is a separate condition from secondary bone cancer, which is cancer that spreads to the bones after developing in another part of the body.")
            print("There is a possibility that you have Bone cancer")
            print("Primary bone cancer is a rare type of cancer that begins in the bones. This is a separate condition from secondary bone cancer, which is cancer that spreads to the bones after developing in another part of the body.")


        elif 'pee' in query and 'more' in query and 'urine' in query and 'fever' in query:
            speak("There is a possibility that you have Cystitis")
            speak("Cystitis is inflammation of the bladder, usually caused by a bladder infection. It's a common type of urinary tract infection (UTI), particularly in women, and is usually more of a nuisance than a cause for serious concern. Mild cases will often get better by themselves within a few days.")
            print("There is a possibility that you have Cystitis")
            print("Cystitis is inflammation of the bladder, usually caused by a bladder infection. It's a common type of urinary tract infection (UTI), particularly in women, and is usually more of a nuisance than a cause for serious concern. Mild cases will often get better by themselves within a few days.")


        elif 'pain' in query and 'cramp' in query and 'weight' in query and 'blood' in query or 'mucus' in query:
            speak("There is a possibility that you have Crohn's disease")
            speak("Crohn's disease is a long-term condition that causes inflammation of the lining of the digestive system.")
            print("There is a possibility that you have Crohn's disease")
            print("Crohn's disease is a long-term condition that causes inflammation of the lining of the digestive system.")


        elif 'cough' in query and 'high temperature fever' in query and 'loss' in query and 'smell' in query or 'taste' in query:
            speak("There is a possibility that you have coronavirus")
            speak("Coronavirus is the illness caused by a new strain of coronavirus first identified in Wuhan city, China. It can cause a new continuous cough, fever or loss of, or change in, sense of smell or taste.")
            print("There is a possibility that you have coronavirus")
            print("Coronavirus is the illness caused by a new strain of coronavirus first identified in Wuhan city, China. It can cause a new continuous cough, fever or loss of, or change in, sense of smell or taste.")


        elif 'stomach' in query and 'cramp' in query or 'ache' in query and 'sick' in query and 'loss' in query and 'appetite' in query:
            speak("There is a possibility that you have constipation")
            speak("Constipation is a common condition that affects people of all ages. It can mean that you're not passing stools regularly or you're unable to completely empty your bowel.")
            print("There is a possibility that you have constipation")
            print("Constipation is a common condition that affects people of all ages. It can mean that you're not passing stools regularly or you're unable to completely empty your bowel.")


        elif 'eyes' in query and 'red' in query or 'redness' in query and 'more' in query and 'water' in query or 'mucus' in query:
            speak("There is a possibility that you have Conjunctivitis")
            speak("Conjunctivitis is a common condition that causes redness and inflammation of the thin layer of tissue that covers the front of the eye. People often refer to conjunctivitis as red eye.")
            print("There is a possibility that you have Conjunctivitis")
            print("Conjunctivitis is a common condition that causes redness and inflammation of the thin layer of tissue that covers the front of the eye. People often refer to conjunctivitis as red eye.")


        elif 'throat' in query and 'nose' in query and 'blocked' in query or 'running' in query and 'sneezing' in query or 'cough' in query:
            speak("There is a possibility that you have Common cold")
            speak("A cold is a mild viral infection of the nose, throat, sinuses and upper airways. It's very common and usually clears up on its own within a week or two.")
            print("There is a possibility that you have Common cold")
            print("A cold is a mild viral infection of the nose, throat, sinuses and upper airways. It's very common and usually clears up on its own within a week or two.")


        elif 'chest' in query and 'mucus' in query or 'blood' in query and 'high temperature' in query and 'pain' in query or 'tightness' in query:
            speak("There is a possibility that you have Chest infection")
            speak("Chest infections are common, especially after a cold or flu during autumn and winter. Although most are mild and get better on their own, some can be serious or even life-threatening.")
            print("There is a possibility that you have Chest infection")
            print("Chest infections are common, especially after a cold or flu during autumn and winter. Although most are mild and get better on their own, some can be serious or even life-threatening.")


        elif 'red rashes' in query and 'face' in query or 'belly' in query or 'chest' in query or 'arms' in query or 'legs' in query:
            speak("There is a possibility that you have Chickenpox")
            speak("Chickenpox is a mild and common childhood illness that most children catch at some point.")
            print("There is a possibility that you have Chickenpox")
            print("Chickenpox is a mild and common childhood illness that most children catch at some point.")

        elif 'weekness' in query and 'weight' in query and 'sick' in query and 'vomiting' in query and 'pain' in query and 'skin' in query and 'eyes' in query:
            speak("There is a possibility that you have Cirrhosis")
            speak("Cirrhosis is scarring of the liver caused by continuous, long-term liver damage. Scar tissue replaces healthy tissue in the liver and prevents the liver from working properly.")
            print("There is a possibility that you have Cirrhosis")
            print("Cirrhosis is scarring of the liver caused by continuous, long-term liver damage. Scar tissue replaces healthy tissue in the liver and prevents the liver from working properly.")


        elif 'throat' in query and 'nose' in query and 'blocked' in query and 'headache' in query and 'mucus' in query:
            speak("There is a possibility that you have catarrh")
            speak("Catarrh is a build-up of mucus in an airway or cavity of the body. It usually affects the back of the nose, the throat or the sinuses. It's often temporary, but some people experience it for months or years. This is known as chronic catarrh.")
            print("There is a possibility that you have catarrh")
            print("Catarrh is a build-up of mucus in an airway or cavity of the body. It usually affects the back of the nose, the throat or the sinuses (air-filled cavities in the bones of the face). It's often temporary, but some people experience it for months or years. This is known as chronic catarrh.")


        elif 'dry' in query and 'mouth' in query or 'eyes' in query or 'lips' in query and 'headache' in query and 'urine' in query:
            speak("There is a possibility that you have Dehydration")
            speak("Dehydration occurs when your body loses more fluid than you take in. When the normal water content of your body is reduced, it upsets the balance of minerals (salts and sugar) in your body, which affects the way it functions")
            print("There is a possibility that you have Dehydration")
            print("Dehydration occurs when your body loses more fluid than you take in. When the normal water content of your body is reduced, it upsets the balance of minerals (salts and sugar) in your body, which affects the way it functions")


        elif 'tooth' in query or 'gum' in query and 'pain' in query and 'redness' in query and 'swelling' in query and 'sensitivity' in query:
            speak("There is a possibility that you have Dental abscess")
            speak("A dental abscess is a collection of pus that can form inside the teeth, in the gums, or in the bone that holds the teeth in place. It’s caused by a bacterial infection.")
            print("There is a possibility that you have Dental abscess")
            print("A dental abscess is a collection of pus that can form inside the teeth, in the gums, or in the bone that holds the teeth in place. It’s caused by a bacterial infection.")


        elif 'sadness' in query or 'low' in query and 'feeling' in query or 'loosing' in query and 'suicide' in query or 'harming' in query:
            speak("There is a possibility that you have Depression")
            speak("Everyone has spells of feeling down, but depression is more than just spending a few days feeling sad or unhappy. Depression can make you feel persistently sad and down for weeks or months at a time.")
            print("There is a possibility that you have Depression")
            print("Everyone has spells of feeling down, but depression is more than just spending a few days feeling sad or unhappy. Depression can make you feel persistently sad and down for weeks or months at a time.")


        elif 'elbows' in query or 'buttocks' in query or 'knees' in query and 'itching' in query or 'stinging' in query and 'rashes' in query and 'red' in query:
            speak("There is a possibility that you have Dermatitis herpetiformis")
            speak("Dermatitis herpetiformis (DH) is an autoimmune skin condition linked to coeliac disease.")
            print("There is a possibility that you have Dermatitis herpetiformis")
            print("Dermatitis herpetiformis (DH) is an autoimmune skin condition linked to coeliac disease.")


        elif 'stomach' in query and 'nausea' in query and 'vomiting' in query and 'headache' in query or 'cramp' in query:
            speak("There is a possibility that you have Dermatitis Diarrhoea")
            speak("Diarrhoea is passing looser or more frequent stools than is normal for you. It affects most people from time to time and is usually nothing to worry about. However, it can be distressing and unpleasant until it passes, which normally takes a few days to a week.")
            print("There is a possibility that you have Dermatitis Diarrhoea")
            print("Diarrhoea is passing looser or more frequent stools than is normal for you. It affects most people from time to time and is usually nothing to worry about. However, it can be distressing and unpleasant until it passes, which normally takes a few days to a week.")


        elif 'abdominal pain' in query or 'pain' in query and 'bloating' in query and 'change in bowel habits' in query or 'change in bowel' in query:
            speak("There is a possibility that you have Diverticular disease and diverticulitis")
            speak("Diverticular disease and diverticulitis are related digestive conditions that affect the large intestine.")
            print("There is a possibility that you have Diverticular disease and diverticulitis")
            print("Diverticular disease and diverticulitis are related digestive conditions that affect the large intestine.")


        elif 'eating' in query or 'drinking' in query and 'coughing' in query or 'choking' in query or 'nose' in query and 'food' in query and 'throat' in query or 'chest' in query or 'drooling' in query:
            speak("There is a possibility that you have Dysphagia")
            speak("Dysphagia is the medical term for swallowing difficulties. Some people with dysphagia have problems swallowing certain foods or liquids, while others can't swallow at all.")
            print("There is a possibility that you have Dysphagia")
            print("Dysphagia is the medical term for swallowing difficulties. Some people with dysphagia have problems swallowing certain foods or liquids, while others can't swallow at all.")


        elif 'ear' in query and 'earache' in query and 'itchiness' in query and 'vertigo' in query:
            speak("There is a possibility that you have Earwax build-up")
            speak("Earwax is produced inside your ears to keep them clean and free of germs. It usually passes out of the ears harmlessly, but sometimes too much can build up and block the ears.")
            print("There is a possibility that you have Earwax build-up")
            print("Earwax is produced inside your ears to keep them clean and free of germs. It usually passes out of the ears harmlessly, but sometimes too much can build up and block the ears.")


        elif 'fever' in query and 'joint pain' in query and 'sore throat' in query and 'muscle pain' in query and 'headache' in query:
            speak("There is a possibility that you have Ebola virus disease")
            speak("Ebola virus disease is a serious illness that originated in Africa, where a large outbreak occurred in 2014-15. In June 2016, the outbreak was officially declared over.")
            print("There is a possibility that you have Ebola virus disease")
            print("Ebola virus disease is a serious illness that originated in Africa, where a large outbreak occurred in 2014-15. In June 2016, the outbreak was officially declared over.")


        elif 'eye' in query and 'vision' in query and 'dark patch' in query and 'bulging' in query and 'lump' in query and 'pain' in query:
            speak("There is a possibility that you have Eye cancer")
            speak("Cancer can also sometimes develop in the tissues surrounding your eyeball or spread to the eye from other parts of the body, such as the lungs or breasts.")
            print("There is a possibility that you have Eye cancer")
            print("Cancer can also sometimes develop in the tissues surrounding your eyeball or spread to the eye from other parts of the body, such as the lungs or breasts.")


        elif 'abdominal pain' in query and 'diarrhoea' in query:
            speak("There is a possibility that you have Ulcerative colitis")
            speak("Ulcerative colitis is a long-term condition, where the colon and rectum become inflamed. The colon is the large intestine, and the rectum is the end of the bowel where stools are stored.")
            print("There is a possibility that you have Ulcerative colitis")
            print("Ulcerative colitis is a long-term condition, where the colon and rectum become inflamed. The colon is the large intestine, and the rectum is the end of the bowel where stools are stored.")


        elif 'tiredness' in query and 'weight gain' in query and 'pain' in query and 'periods' in query and 'movements' in query and 'muscle' in query:
            speak("There is a possibility that you have Underactive thyroid")
            speak("An underactive thyroid gland (hypothyroidism) is where your thyroid gland doesn't produce enough hormones. Common signs of an underactive thyroid are tiredness, weight gain and feeling depressed.")
            print("There is a possibility that you have Underactive thyroid")
            print("An underactive thyroid gland (hypothyroidism) is where your thyroid gland doesn't produce enough hormones. Common signs of an underactive thyroid are tiredness, weight gain and feeling depressed.")


        elif 'blood' in query and 'pee' in query and 'pain' in query:
            speak("There is a possibility that you have Urinary tract infection")
            speak("Urinary tract infections are common infections that can affect the bladder, the kidneys and the tubes connected to them.")
            print("There is a possibility that you have Urinary tract infection")
            print("Urinary tract infections are common infections that can affect the bladder, the kidneys and the tubes connected to them.")


        elif 'ankle' in query and 'legs' in query and 'swelling' in query and 'smell' in query:
            speak("There is a possibility that you have Venous leg ulcer")
            speak("A leg ulcer is a long-lasting sore that takes more than 4 to 6 weeks to heal. They usually develop on the inside of the leg, just above the ankle.")
            print("There is a possibility that you have Venous leg ulcer")
            print("A leg ulcer is a long-lasting sore that takes more than 4 to 6 weeks to heal. They usually develop on the inside of the leg, just above the ankle.")


        elif 'dry' in query and 'flaky' in query and 'red' in query and 'swollen' in query and 'pain' in query:
            speak("There is a possibility that you have Varicose eczema")
            speak("Varicose eczema is a long-term skin condition that affects the lower legs and is common in people with varicose veins.")
            print("There is a possibility that you have Varicose eczema")
            print("Varicose eczema is a long-term skin condition that affects the lower legs and is common in people with varicose veins.")


        elif 'fever in children' in query or 'child fever' in query or 'kid fever' in query:
            speak("You have a fever when your temperature rises above its normal range.")
            speak("What's normal for you may be a little higher or lower than the average normal temperature of 98.6 F (37 C).")
            speak("Depending on what causing your fever, additional fever signs and symptoms may include are:")
            speak("Sweating")
            speak("Chills and shivering")
            speak("Headache")
            speak("Muscle aches")
            speak("Loss of appetite")
            speak("Irritability")
            speak("Dehydration")
            speak("General weakness")
            print("You have a fever when your temperature rises above its normal range.")
            print("What's normal for you may be a little higher or lower than the average normal temperature of 98.6 F (37 C).")
            print("Depending on what causing your fever, additional fever signs and symptoms may include are:")
            print("Sweating")
            print("Chills and shivering")
            print("Headache")
            print("Muscle aches")
            print("Loss of appetite")
            print("Irritability")
            print("Dehydration")
            print("General weakness")

        elif 'flu' in query and 'influenza' in query and 'stuffy nose' in query and 'feeling feverish' in query:
            speak("Influenza (flu) can cause mild to severe illness, and at times can lead to death.")
            speak("Flu is different from a cold. Flu usually comes on suddenly.")
            speak("People who have flu often feel some or all of these symptoms are:")
            speak("Fever or Feeling feverish/chills")
            speak("cough")
            speak("sore throat")
            speak("fatigue (tiredness)")
            speak("muscle or body aches")
            speak("Runny or stuffy nose")
            speak("some people may have vomiting and diarrhea, though this is more common in children than adults.")
            print("Influenza (flu) can cause mild to severe illness, and at times can lead to death.")
            print("Flu is different from a cold. Flu usually comes on suddenly.")
            print("People who have flu often feel some or all of these symptoms are:")
            print("Fever or Feeling feverish/chills")
            print("cough")
            print("sore throat")
            print("fatigue (tiredness)")
            print("muscle or body aches")
            print("Runny or stuffy nose")
            print("some people may have vomiting and diarrhea, though this is more common in children than adults.")

        elif 'food poisoning' in query or 'food poison' in query or 'food poison in stomach' in query or 'foodborne illness' in query or 'toxic food' in query or 'spoiled food' in query:
            speak("Foodborne illness, more commonly referred to as food poisoning, is the result of eating contaminated, spoiled, or toxic food. ")
            speak("The most common symptoms of food poisoning include nausea, vomiting, and diarrhea. Although it's quite uncomfortable, food poisoning isn't unusual.")
            print("Foodborne illness, more commonly referred to as food poisoning, is the result of eating contaminated, spoiled, or toxic food. ")
            print("The most common symptoms of food poisoning include nausea, vomiting, and diarrhea. Although it's quite uncomfortable, food poisoning isn't unusual.")

        elif 'nail infection' in query or 'fungal nail infection' in query or 'nail fungus' in query or 'nail discolor' in query or 'crumble nail' in query or 'distorted nail' in query:
            speak("Nail fungus is a common condition that begins as a white or yellow spot under the tip of your fingernail or toenail.")
            speak("If your nail fungus is painful and has caused thickened nails, self-care steps and medications may help.")
            speak("You may have nail fungus if one or more of your nails are:")
            speak("Thickened")
            speak("Whitish to yellow-brown discoloration")
            speak("Brittle, crumbly or ragged")
            speak("Distorted in shape")
            speak("A dark color, caused by debris building up under your nail")
            speak("Smelling slightly foul")
            print("Nail fungus is a common condition that begins as a white or yellow spot under the tip of your fingernail or toenail.")
            print("If your nail fungus is painful and has caused thickened nails, self-care steps and medications may help.")
            print("You may have nail fungus if one or more of your nails are:")
            print("Thickened")
            print("Whitish to yellow-brown discoloration")
            print("Brittle, crumbly or ragged")
            print("Distorted in shape")
            print("A dark color, caused by debris building up under your nail")
            print("Smelling slightly foul")


        elif 'gastroenteritis' in query or 'gastro' in query or 'stomach bug' in query or 'stomach virus' in query or 'stomach flu' in query or 'gastric flu' in query or 'gas' in query:
            speak("Gastroenteritis is a very common condition that causes diarrhoea and vomiting. It usually caused by a bacterial or viral tummy bug.")
            speak("It affects people of all ages, but is particularly common in young children.")
            speak("common causes. Eating improperly prepared food, drinking contaminated water or close contact with a person who is infected can spread the disease.")
            speak("The main symptoms of gastroenteritis are:")
            speak("sudden, watery diarrhoea")
            speak("feeling sick")
            speak("vomiting, which can be projectile")
            speak("a mild fever")
            print("Gastroenteritis is a very common condition that causes diarrhoea and vomiting. It usually caused by a bacterial or viral tummy bug.")
            print("It affects people of all ages, but is particularly common in young children.")
            print("common causes. Eating improperly prepared food, drinking contaminated water or close contact with a person who is infected can spread the disease.")
            print("The main symptoms of gastroenteritis are:")
            print("sudden, watery diarrhoea")
            print("feeling sick")
            print("vomiting, which can be projectile")
            print("A mild fever")

        elif 'glandular fever' in query or 'mono' in query or 'mononucleosis' in query or 'mononucleosis' in query:
            speak("Glandular fever is a type of viral infection that mostly affects young adults.")
            speak("It is also known as infectious mononucleosis, or mono.")
            speak("Common symptoms include:")
            speak("A high temperature (fever)")
            speak("A severely sore throat")
            speak("Sowllen glands in the neck")
            speak("Fatigue (extereme tiredness)")
            print("Glandular fever is a type of viral infection that mostly affects young adults.")
            print("It is also known as infectious mononucleosis, or mono.")
            print("Common symptoms include:")
            print("A high temperature (fever)")
            print("A severely sore throat")
            print("Sowllen glands in the neck")
            print("Fatigue (extereme tiredness)")

        elif 'gum disease' in query or 'red gums' in query or 'sowllen gums' in query or 'paining gums' in query or 'gums' in query:
            speak("Periodontitis (per-e-o-don-TIE-tis), also called gum disease, is a serious gum infection that damages the soft tissue and, without treatment, can destroy the bone that supports your teeth.")
            speak("Periodontitis can cause teeth to loosen or lead to tooth loss.")
            speak("Healthy gums are firm and pale pink and fit snugly around teeth. Signs and symptoms of periodontitis can include are:")
            speak("Swollen or puffy gums")
            speak("Bright red, dusky red or purplish gums")
            speak("Gums that feel tender when touched")
            speak("Gums that bleed easily")
            speak("Pink-tinged toothbrush after brushing")
            speak("Spitting out blood when brushing or flossing your teeth")
            speak("Pus between your teeth and gums")
            speak("Gums that pull away from your teeth (recede), making your teeth look longer than normal")
            print("Periodontitis (per-e-o-don-TIE-tis), also called gum disease, is a serious gum infection that damages the soft tissue and, without treatment, can destroy the bone that supports your teeth.")
            print("Periodontitis can cause teeth to loosen or lead to tooth loss.")
            print("Healthy gums are firm and pale pink and fit snugly around teeth. Signs and symptoms of periodontitis can include are:")
            print("Swollen or puffy gums")
            print("Bright red, dusky red or purplish gums")
            print("Gums that feel tender when touched")
            print("Gums that bleed easily")
            print("Pink-tinged toothbrush after brushing")
            print("Spitting out blood when brushing or flossing your teeth")
            print("Pus between your teeth and gums")
            print("Gums that pull away from your teeth (recede), making your teeth look longer than normal")

        elif 'haemorrhoids' in query or 'piles' in query:
            speak("Haemorrhoids, also known as piles, are swellings containing enlarged blood vessels that are found inside or around the bottom (the rectum and anus).")
            speak("In many cases, haemorrhoids don&#39;t cause symptoms, and some people don&#39;t even realise they have them. However, when symptoms do occur, they may include are:")
            speak("Bleeding after passing a stool (the blood is usually bright red)")
            speak("Itchy bottom")
            speak("A lump hanging down outside of the anus, which may need to be pushed back in after passing a stool")
            speak("A mucus discharge after passing a stool")
            speak("soreness, redness and swelling around your anus")
            print("Haemorrhoids, also known as piles, are swellings containing enlarged blood vessels that are found inside or around the bottom (the rectum and anus).")
            print("In many cases, haemorrhoids don&#39;t cause symptoms, and some people don&#39;t even realise they have them. However, when symptoms do occur, they may include are:")
            print("Bleeding after passing a stool (the blood is usually bright red)")
            print("Itchy bottom")
            print("A lump hanging down outside of the anus, which may need to be pushed back in after passing a stool")
            print("A mucus discharge after passing a stool")
            print("soreness, redness and swelling around your anus")

        elif 'hearing loss' in query or 'loss of hearing ' in query or 'Deaf' in query or 'Hard of hearing' in query or 'total deafness' in query or 'hearing issue' in query:

            speak("Hearing loss is a common problem that often develops with age or is caused by repeated exposure to loud noises.")
            speak("Hearing loss can occur suddenly, but usually develops gradually. General signs of hearing loss can include:")
            speak("difficulty hearing other people clearly and misunderstanding what they say")
            speak("asking people to repeat themselves")
            speak("listening to music or watching television with the volume turned up higher than other people require")
            print("Hearing loss is a common problem that often develops with age or is caused by repeated exposure to loud noises.")
            print("Hearing loss can occur suddenly, but usually develops gradually. General signs of hearing loss can include:")
            print("difficulty hearing other people clearly and misunderstanding what they say")
            print("asking people to repeat themselves")
            print("listening to music or watching television with the volume turned up higher than other people require")

        elif 'heart failure' in query or 'cardiac failure' in query or 'heart inability' in query or 'left sided heart failure' in query or 'right-sided heart failure' in query or 'diastolic heart failure' in query:

            speak("Heart failure is characterized by the heart’s inability to pump an adequate supply of blood to the body. Without sufficient blood flow, all major body functions are disrupted. Heart failure is a condition or a collection of symptoms that weaken your heart.")
            speak("The symptoms of heart failure may include:")
            speak("excessive fatigue")
            speak("sudden weight gain")
            speak("a loss of appetite")
            speak("irregular pulse")
            speak("heart palpitations")
            speak("abdominal swelling")
            speak("shortness of breath")
            speak("leg and ankle swelling")
            speak("protruding neck veins")
            print("Heart failure is characterized by the heart’s inability to pump an adequate supply of blood to the body. Without sufficient blood flow, all major body functions are disrupted. Heart failure is a condition or a collection of symptoms that weaken your heart.")
            print("The symptoms of heart failure may include:")
            print("excessive fatigue")
            print("sudden weight gain")
            print("a loss of appetite")
            print("irregular pulse")
            print("heart palpitations")
            print("abdominal swelling")
            print("shortness of breath")
            print("leg and ankle swelling")
            print("protruding neck veins")


        elif 'high blood cholesterol' in query or 'lipid disorder' in query or 'high blood ' in query or 'high cholesterol' in query or 'cholesterol' in query or 'blood cholesterol' in query:

            speak("Cholesterol is a fatty substance known as a lipid. It vital for the normal functioning of the body. Cell membranes, hormones and vitamin D are created by your body using cholesterol.")
            speak("There are two main sources of the cholesterol in your blood:")
            speak("cholesterol in the food you eat")
            speak("cholesterol produced by your liver")
            speak("The most common symptoms include are:")
            speak("angina, chest pain.")
            speak("nausea.")
            speak("extreme fatigue.")
            speak("shortness of breath.")
            speak("pain in the neck, jaw, upper abdomen, or back.")
            speak("numbness or coldness in your extremities.")
            print("Cholesterol is a fatty substance known as a lipid. It vital for the normal functioning of the body. Cell membranes, hormones and vitamin D are created by your body using cholesterol.")
            print("There are two main sources of the cholesterol in your blood:")
            print("● cholesterol in the food you eat")
            print("● cholesterol produced by your liver")
            print("The most common symptoms include are:")
            print("angina, chest pain.")
            print("nausea.")
            print("extreme fatigue.")
            print("shortness of breath.")
            print("pain in the neck, jaw, upper abdomen, or back.")
            print("numbness or coldness in your extremities.")


        elif 'hyperglycaemia' in query or 'high blood sugar' in query or 'blood sugar high ' in query or 'blood sugar' in query or 'high sugar' in query:
            speak("Hyperglycaemia is the medical term for a high blood sugar (glucose) level. It&#39;s a common problem for people with diabetes.")
            speak("It can affect people with type 1 diabetes and type 2 diabetes, as well as pregnant women with gestational diabetes.")
            speak("Hyperglycaemia shouldn&#39;t be confused with hypoglycaemia, which is when a person&#39;s blood sugar level drops too low.")
            speak("Symptoms of hyperglycaemia include are:")
            speak("increased thirst and a dry mouth")
            speak("needing to pee frequently")
            speak("tiredness")
            speak("blurred vision")
            speak("unintentional weight loss")
            speak("recurrent infections, such as thrush, bladder infections (cystitis) and skin infections")
            print("Hyperglycaemia is the medical term for a high blood sugar (glucose) level. It&#39;s a common problem for people with diabetes.")
            print("It can affect people with type 1 diabetes and type 2 diabetes, as well as pregnant women with gestational diabetes.")
            print("Hyperglycaemia shouldn&#39;t be confused with hypoglycaemia, which is when a person&#39;s blood sugar level drops too low.")
            print("Symptoms of hyperglycaemia include are:")
            print("increased thirst and a dry mouth")
            print("needing to pee frequently")
            print("tiredness")
            print("blurred vision")
            print("unintentional weight loss")
            print("recurrent infections, such as thrush, bladder infections (cystitis) and skin infections")

        elif 'hypoglycaemia' in query or 'low blood sugar' in query or 'low blood ' in query or 'blood sugar low' in query or 'low sugar' in query:
            speak("Hypoglycaemia, or a &quot;hypo&quot;, is an abnormally low level of glucose in your blood (less than four millimoles per litre).")
            speak("When your glucose (sugar) level is too low, your body doesn&#39;t have enough energy to carry out its activities.")
            speak("Hypoglycaemia is most commonly associated with diabetes, and mainly occurs if someone with diabetes takes too much insulin, misses a meal or exercises too hard.")
            speak("Signs and symptoms of hypoglycaemia can include are:")
            speak("feeling hungry")
            speak("sweating")
            speak("dizziness")
            speak("tiredness (fatigue)")
            speak("blurred vision")
            speak("trembling or shakiness")
            speak("going pale")
            speak("fast pulse or palpitations")
            speak("tingling lips")
            speak("irritability")
            speak("difficulty concentrating")
            speak("confusion")
            speak("disorderly or irrational behaviour, which may be mistaken for drunkenness")
            print("Hypoglycaemia, or a &quot;hypo&quot;, is an abnormally low level of glucose in your blood (less than four millimoles per litre).")
            print("When your glucose (sugar) level is too low, your body doesn&#39;t have enough energy to carry out its activities.")
            print("Hypoglycaemia is most commonly associated with diabetes, and mainly occurs if someone with diabetes takes too much insulin, misses a meal or exercises too hard.")
            print("Signs and symptoms of hypoglycaemia can include are:")
            print("feeling hungry")
            print("sweating")
            print("dizziness")
            print("tiredness (fatigue)")
            print("blurred vision")
            print("trembling or shakiness")
            print("going pale")
            print("fast pulse or palpitations")
            print("tingling lips")
            print("irritability")
            print("difficulty concentrating")
            print("confusion")
            print("disorderly or irrational behaviour, which may be mistaken for drunkenness")

        elif 'ingrown toenail' in query or 'ingrown nail' in query or 'ingrown toenails' in query or 'overgrown nail' in query or 'red nail' in query or 'swollen nail' in query:
            speak("An ingrown toenail develops when the sides of the toenail grow into the surrounding skin.")
            speak("The big toe is often affected, either on one or both sides.")
            speak("The nail curls and pierces the skin, which becomes red, swollen and tender.")
            speak("Other possible symptoms include are:")
            speak("pain if pressure is placed on the toe")
            speak("inflammation of the skin at the end of the toe")
            speak("a build-up of fluid (oedema) in the area surrounding the toe")
            speak("an overgrowth of skin around the affected toe (hypertrophy)")
            speak("bleeding")
            speak("white or yellow pus coming from the affected area")
            print("An ingrown toenail develops when the sides of the toenail grow into the surrounding skin.")
            print("The big toe is often affected, either on one or both sides.")
            print("The nail curls and pierces the skin, which becomes red, swollen and tender.")
            print("Other possible symptoms include are:")
            print("pain if pressure is placed on the toe")
            print("inflammation of the skin at the end of the toe")
            print("a build-up of fluid (oedema) in the area surrounding the toe")
            print("an overgrowth of skin around the affected toe (hypertrophy)")
            print("bleeding")
            print("white or yellow pus coming from the affected area")

        elif 'iron deficiency' in query or 'insufficient iron' in query or 'iron deficiency anemia' in query or 'iron deficiency anaemia' in query:
            speak("Iron deficiency anaemia is a condition where a lack of iron in the body leads to a reduction in the number of red blood cells.")
            speak("Iron is used to produce red blood cells, which help store and carry oxygen in the blood. If you have fewer red blood cells than is normal, your organs and tissues won&#39;t get as much oxygen as they usually would.")
            speak("There are several different types of anaemia, and each one has a different cause. Iron deficiency anaemia is the most common type.")
            speak("The most common symptoms include are:")
            speak("tiredness and lack of energy (lethargy)")
            speak("shortness of breath")
            speak("noticeable heartbeats (heart palpitations)")
            speak("a pale complexion")
            print("Iron deficiency anaemia is a condition where a lack of iron in the body leads to a reduction in the number of red blood cells.")
            print("Iron is used to produce red blood cells, which help store and carry oxygen in the blood. If you have fewer red blood cells than is normal, your organs and tissues won&#39;t get as much oxygen as they usually would.")
            print("There are several different types of anaemia, and each one has a different cause. Iron deficiency anaemia is the most common type.")
            print("The most common symptoms include are:")
            print("tiredness and lack of energy (lethargy)")
            print("shortness of breath")
            print("noticeable heartbeats (heart palpitations)")
            print("a pale complexion")

        elif 'irritable bowel syndrome' in query or 'ibs' in query or 'spastic colon' in query or 'nervous colon' in query or 'mucous colitis' in query or 'spastic bowel' in query:
            speak("Irritable bowel syndrome (IBS) is a common, long-term condition of the digestive system. Symptoms can include stomach cramps, bloating, diarrhoea and/or constipation.")
            speak("IBS is thought to affect up to one in five people at some point in their life, and it usually first develops when a person is between 20 and 30 years of age. Around twice as many women are affected as men.")
            speak("The most common symptoms of IBS are:")
            speak("a change in your bowel habits – such as diarrhoea, constipation or sometimes both")
            speak("bloating and swelling of your stomach")
            speak("excessive wind (flatulence)")
            speak("occasionally experiencing an urgent need to move your bowels")
            print("Irritable bowel syndrome (IBS) is a common, long-term condition of the digestive system. Symptoms can include stomach cramps, bloating, diarrhoea and/or constipation.")
            print("IBS is thought to affect up to one in five people at some point in their life, and it usually first develops when a person is between 20 and 30 years of age. Around twice as many women are affected as men.")
            print("The most common symptoms of IBS are:")
            print("a change in your bowel habits – such as diarrhoea, constipation or sometimes both")
            print("bloating and swelling of your stomach")
            print("excessive wind (flatulence)")
            print("occasionally experiencing an urgent need to move your bowels")

        elif 'indigestion ' in query or 'dyspepsia' in query or 'upset stomach' in query or 'abdominal pain ' in query or 'stomach ache	' in query or 'stomach pain' in query or 'heartburn' in query:
            speak("Indigestion can be pain or discomfort in your upper abdomen (dyspepsia) or burning pain behind the breastbone (heartburn).")
            speak("Dyspepsia and heartburn may occur together or on their own. Symptoms usually appear soon after eating or drinking.")
            speak("Common associated symptoms include:")
            speak("feeling full or bloated")
            speak("feeling sick (nausea)")
            speak("belching")
            speak("bringing up (regurgitating) fluid or food into the gullet (oesophagus)")
            print("Indigestion can be pain or discomfort in your upper abdomen (dyspepsia) or burning pain behind the breastbone (heartburn).")
            print("Dyspepsia and heartburn may occur together or on their own. Symptoms usually appear soon after eating or drinking.")
            print("Common associated symptoms include:")
            print("feeling full or bloated")
            print("feeling sick (nausea)")
            print("belching")
            print("bringing up (regurgitating) fluid or food into the gullet (oesophagus)")

        elif 'sleep disorder' in query or 'insomnia ' in query or 'staying asleep' in query or 'sleeplessness' in query or 'wakefulness' in query or 'indisposition' in query:
            speak("Insomnia is difficulty getting to sleep or staying asleep for long enough to feel refreshed the next morning.")
            speak("If you have insomnia, you may:")
            speak("find it difficult to fall asleep")
            speak("lie awake for long periods at night")
            speak("wake up several times during the night")
            speak("wake up early in the morning and not be able to get back to sleep")
            speak("not feel refreshed when you get up")
            speak("find it hard to nap during the day, despite feeling tired")
            speak("feel tired and irritable during the day and have difficulty concentrating")
            print("If you have insomnia, you may:")
            print("find it difficult to fall asleep")
            print("lie awake for long periods at night")
            print("wake up several times during the night")
            print("wake up early in the morning and not be able to get back to sleep")
            print("not feel refreshed when you get up")
            print("find it hard to nap during the day, despite feeling tired")
            print("feel tired and irritable during the day and have difficulty concentrating")

        elif 'kidney infection' in query or 'bladder infection' in query or 'lower urinary tract infection' in query or 'urinary tract infection' in query:
            speak("A kidney infection (pyelonephritis) is a painful and unpleasant illness caused by bacteria travelling from your bladder into one or both of your kidneys.")
            speak("It's more serious than cystitis, a common infection of the bladder that makes urinating painful.")
            speak("If treated promptly, a kidney infection doesn&#39;t cause serious harm, but will make you feel very unwell. If a kidney infection isn&#39;t treated, it can get worse and cause permanent kidney damage.")
            speak("Common symptoms include are:")
            speak("pain and discomfort in your side, lower back or around your genitals")
            speak("high temperature (it may reach 39.5C or 103.1F)")
            speak("shivering or chills")
            speak("feeling very weak or tired")
            speak("loss of appetite")
            speak("feeling sick or being sick")
            speak("diarrhoea")
            print("A kidney infection (pyelonephritis) is a painful and unpleasant illness caused by bacteria travelling from your bladder into one or both of your kidneys.")
            print("It's more serious than cystitis, a common infection of the bladder that makes urinating painful.")
            print("If treated promptly, a kidney infection doesn&#39;t cause serious harm, but will make you feel very unwell. If a kidney infection isn&#39;t treated, it can get worse and cause permanent kidney damage.")
            print("Common symptoms include are:")
            print("pain and discomfort in your side, lower back or around your genitals")
            print("high temperature (it may reach 39.5C or 103.1F)")
            print("shivering or chills")
            print("feeling very weak or tired")
            print("loss of appetite")
            print("feeling sick or being sick")
            print("diarrhoea")

        elif 'kidney stone' in query or 'urinary stones' in query or 'urinary calculus' in query or 'calculus' in query or 'kidney' in query:
            speak("Kidney stones can develop in one or both kidneys and most often affect people aged 30 to 60.")
            speak("They're quite common, with around three in 20 men and up to two in 20 women developing them at some stage of their lives.")
            speak("The medical term for kidney stones is nephrolithiasis, and if they cause severe pain it's known as renal colic.")
            speak("Different Symptoms are:")
            speak("Pain in the back, belly, or side")
            speak("Pain or burning during urination")
            speak("Blood in the urine")
            speak("Nausea and vomiting")
            speak("Cloudy or smelly urine")
            print("Kidney stones can develop in one or both kidneys and most often affect people aged 30 to 60.")
            print("They're quite common, with around three in 20 men and up to two in 20 women developing them at some stage of their lives.")
            print("The medical term for kidney stones is nephrolithiasis, and if they cause severe pain it's known as renal colic.")
            print("Different Symptoms are:")
            print("Pain in the back, belly, or side")
            print("Pain or burning during urination")
            print("Blood in the urine")
            print("Nausea and vomiting")
            print("Cloudy or smelly urine")


        elif ' skin ' in query and ' crust ' in query and ' sores ' in query and ' rashes ' in query and ' itching ' in query:
            speak("There ia a possibility that you have Scabies")
            speak(" Scabies is an itchy skin condition caused by a tiny burrowing mite called Sarcoptes scabiei. Intense itching occurs in the area where the mite burrows.+C1:C7 The urge to scratch may be especially strong at night. ")
            print("There ia a possibility that you have Scabies")
            print(" Scabies is an itchy skin condition caused by a tiny burrowing mite called Sarcoptes scabiei. Intense itching occurs in the area where the mite burrows. The urge to scratch may be especially strong at night. ")

        elif ' fever ' in query and ' skin rash ' in query and ' sore throat'in query:
            speak("There ia a possibility that you have scarlet fever ")
            speak("Scarlet fever affects a small number of people who have strep throat or streptococcal skin infections. The bacteria are usually spread by people coughing or sneezing. ")
            print("There ia a possibility that you have scarlet fever ")
            print("Scarlet fever affects a small number of people who have strep throat or streptococcal skin infections. The bacteria are usually spread by people coughing or sneezing. ")

        elif ' swelling ' in query and ' vision ' in query and ' infection '   in query and ' anemia ' in query:
            speak("There ia a possibility that you have sickle cell disease")
            speak(" Sickle cell disease (SCD) is a group of blood disorders typically inherited from a person's parents. ")
            print("There ia a possibility that you have sickle cell disease")
            print(" Sickle cell disease (SCD) is a group of blood disorders typically inherited from a person's parents. ")

        elif ' stomach ' in query or ' bloating ' in query and ' vomiting ' in query or 'diarrhea ' in query or ' nausea ' in query and ' pain ' in query and ' heartburn 'in query:
            speak("There ia a possibility that you have stomach cancer")
            speak(" Stomach cancer, also known as gastric cancer, is a cancer that develops from the lining of the stomach. ")
            print("There ia a possibility that you have stomach cancer")
            print(" Stomach cancer, also known as gastric cancer, is a cancer that develops from the lining of the stomach. ")

        elif ' brain ' in query and ' strength ' in query and ' loss of vision ' in query and ' loss of balance ' in query and ' headache ' in query:
            speak("There ia a possibility that you have stroke")
            speak(" A stroke is a medical condition in which poor blood flow to the brain causes cell death.")
            print("There ia a possibility that you have stroke")
            print(" A stroke is a medical condition in which poor blood flow to the brain causes cell death.")

        elif ' skin ' in query and ' swelling ' in query and ' redness ' in query or ' tenderness ' in query and ' rashes ' in query:
            speak("There ia a possibility that you have sunburn")
            speak(" A sunburn is a kind of burn that happens when skin is exposed to sunlight for too long. ")
            print("There ia a possibility that you have sunburn")
            print(" A sunburn is a kind of burn that happens when skin is exposed to sunlight for too long. ")

        elif ' nose ' in query and 'cough  ' in query and ' fever ' in query and ' red ' in query and ' runny nose ' in query:
            speak("There ia a possibility that you have whooping cough")
            speak(" Whooping cough, also known as pertussis or the 100-day cough, is a highly contagious bacterial disease.")
            print("There ia a possibility that you have whooping cough")
            print(" Whooping cough, also known as pertussis or the 100-day cough, is a highly contagious bacterial disease.")

        elif ' kidney ' in query and ' constipation ' in query and ' shortness of breath ' in query and ' loss of appetite. ' in query and ' vomiting '  in query or ' nausea '  in query and ' blood '  in query and ' fever. ' in query:
            speak("There ia a possibility that you have Wilms’ tumour")
            speak(" Wilms' tumor is a rare kidney cancer that primarily affects children. Also known as nephroblastoma, it's the most common cancer of the kidneys in children. ")
            print("There ia a possibility that you have Wilms’ tumour")
            print(" Wilms' tumor is a rare kidney cancer that primarily affects children. Also known as nephroblastoma, it's the most common cancer of the kidneys in children. ")

        elif ' fever ' in query and ' muscle pain ' in query or ' backache ' in query and ' headache '  in query:
            speak("There ia a possibility that you have Yellow fever")
            speak(" The disease is caused by yellow fever virus and is spread by the bite of an infected female mosquito.")
            print("There ia a possibility that you have Yellow fever")
            print(" The disease is caused by yellow fever virus and is spread by the bite of an infected female mosquito.")

        elif 'breast' in query and 'nipple' in query and 'burning' in query and 'itching' in query and 'bleeding' in query and 'rash' in query and 'eczema' in query:
            speak("There is a possibility you have Paget's disease.")
            speak("Paget's disease usually affects the skin of one nipple and produces eczema-like symptoms, appearing as an itchy, red rash on the nipple that can extend to the areola.")
            speak("Paget's disease is usually a sign of breast cancer in tissue behind the nipple, or breast tissue away from the nipple.")
            print("There is a possibility you have Paget's disease.")
            print("Paget's disease usually affects the skin of one nipple and produces eczema-like symptoms, appearing as an itchy, red rash on the nipple that can extend to the areola.")
            print("Paget's disease is usually a sign of breast cancer in tissue behind the nipple, or breast tissue away from the nipple.")

        elif 'brain' in query and 'damage' and 'depression' in query or 'anxiety' in query and 'balance problem' in query and 'loss smell' in query and 'insomnia' in query and 'memory problem' in query:
            speak("There is a possibility you have Parkinson's disease.")
            speak("Parkinson's disease is a condition in which parts of the brain become progressively damaged over many years.")
            speak("Parkinson's disease is caused by a loss of nerve cells in part of the brain called the substantia nigra. This leads to a reduction in a chemical called dopamine in the brain.")
            print("There is a possibility you have Parkinson's disease.")
            print("Parkinson's disease is a condition in which parts of the brain become progressively damaged over many years.")
            print("Parkinson's disease is caused by a loss of nerve cells in part of the brain called the substantia nigra. This leads to a reduction in a chemical called dopamine in the brain.")

        elif 'penis' in query and 'skin' in query and 'growth' in query or 'sore' in query and 'blood' in query and 'foul discharge' in query and 'thick' in query and 'change colour' in query and 'rashes' in query:
            speak("There is a possibility you have penile cancer.")
            speak("Penile cancer is a rare type of cancer that occurs on the skin of the penis or within the penis.")
            speak("Men who carry the human papilloma virus (HPV) have an increased risk of developing penile cancer, which is the virus that causes genital warts.")
            print("There is a possibility you have penile cancer.")
            print("Penile cancer is a rare type of cancer that occurs on the skin of the penis or within the penis.")
            print("Men who carry the human papilloma virus (HPV) have an increased risk of developing penile cancer, which is the virus that causes genital warts.")

        elif 'personality' in query and 'negative feeling' in query and 'worthless' in query and 'feeling empty' in query and 'emotionally disconnected' in query and 'odd behaviour' in query and 'losing reality' in query:
            speak("There is a possibility you have personality disorder.")
            speak("Personality disorders are conditions in which an individual differs significantly from an average person, in terms of how they think, perceive, feel or relate to others.")
            speak("Changes in how a person feels and distorted beliefs about other people can lead to odd behaviour, which can be distressing and may upset others.")
            print("There is a possibility you have personality disorder.")
            print("Personality disorders are conditions in which an individual differs significantly from an average person, in terms of how they think, perceive, feel or relate to others.")
            print("Changes in how a person feels and distorted beliefs about other people can lead to odd behaviour, which can be distressing and may upset others.")

        elif 'event' in query and 'stress' in query and 'frightening' in query and 'distress' in query and 'assault' in query or 'abuse' in query and 'sexual' in query and 'violent death' in query and 'hostage' in query and 'terrorist attack' in query:
            speak("There is a possibility you have Post-traumatic stress disorder.")
            speak("Post-traumatic stress disorder (PTSD) is an anxiety disorder caused by very stressful, frightening or distressing events.")
            speak("Someone with PTSD often relives the traumatic event through nightmares and flashbacks, and may experience feelings of isolation, irritability and guilt.")
            print("There is a possibility you have Post-traumatic stress disorder.")
            print("Post-traumatic stress disorder (PTSD) is an anxiety disorder caused by very stressful, frightening or distressing events.")
            print("Someone with PTSD often relives the traumatic event through nightmares and flashbacks, and may experience feelings of isolation, irritability and guilt.")

        elif 'prostate' in query and 'large' in query and 'straining while urinate' in query and 'bladder not empty' in query:
            speak("There is a possibility that you have prostate cancer.")
            speak("Prostate cancer is the most common cancer in men in the UK, with over 40,000 new cases diagnosed every year.")
            speak("Symptoms often only become apparent when your prostate is large enough to affect the urethra (the tube that carries urine from the bladder to the penis).")
            print("There is a possibility that you have prostate cancer.")
            print("Prostate cancer is the most common cancer in men in the UK, with over 40,000 new cases diagnosed every year.")
            print("Symptoms often only become apparent when your prostate is large enough to affect the urethra (the tube that carries urine from the bladder to the penis).")


        elif 'testicle' in query and 'swelling' in query or 'lump' in query and 'pain' in query and 'scrotum' in query and 'heaviness' in query:
            speak("There is a possibility you have testicular cancer.")
            speak("Cancer of the testicle is one of the less common cancers and tends to mostly affect men between 15 and 49 years of age.")
            speak("Testicular cancer is a relatively rare type of cancer, accounting for just 1% of all cancers that occur in men.")
            print("There is a possibility you have testicular cancer.")
            print("Cancer of the testicle is one of the less common cancers and tends to mostly affect men between 15 and 49 years of age.")
            print("Testicular cancer is a relatively rare type of cancer, accounting for just 1% of all cancers that occur in men.")

        elif 'large intestine' in query and 'worm' in query and 'anus' in query or 'vagina' in query and 'itching' in query:
            speak("There is a possibility you have threadworms.")
            speak("Threadworms often go unnoticed by people who have them,However, they can cause intense itching around the anus (and the vagina in girls), particularly at night.")
            speak("In some cases, you may spot threadworms on your bed clothes or sheets at night, or you may notice them in your stools.")
            print("There is a possibility you have threadworms.")
            print("Threadworms often go unnoticed by people who have them,However, they can cause intense itching around the anus and the vagina in girls, particularly at night.")
            print("In some cases, you may spot threadworms on your bed clothes or sheets at night, or you may notice them in your stools.")

        elif 'penis' in query and 'fungus' in query and 'irritation' in query or 'burning' in query and 'redness' in query or 'patch' in query and 'discharge' in query and 'skin' in query:
            speak("There is a possibility you have thrush.")
            speak("Thrush is a yeast infection caused by a fungus called Candida albicans. Both men and women can get thrush, though it is more often associated with women.")
            speak("In men, it usually affects the head of the penis – causing irritation, discharge and redness.")
            print("There is a possibility you have thrush.")
            print("Thrush is a yeast infection caused by a fungus called Candida albicans. Both men and women can get thrush, though it is more often associated with women.")
            print("In men, it usually affects the head of the penis – causing irritation, discharge and redness.")

        elif 'thyroid gland' in query and 'neck' in query and 'swelling' in query or 'lump' in query and 'sore throat' in query or 'swallowing' in query:
            speak("There is a possibility you have thyroid cancer.")
            speak("Thyroid cancer is a rare type of cancer that affects the thyroid gland, a small gland at the base of the neck.")
            speak("It's important to remember that if you have a lump in your thyroid gland, it doesn't necessarily mean you have thyroid cancer.")
            print("There is a possibility you have thyroid cancer.")
            print("Thyroid cancer is a rare type of cancer that affects the thyroid gland, a small gland at the base of the neck.")
            print("It's important to remember that if you have a lump in your thyroid gland, it doesn't necessarily mean you have thyroid cancer.")

        elif 'body' in query and 'ear' in query and 'sound' in query and 'ringing' in query and 'buzzing' in query and 'humming' in query and 'grinding' in query and 'hissing' in query and 'whistling' in query:
            speak("There is a possibility you have tinnitus.")
            speak("Tinnitus is the term for hearing sounds that come from inside your body, rather than from an outside source.")
            speak("Most people have experienced short periods of tinnitus after being exposed to loud noises, such as after a music concert.")
            print("There is a possibility you have tinnitus.")
            print("Tinnitus is the term for hearing sounds that come from inside your body, rather than from an outside source.")
            print("Most people have experienced short periods of tinnitus after being exposed to loud noises, such as after a music concert.")

        elif 'tonsil' in query and 'sore throat' in query and 'earache' in query and 'fever' in query and 'cough' in query and 'headache' in query and 'common cold' in query and 'influenza' in query:
            speak("There is a possibility you have tonsillitis.")
            speak("Tonsillitis is inflammation of the tonsils. It's usually caused by a viral infection or, less commonly, a bacterial infection.")
            speak("Most cases of tonsillitis are caused by a viral infection, such as the viruses that cause the common cold or flu virus influenza.")
            print("There is a possibility you have tonsillitis.")
            print("Tonsillitis is inflammation of the tonsils. It's usually caused by a viral infection or, less commonly, a bacterial infection.")
            print("Most cases of tonsillitis are caused by a viral infection, such as the viruses that cause the common cold or flu virus influenza.")

        elif 'tooth' in query and 'pain' in query or 'ache' in query and 'tenderness' in query and 'spot' in query and 'bad breath' in query:
            speak("There is a possibility your tooth might decay.")
            speak("Tooth decay can occur when acid is produced from plaque, which builds up on your teeth.")
            speak("Although tooth decay is a common problem, it's often entirely preventable. The best way to avoid tooth decay is to keep your teeth and gums as healthy as possible.")
            print("There is a possibility your tooth might decay")
            print("Tooth decay can occur when acid is produced from plaque, which builds up on your teeth.")
            print("Although tooth decay is a common problem, it's often entirely preventable. The best way to avoid tooth decay is to keep your teeth and gums as healthy as possible.")

        elif 'lung' in query and 'inhalation' in query and 'cough' in query and 'sneeze' in query and 'weight loss' in query and 'night sweat' in query and 'fever' in query and 'tiredness' in query or 'fatigue' in query and 'swelling' in query:
            speak("There is a possibility you have tuberculosis.")
            speak("Tuberculosis is a bacterial infection spread through inhaling tiny droplets from the coughs or sneezes of an infected person.")
            speak("TB mainly affects the lungs. However, it can affect any part of the body, including the glands, bones and nervous system.")
            print("There is a possibility you have tuberculosis.")
            print("Tuberculosis is a bacterial infection spread through inhaling tiny droplets from the coughs or sneezes of an infected person.")
            print("TB mainly affects the lungs. However, it can affect any part of the body, including the glands, bones and nervous system.")

        elif 'sugar' in query and 'high' in query and 'thirst' in query and 'urine' in query and 'tired' in query and 'weight loss' in query or 'muscle bulk' in query and 'thrush' in query and 'blurred vision' in query:
            speak("There is a possibility you have type 2 diabetes.")
            speak("Diabetes is usually a lifelong condition that causes a person's blood glucose sugar level to become too high.")
            speak("Type 2 diabetes occurs when the body doesn't produce enough insulin to function properly, or the body's cells don't react to insulin.")
            print("There is a possibility you have type 2 diabetes.")
            print("Diabetes is usually a lifelong condition that causes a person's blood glucose sugar level to become too high.")
            print("Type 2 diabetes occurs when the body doesn't produce enough insulin to function properly, or the body's cells don't react to insulin.")

        elif 'mosquito' in query and 'bite' in query and 'fever' in query and 'sweat' in query or 'chills' in query and 'headache' in query and 'muscle pain' in query and 'vomit' in query and 'diarrhoea' in query:
            speak("There is a possibility you have malaria.")
            speak("Malaria is a serious tropical disease spread by mosquitoes. If it isn't diagnosed and treated properly it can be fatal.")
            speak("A single mosquito bite is all it takes for someone to be infected.")
            print("There is a possibility you have malaria.")
            print("Malaria is a serious tropical disease spread by mosquitoes. If it isn't diagnosed and treated properly it can be fatal.")
            print("A single mosquito bite is all it takes for someone to be infected.")

        elif 'brain' in query and 'tumour' in query and 'persistent' in query and 'headache' in query and 'seizure' in query and 'nausea' in query and 'vomit' in query and 'drowsiness' in query and 'change' in query and 'mental' in query or 'behavioural' in query and 'weakness' in query or 'paralysis one side' in query:
            speak("There is a possibility you have malignant brain tumor.")
            speak("A malignant brain tumor is a fast growing cancer that spreads to the other areas of the brain and spine.")
            speak("Brain tumours can affect people of any age including children, although they tend to be more common in adults.")
            print("There is a possibility you have malignant brain tumor.")
            print("A malignant brain tumor is a fast growing cancer that spreads to the other areas of the brain and spine.")
            print("Brain tumours can affect people of any age including children, although they tend to be more common in adults.")

        elif 'diet' in query and 'poor' in query or 'nutrients' in query and 'amount' in query or 'weak muscle' in query or 'tired' in query :
            speak("There is a possibility you have malnutrition.")
            speak("Malnutrition is a serious condition that occurs when a person's diet doesn't conatin the right amount of nutrients.")
            speak("Malnutrition is caused by having an inadequate diet or a problem absorbing nutrients from food. There are many reasons why these might happen,including having reduced mobility, a long-term health condition, or a low income.")
            print("There is a possibility you have malnutrition.")
            print("Malnutrition is a serious condition that occurs when a person's diet doesn't conatin the right amount of nutrients.")
            print("Malnutrition is caused by having an inadequate diet or a problem absorbing nutrients from food. There are many reasons why these might happen,including having reduced mobility, a long-term health condition, or a low income.")

        elif 'respiratory tract' in query and 'viral' in query and 'fever' in query and 'runny nose' in query and 'cough' in query or 'sneze' in query and 'red eye' in query and 'grey' in query and 'white' in query and 'spot' in query and 'cheek' in query:
            speak("There is a possibility you have Measles.")
            speak("Measles is a highly infectious viral illness that can be very unpleasant and sometimes lead to serious complications.")
            speak("Measles can be unpleasant but will usually pass in about 7 to 10 days without causing any further problems.")
            print("There is a possibility you have Measles.")
            print("Measles is a highly infectious viral illness that can be very unpleasant and sometimes lead to serious complications.")
            print("Measles can be unpleasant but will usually pass in about 7 to 10 days without causing any further problems.")

        elif 'brain' in query and 'membrane' in query and 'fever' in query or 'sick' in query and 'headache' in query and ' blotchy rash' in query and 'stiff neck' in query and 'bright light' in query and 'drowsiness' in query or 'unresponsiveness' in query and 'seizure' in query or 'fits' in query:
            speak("There is a possibility you have Meningitis.")
            speak("Meningtis is an infection of the protective membranes that surround the brain and the spinal cord.")
            speak("It can affect anyone,but is most common in babies, young children, teenagers and young adults.")
            print("There is a possibility you have Meningitis.")
            print("Meningtis is an infection of the protective membranes that surround the brain and the spinal cord.")
            print("It can affect anyone,but is most common in babies, young children, teenagers and young adults.")

        elif 'woman' in query and 'period' in query and 'stop' in query or 'no' in query and 'hot flush' in query and 'night sweat' in query and 'dry vagina' in query and 'difficult sleep' in query and 'low mood' in query or 'anxiety' in query:
            speak("There is a possibility you have Menopause.")
            speak("The Menopause is when a woman stops having periods and is no longer able to get pregnant naturally.")
            speak("The Menopause is a natural part of ageing that usually occurs between 45 and 55 years of age, as a woman's oestrogen levels decline.")
            print("There is a possibility you have Menopause.")
            print("The Menopause is when a woman stops having periods and is no longer able to get pregnant naturally.")
            print("The Menopause is a natural part of ageing that usually occurs between 45 and 55 years of age, as a woman's oestrogen levels decline.")

        elif 'lung' in query and 'stomach' in query and 'line' in query and 'chest pain' in query and 'shortness of breath' and 'fatigue' in query and 'fever' in query and 'cough' in query and 'weight loss' in query and 'swollen fingertip' in query:
            speak("There is a possibility you have mesothelioma.")
            speak("Mesothelioma is a type of cancer that develops in the lining that covers the outer surface of some of the body's organs.")
            speak("Mesothelioma mainly affects the lining of the lungs ,although it can also affect the lining of the stomach, heart or testicles")
            print("There is a possibility you have mesothelioma.")
            print("Mesothelioma is a type of cancer that develops in the lining that covers the outer surface of some of the body's organs.")
            print("Mesothelioma mainly affects the lining of the lungs ,although it can also affect the lining of the stomach, heart or testicles")

        elif 'head' in query and 'pain' in query and 'one side' in query and 'ache' in query and 'tiredness' in query and 'stress' in query and 'nausea' in query and 'vomit' in query:
            speak("There is a possibility you have migraine.")
            speak("Migraine is usually a moderate or severe headache felt as a throbbing pain on one side of the head.")
            speak("Migraine is a common health condition affecting one in every five women and around one in every fifteen men. They usually begin in early adulthood")
            print("There is a possibility you have migraine.")
            print("Migraine is usually a moderate or severe headache felt as a throbbing pain on one side of the head.")
            print("Migraine is a common health condition affecting one in every five women and around one in every fifteen men. They usually begin in early adulthood")

        elif 'woman' in query and 'baby' in query and 'loss' and 'vagina' in query or 'blood' in query and 'cramping pain' in query and 'waters break' in query and 'change movement' in query:
            speak("There is a possibility you have miscarriage.")
            speak("A miscarriage is the loss of your baby before 24 weeks. Early miscarriages happen in the first 12 weeks of pregnancy.")
            speak("About 1 out of 5 pregnancies miscarry. Since many miscarriages aren't recorded the figure might be higher.")
            print("There is a possibility you have miscarriage.")
            print("A miscarriage is the loss of your baby before 24 weeks. Early miscarriages happen in the first 12 weeks of pregnancy")
            print("About 1 out of 5 pregnancies miscarry. Since many miscarriages aren't recorded the figure might be higher.")

        elif 'muscle' in query and 'weak' in query and 'shoulder' in query or 'grip' in query and 'ankle' in query and 'slurr speech' in query:
            speak("There is a possibility you have motor neurone disease.")
            speak("Motor neurone disease is a rare condition that progressively damages part of the nervous system. This leads to muscle weakness, often with visible wasting.")
            speak("It occurs when specialist nerve cells in the brain and spinal cord motor neurons stop working properly.")
            print("There is a possibility you have motor neurone disease.")
            print("Motor neurone disease is a rare condition that progressively damages part of the nervous system. This leads to muscle weakness, often with visible wasting.")
            print("It occurs when specialist nerve cells in the brain and spinal cord motor neurons stop working properly.")

        elif 'mouth' in query and 'tongue' in query and 'patch' in query and 'red' in query or 'white' in query and 'lining' in query and 'ulcer' in query and 'lump' in query or 'growth' in query:
            speak("There is a possibility you have Mouth cancer.")
            speak("Mouth cancer, also known as oral cancer, is where a tumour develops on the surface of the tongue, mouth, lips or gums.")
            speak("Mouth cancer occurs when something goes wrong with the normal cell lifecycle, causing them to grow and reproduce uncontrollably.")
            print("There is a possibility you have Mouth cancer.")
            print("Mouth cancer, also known as oral cancer, is where a tumour develops on the surface of the tongue, mouth, lips or gums.")
            print("Mouth cancer occurs when something goes wrong with the normal cell lifecycle, causing them to grow and reproduce uncontrollably.")

        elif 'mouth' in query and 'sore' in query and 'bump' in query or 'lesion' in query and 'ulcer' in query:
            speak("There is a possibility you have Mouth ulcer.")
            speak("Mouth ulcers are painful sores that appear in the mouth. Although they're uncomfortable, they’re usually harmless and most clear up by themselves within a week or two.")
            speak("Mouth ulcers can be painful, which can make it uncomfortable to eat, drink or brush your teeth.")
            print("There is a possibility you have Mouth ulcer.")
            print("Mouth ulcers are painful sores that appear in the mouth. Although they're uncomfortable, they’re usually harmless and most clear up by themselves within a week or two.")
            print("Mouth ulcers can be painful, which can make it uncomfortable to eat, drink or brush your teeth.")

        elif 'bone' in query and 'marrow' in query and 'weak' in query and 'persistent ache' in query or 'tenderness' in query and 'tiredness' in query or 'anaemia' in query and 'repeated infection' in query and 'bruising' in query or 'blood' in query:
            speak("There is a possibility you have multiple myeloma.")
            speak("Myeloma does not usually take the form of a lump or tumour. Instead, the myeloma cells divide and expand within the bone marrow, damaging the bones and affecting the production of healthy blood cells.")
            speak("adults over 60 – most cases are diagnosed at around the age of 70, and cases affecting people under the age of 40 are rare.")
            print("There is a possibility you have multiple myeloma")
            print("Myeloma does not usually take the form of a lump or tumour. Instead, the myeloma cells divide and expand within the bone marrow, damaging the bones and affecting the production of healthy blood cells.")
            print("adults over 60 – most cases are diagnosed at around the age of 70, and cases affecting people under the age of 40 are rare.")

        elif 'face' in query and 'swelling' in query and 'side' in query and 'ear' in query and 'headache' in query and 'joint pain' in query:
            speak("There is a possibilty you have Mumps.")
            speak("Mumps is a contagious viral infection that used to be common in children before the introduction of the MMR vaccine.")
            speak("Most cases of mumps occur in people between 17 and 34 years of age who have not received 2 doses of the MMR vaccine.")
            print("There is a possibilty you have Mumps.")
            print("Mumps is a contagious viral infection that used to be common in children before the introduction of the MMR vaccine.")
            print("Most cases of mumps occur in people between 17 and 34 years of age who have not received 2 doses of the MMR vaccine.")

        elif 'inner ear' in query and 'vertigo' in query and 'tinnitus' in query and 'hearing loss' in query and 'pressure' in query:
            speak("There is a possibility you have Meniere's disease.")
            speak("Ménière's disease is a rare disorder that affects the inner ear. It can cause vertigo, tinnitus, hearing loss, and a feeling of pressure deep inside the ear.")
            speak("Ménière's disease most commonly affects people aged 20-60 and it's thought to be slightly more common in women than men.")
            print("There is a possibility you have Meniere's disease.")
            print("Ménière's disease is a rare disorder that affects the inner ear. It can cause vertigo, tinnitus, hearing loss, and a feeling of pressure deep inside the ear.")
            print("Ménière's disease most commonly affects people aged 20-60 and it's thought to be slightly more common in women than men.")

        elif 'ear' in query and 'pain' in query and 'pressure' in query and 'ringing' in query or 'humming' in query and 'fluid' in query or 'pus' in query and 'nausea' in query and 'blurred vision' in query and 'mild headache' in query and 'dizziness' in query and 'hearing loss' in query:
            speak("There is a possibility that you have Labyrinthitis")
            speak("It is a inner ear infection. It causes a delicate structure deep inside your ear called the labyrinth to become inflamed,affecting your hearing and balance")
            speak("You should avoid driving, using tools and machinery, or working at heights if you're feeling dizzy.")
            print("There is a possibility that you have Labyrinthitis")
            print("It is a inner ear infection. It causes a delicate structure deep inside your ear called the labyrinth to become inflamed,affecting your hearing and balance")
            print("You should avoid driving, using tools and machinery, or working at heights if you're feeling dizzy.")

        elif 'stomach' in query or 'bloating' in query and 'wind' in query and 'diarrhoea' in query and 'pain' in query or 'cramp' in query and 'rumbling' in query:
            speak("There is a possibility you have lactose intolerance.")
            speak("It is a common digestive problem where the body is unable to digest lactose, a type of sugar mainly found in milk and dairy products.")
            speak("Lactose Intolerance usually develop within a few hours of consuming food or drink that contains lactose some people may still be able to drink a small glass of milk, while others may not even be able to have milk in their tea or coffee.")
            print("There is a possibility you have lactose intolerance.")
            print("It is a common digestive problem where the body is unable to digest lactose, a type of sugar mainly found in milk and dairy products.")
            print("Lactose Intolerance usually develop within a few hours of consuming food or drink that contains lactose some people may still be able to drink a small glass of milk, while others may not even be able to have milk in their tea or coffee.")

        elif 'throat' in query and 'pain' in query and 'voice' in query and 'change' in query and 'swallowing' in query and 'neck' in query and 'swelling' in query or 'lump' in query and 'breathing' in query or 'difficult' in query:
            speak("There is a possibility you have Laryngeal cancer.")
            speak("Laryngeal cancer mainly affects the voice box,The Larynx is part of the throat found at the entrance of the windpipe. It plays an important role in helping you breathe and speak.")
            speak("The condition is more common in people over the age of 60 It's about four times more common in men than women.")
            print("There is a possibility you have Laryngeal cancer.")
            print("Laryngeal cancer mainly affects the voice box,The Larynx is part of the throat found at the entrance of the windpipe. It plays an important role in helping you breathe and speak.")
            print("The condition is more common in people over the age of 60 It's about four times more common in men than women.")

        elif 'throat' in query or 'hoarse' in query and 'difficulty speaking' in query and 'voice' in query and 'sore' in query and 'cold' in query and 'flu' in query and 'swollen glands' in query:
            speak("There is a possibility you have Laryngitis.")
            speak("The hoarse voice and speaking difficulties usually get worse each day you're ill and may last upto a week.")
            speak("Laryngitis is often linked to another illness such as cold ,flu and throat infection.")
            print("There is a possibility you have Laryngitis")
            print("The hoarse voice and speaking difficulties usually get worse each day you're ill and may last upto a week.")
            print("Laryngitis is often linked to another illness such as cold ,flu and throat infection.")

        elif 'leg' in query and 'cramp' in query and 'pregnancy' in query and 'exercise' in query and 'medication' in query:
            speak("There is a possibility you have leg cramps.")
            speak("Leg cramps are a common and usually harmless condition where the muscles in your leg suddenly become tight and painful.")
            speak("It usually occurs in the calf muscles, although it can affect any part of your leg,including your feet and thighs.")
            print("There is a possibility you have leg cramps.")
            print("Leg cramps are a common and usually harmless condition where the muscles in your leg suddenly become tight and painful.")
            print("It usually occurs in the calf muscles, although it can affect any part of your leg,including your feet and thighs.")

        elif 'body' in query and 'rash' in query and 'arm' in query and 'leg' in query and 'trunk' in query and 'mouth' in query and 'nails' in query or 'scalp' in query and 'vagina' in query or 'vulva' in query and 'penis' in query:
            speak("There is a possibility you have Lichnen Planus.")
            speak("Lichen Planus is a non-infectious, itchy rash that can affect many areas of the body.")
            speak("Lichen Planus is thought to affect 1-2% of the worldwide population. It's more common in adults over the age of 40.")
            print("There is a possibility you have Lichnen Planus.")
            print("Lichen Planus is a non-infectious, itchy rash that can affect many areas of the body.")
            print("Lichen Planus is thought to affect 1-2% of the worldwide population. It's more common in adults over the age of 40.")

        elif 'liver' in query and 'fat' in query and 'top right stomach' in query and 'fatigue' in query and 'weakness' in query and 'pain' in query:
            speak("There is a possibility you have Non-alcoholic fatty liver disease.")
            speak("NAFLD is the term for a range of conditions caused by a build-up of fat in liver.")
            speak("Early stage NAFLD doesn't usually cause any harm, but it can lead to serious liver damage including cirrhosis, if it gets worse.")
            print("There is a possibilty you have Non-alcoholic fatty liver disease.")
            print("NAFLD is the term for a range of conditions caused by a build-up of fat in liver.")
            print("Early stage NAFLD doesn't usually cause any harm, but it can lead to serious liver damage including cirrhosis, if it gets worse.")

        elif 'liver' in query and 'pain' in query and 'weight loss' in query and 'loss appetite' in query and 'sick' in query or 'vomit' in query and 'swelling abdomen' in query and 'jaundice' in query and 'itchy skin' in query and 'week' in query:
            speak("There is a possibility you have liver cancer.")
            speak("Primary Liver Cancer is an uncommon but serious type of cancer that begins in the liver.")
            speak("This is a seprate condition from secondary cancer,which occurs when cancer that first develops in another part of the body spreads to the liver.")
            print("There is a possibility you have liver cancer.")
            print("Primary Liver Cancer is an uncommon but serious type of cancer that begins in the liver.")
            print("This is a seprate condition from secondary cancer,which occurs when cancer that first develops in another part of the body spreads to the liver.")

        elif 'liver' in query and 'lump' in query and 'growth' in query and 'swelling' in query and 'sick' in query and 'weight loss' in query and 'vomit' in query:
            speak("There is a possibility you have a liver tumour.")
            speak("A Liver Tumor is a condition where a lump or growth occurs in the liver.")
            speak("Approximately 10 children in the UK develop primary liver tumours each year. Boys are affected more commonly than girls. Liver tumours can be cancerous or non cancerous.")
            print("There is a possibility you have a liver tumour.")
            print("A Liver Tumor is a condition where a lump or growth occurs in the liver.")
            print("Approximately 10 children in the UK develop primary liver tumours each year. Boys are affected more commonly than girls. Liver tumours can be cancerous or non cancerous.")

        elif 'lung' in query and 'pain' in query and 'persistent' in query and 'cough' in query and 'blood' in query and 'breathlessness' in query and 'tired' in query or 'weight loss' in query and 'breath' in query:
            speak("There is a possibility you have Lung Cancer.")
            speak("Lung Cancer is one of the most common and serious types of cancer. Around 44,500 people are diagnosed with the condition every year in the UK")
            speak("Cancer that begins in the lungs is called primary lung cancer. Cancer that spreads from the lungs to another place in the body is known as secondary lung cancer.")
            print("There is a possibility you have Lung Cancer.")
            print("Lung Cancer is one of the most common and serious types of cancer. Around 44,500 people are diagnosed with the condition every year in the UK")
            print("Cancer that begins in the lungs is called primary lung cancer. Cancer that spreads from the lungs to another place in the body is known as secondary lung cancer.")

        elif 'body' in query and 'tissue' in query and 'swelling' in query and 'leg' in query or 'arm' in query and 'heavy feeling' in query or 'difficult moving' in query:
            speak("There is a possibility that you have Lymphoedema.")
            speak("Lymphoedema is a chronic condition that causes swelling in the body's tissues. It can affect any part of the body,but usually develops in the arms or legs.")
            speak("Lymphoedema can get worse if it's not treated, so you should speak to a doctor if you think you may have the condition.")
            print("There is a possibility that you have Lymphoedema.")
            print("Lymphoedema is a chronic condition that causes swelling in the body's tissues. It can affect any part of the body,but usually develops in the arms or legs.")
            print("Lymphoedema can get worse if it's not treated, so you should speak to a doctor if you think you may have the condition.")

        elif 'nose' in query or 'sinus' in query and 'blocked' in query and 'persitent' in query and 'one side' in query and 'blood' in query and 'mucus' in query and 'smell' in query:
            speak("There is a possibility you have nasal and sinus cancer.")
            speak("Nasal and sinus cancer affects the nasal cavity (the space behind your nose) and the sinuses (small, air-filled cavities inside your nose, cheekbones and forehead).")
            speak("It's a rare type of cancer that most often affects men aged 50-60.")
            print("There is a possibility you have nasal and sinus cancer.")
            print("Nasal and sinus cancer affects the nasal cavity (the space behind your nose) and the sinuses (small, air-filled cavities inside your nose, cheekbones and forehead).")
            print("It's a rare type of cancer that most often affects men aged 50-60.")

        elif 'nerve' in query and 'stomach' in query or 'chest' in query and 'lump' in query and 'weak' in query and 'lower body' in query and 'numbness' in query and 'pale skin' in query and 'black eye' in query:
            speak("There is a possibility you have neuroblatoma.")
            speak("Neuroblastoma is a rare cancer that mostly affects young children. It develops from nerve cells called neuroblasts.")
            speak("Neuroblastoma affects around 100 children each year in the UK. It usually affects children under the age of five, and can even occur before a child is born.")
            print("There is a possibility you have neuroblatoma.")
            print("Neuroblastoma is a rare cancer that mostly affects young children. It develops from nerve cells called neuroblasts.")
            print("Neuroblastoma affects around 100 children each year in the UK. It usually affects children under the age of five, and can even occur before a child is born.")

        elif 'cell' in query and 'tumour' in query and 'diarrhoea' in query and 'constipation' in query and 'low blood sugar' in query and 'wheezing' in query:
            speak("There is a possibility you have neuroendocrine tumour.")
            speak("Neuroendocrine tumours are rare tumours that can occur in the cells of the neuroendocrine system.")
            speak("Unfortunately, many people are only diagnosed after other parts of their body are affected. However,it may still be possible to surgically remove the tumour.")
            print("There is a possibility you have neuroendocrine tumour.")
            print("Neuroendocrine tumours are rare tumours that can occur in the cells of the neuroendocrine system.")
            print("Unfortunately, many people are only diagnosed after other parts of their body are affected. However,it may still be possible to surgically remove the tumour.")

        elif 'lymph' in query and 'swelling' in query and 'neck' in query and 'armpit' in query and 'groin' in query:
            speak("There is a possibility you have Non-Hodgkin lymphoma.")
            speak("Non-Hodkin lymphoma is an uncommon cancer that develops in the lymphatic system, which is a network of vessels and glands spread throughout your body.")
            speak("Non-Hodgkin lymphoma can occur at any age, but your chances of developing the condition increase as you get older with most cases diagnosed in people over 65.")
            print("There is a possibility you have Non-Hodgkin lymphoma.")
            print("Non-Hodkin lymphoma is an uncommon cancer that develops in the lymphatic system, which is a network of vessels and glands spread throughout your body.")
            print("Non-Hodgkin lymphoma can occur at any age, but your chances of developing the condition increase as you get older with most cases diagnosed in people over 65.")

        elif 'nose' in query and 'blood' in query and 'picking' in query and 'blowing' in query and 'temperature' or 'humidity' in query:
            speak("There is a possibility you have nose bleeds")
            speak("Nosebleeds can be frightening, but they aren't usually a sign of anything serious and can often be treated at home.")
            speak("During a nosebleed, blood flows from one or both nostrils. It can be heavy or light and last for a few seconds to 15 minutes or more")
            print("There is a possibility you have nose bleeds")
            print("Nosebleeds can be frightening, but they aren't usually a sign of anything serious and can often be treated at home.")
            print("During a nosebleed, blood flows from one or both nostrils. It can be heavy or light and last for a few seconds to 15 minutes or more")

        elif 'overweight' in query and 'body' in query and 'fat' in query:
            speak("There is a possibility you have obesity.")
            speak("The term obese describes a person who's very overweight, with a lot of body fat.")
            speak("It's a common problem in every four adults and around one in every five children 10 and 11.")
            print("There is a possibility you have obesity.")
            print("The term obese describes a person who's very overweight, with a lot of body fat.")
            print("It's a common problem in every four adults and around one in every five children 10 and 11.")

        elif 'thought' in query and 'obsess' in query and 'compulsive' in query:
            speak("There is a possibility you have obsessive compulsive disorder.")
            speak("Obsessive compulsive disordeder OCD is a mental health condition where a person has obsessive thoughts and compulsive activity.")
            speak("In some cases the condition may run in families, and may be linked to certain inherited genes that affect the brain's development.")
            print("There is a possibility you have obsessive compulsive disorder.")
            print("Obsessive compulsive disordeder OCD is a mental health condition where a person has obsessive thoughts and compulsive activity.")
            print("In some cases the condition may run in families, and may be linked to certain inherited genes that affect the brain's development.")

        elif 'throat' in query and 'narrow' in query and 'sleep' in query and 'snoring' in query and 'noisy' in query or 'laboured' in query and 'breathing' in query and 'gasping' in query or 'snorting' in query:
            speak("There is a possibility you have obstructive sleep apnoea")
            speak("Obstructive sleep apnoea is a relatiely common condition where the walls of the throat relax and narrow during sleep, interrupting normal breathing.")
            speak("This may lead to regularly interrupted sleep,which may have a big impact on quality of life and increases the risk of developing certain conditions.")
            print("There is a possibility you have obstructive sleep apnoea")
            print("Obstructive sleep apnoea is a relatiely common condition where the walls of the throat relax and narrow during sleep, interrupting normal breathing.")
            print("This may lead to regularly interrupted sleep,which may have a big impact on quality of life and increases the risk of developing certain conditions.")

        elif 'oesophagus' in query and 'difficult swallowing' in query and 'indigestion' in query or 'heartburn' in query and 'bringing up food' in query and 'pain' in query and 'upper stomach' in query and 'chest' in query and 'back' in query:
            speak("There is a possibility you have oesophageal cancer.")
            speak("Oesophageal cancer is a type of cancer affceting the oesophagus, the long tube carries food from the throat to the stomach.")
            speak("It mainly affects people in their 60s and 70s and is more common in men than women")
            print("There is a possibility you have oesophageal cancer.")
            print("Oesophageal cancer is a type of cancer affceting the oesophagus, the long tube carries food from the throat to the stomach.")
            print("It mainly affects people in their 60s and 70s and is more common in men than women")

        elif 'mouth' in query and 'fungal' in query and 'patch' in query and 'taste' in query and 'loss' in query or 'unpleasent' in query and 'redness' in query and 'throat' in query and 'crack' in query and 'burning' in query:
            speak("There is a possibility you have oral thrush.")
            speak("Oral thrush is a fungal infection of the mouth. It is not contagious and is usually successfully treated with antifungal medication.")
            speak("Low numbers of the fungus Candida are naturally found in the mouth and digestive system of most people. They don't usually cause any problem but can lead to oral thrush if they multiply.")
            print("There is a possibility you have oral thrush.")
            print("Oral thrush is a fungal infection of the mouth. It is not contagious and is usually successfully treated with antifungal medication.")
            print("Low numbers of the fungus Candida are naturally found in the mouth and digestive system of most people. They don't usually cause any problem but can lead to oral thrush if they multiply")

        elif 'joint' in query and 'pain' in query or 'stiff' in query and 'knee' in query and 'hip' in query:
            speak("There is a possibility you have osteoarthritis.")
            speak("Oestoarthritis is a condition that causes the joints to become painful and stiff. It is the most common type of arthritis.")
            speak("Almost any joint can be affected by osteoarthritis but the condition most often causes problem in the hips, kness and small joints of hands.")
            print("There is a possibility you have osteoarthritis.")
            print("Oestoarthritis is a condition that causes the joints to become painful and stiff. It is the most common type of arthritis.")
            print("Almost any joint can be affected by osteoarthritis but the condition most often causes problem in the hips, kness and small joints of hands.")

        elif 'bone' in query and 'weak' in query or 'fragile' in query and 'ageing' in query and 'density' in query:
            speak("There is a possibility you have osteporosis.")
            speak("Osteporosis is a condition that weakens bones, making them fragile and more likely to break. It develops slowly over several years.")
            speak("Osteporosis isn't usually paainful until a fracture occurs, but spinal fractures are a common cause of long term pain.")
            print("There is a possibility you have osteporosis.")
            print("Osteporosis is a condition that weakens bones, making them fragile and more likely to break. It develops slowly over several years")
            print("Osteporosis isn't usually paainful until a fracture occurs, but spinal fractures are a common cause of long term pain.")

        elif 'ear canal' in query and 'ear pain' in query and 'itchiness' in query and 'liquid' in query or 'pus' in query and 'hearing loss' in query and 'swelling' in query and 'redness' in query:
            speak("There is a possibility you have otitis externa.")
            speak("Otitis externa is a condition that causes inflammation of the external ear canal, which is the tube between the outer ear and eardrum.")
            speak("Otitis externa is relatively common. It's estimated that around 1 in 10 people will be affected by it at some point in their life.")
            print("There is a possibility you have otitis externa.")
            print("Otitis externa is a condition that causes inflammation of the external ear canal, which is the tube between the outer ear and eardrum.")
            print("Otitis externa is relatively common. It's estimated that around 1 in 10 people will be affected by it at some point in their life.")

        elif 'ovary' in query and 'pain' in query  and 'bloating' in query and 'pelvis' in query and 'lower stomach' in query and 'difficulty eating' in query:
            speak("There is a possibility you have ovarian cancer.")
            speak("Ovarian cancer are common in women who have been through the menopause, altough it can affect women of any age.")
            speak("The condition depends upon the factors such as age, the number of eggs the ovaries release and whether someone in your family has had ovarian or breast cancer in the past.")
            print("There is a possibility you have ovarian cancer.")
            print("Ovarian cancer are common in women who have been through the menopause, altough it can affect women of any age.")
            print("The condition depends upon the factors such as age, the number of eggs the ovaries release and whether someone in your family has had ovarian or breast cancer in the past.")

        elif 'ovary' in query and 'sac' in query and 'cyst' in query and 'pain' in query and 'pelvic' in query or 'sex' in query and 'frequent urinate' in query and 'heavy period' in query and 'bloating' in query or 'swollen stomach' in query and 'difficult pregnant' in query:
            speak("There is a possibility you have ovarian cyst.")
            speak("An ovarian cyst is a fluid filled sac that develops on a women's ovary. They are very common and usually do not cause any symptoms.")
            speak("Ab ovarian cyst will usally only cause symptoms if it splits, is very large, or it blocks the blood supply to the ovaries.")
            print("There is a possibility you have ovarian cyst.")
            print("An ovarian cyst is a fluid filled sac that develops on a women's ovary. They are very common and usually do not cause any symptoms.")
            print("Ab ovarian cyst will usally only cause symptoms if it splits, is very large, or it blocks the blood supply to the ovaries.")

        elif 'thyroid' in query and 'hormone' in query and 'anxiety' in query or 'nervousness' in query and 'hyperactivity' in query and 'weightloss' in query and 'swelling' in query:
            speak("There is a possibility you have overactive thyroids.")
            speak("Overactive thyroid is a common hormonal condition that occurs when there is too much thyroid hormone in the body.")
            speak("Women are 10 times more likely to have an overactive thyroid gland then men.")
            print("There is a possibility you have overactive thyroids.")
            print("Overactive thyroid is a common hormonal condition that occurs when there is too much thyroid hormone in the body.")
            print("Women are 10 times more likely to have an overactive thyroid gland then men.")

        elif 'menu' in query or 'back' in query:
            speak("redirecting to menu")
            menu()


        else:
            speak("Cannot find any disease for this symptoms")
            speak("please specify more about your symptoms")




def doctor():

    speak("Tell me where do you having problem")

    i=0
    a=0
    b=0
    c=0
    e=0
    f=0
    g=0
    h=0
    j=0
    k=0
    l=0
    m=0
    o=0
    p=0
    q=0
    id=0
    t=0
    u=0
    v=0
    w=0
    x=0
    y=0
    z=0
    ia=0
    ib=0
    ic=0

    while True:
        query = takeCommand().lower()


        if 'allergy' in query:
            speak("I think you need to go for a Allergist")
            print("I think you need to go for a Allergist")
            speak("They treat immune system disorders such as asthma, eczema, food allergies, insect sting allergies, and some autoimmune diseases.")
            print("They treat immune system disorders such as asthma, eczema, food allergies, insect sting allergies, and some autoimmune diseases.")
            speak("You can contact Doctor sarika verma")
            print("You can contact Dr sarika verma")
            speak("Below are the address and contact number of Doctor sarika verma")
            print("Address: Doctor House, 101, First Floor, Peddar Rd, Cumballa Hill, Mumbai, Maharashtra 400026")
            print("Contact: 098159 06322")

            speak("Do you want to book an appoinment")
            print("Do you want to book an appoinment?")
            print("Yes or No")
            query=takeCommand().lower()
            if 'yes' in query or 'sure' in query or 'ok' in query:
                i=i+1
                sender = "healthcaremajor10@gmail.com"
                password = "major102021"
                speak("Tell me the patient name-")
                n=takeCommand()
                speak("Enter your email id")
                dr="Dr sarika verma"
                d= datetime.datetime.now()
                speak("By doing this you will get token number address and contact on your email id")
                receivers = [input('Please enter your email id-')]
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(sender, password)
                s.sendmail(sender, receivers,"Token is "+str(i)+"\nDr. sarika verma\nAddress: Doctor House, 101, First Floor, Peddar Rd, Cumballa Hill, Mumbai, Maharashtra 400026 \n Contact: 098159 06322")
                s.quit()
                sql = "insert into doctor(t_no, name, doctor, date) values(%s, %s, %s, %s)"
                val = (i, n, dr, d)
                myCursor.execute(sql, val)
                conn.commit()
                speak("your email is sent")
                print("Done")

            else :
                speak("ok")


        elif 'heart' in query:
            speak("I think you need to go for a Cardiologist")
            print("I think you need to go for a Cardiologist")
            speak("You might see them for heart failure, a heart attack high blood pressure or an irregular heartbeat")
            print("You might see them for heart failure, a heart attack, high blood pressure or an irregular heartbeat.")
            speak("You can contact Doctor Kamales Kumar Saha")
            print("You can contact Dr Kamales Kumar Saha")
            speak("Below are the address and contact number of Doctor Kamales Kumar Saha")
            print("Address: HeartClinic 5 accord classic 6 th floor near station, anupam stationary building, Goregaon, Mumbai, Maharashtra 400063")
            print("Contact: 099773 45555")
            speak("Do you want to book an appoinment")
            print("Do you want to book an appoinment?")
            print("Yes or No")
            query=takeCommand().lower()
            if 'yes' in query or 'sure' in query or 'ok' in query:
                a=a+1
                sender = "healthcaremajor10@gmail.com"
                password = "major102021"
                speak("Tell me the patient name-")
                n=takeCommand()
                dr="Dr Kamales Kumar Saha"
                d= datetime.datetime.now()
                speak("Enter your email id")
                speak("By doing this you will get token number address and contact on your email id")
                receivers = [input('Please enter your email id-')]
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(sender, password)
                s.sendmail(sender, receivers,"Token is "+str(a)+"\nDr. Kamales Kumar Saha\nAddress: HeartClinic 5 accord classic 6 th floor near station, anupam stationary building, Goregaon, Mumbai, Maharashtra 400063 \n Contact: 099773 45555")
                s.quit()
                sql = "insert into doctor(t_no, name, doctor, date) values(%s, %s, %s, %s)"
                val = (a, n, dr, d)
                myCursor.execute(sql, val)
                conn.commit()
                speak("your email is sent")
                print("Done")
            else :
                speak("ok")

        elif 'small Intestine' in query or 'colon' in query or 'bottom' in query:
            speak("I think you need to go for a Colon and Rectal Surgeons")
            print("I think you need to go for a Colon and Rectal Surgeons")
            speak("You would see these doctors for problems with your small intestine,colon, and bottom. They can treat colon cancer, hemorrhoids, and inflammatory bowel disease")
            print("You would see these doctors for problems with your small intestine,colon, and bottom. They can treat colon cancer, hemorrhoids, and inflammatory bowel disease")
            speak("You can contact Doctor Shyam singh")
            print("You can contact Dr shyam singh")
            speak("Below are the address and contact number of Doctor shyam singh")
            print("Address: Grant Road West, Chikalwadi, Tardeo, Mumbai, Maharashtra 400007")
            print("Contact: 022 6666 0099")
            speak("Do you want to book an appoinment")
            print("Do you want to book an appoinment?")
            print("Yes or No")
            query=takeCommand().lower()
            if 'yes' in query or 'sure' in query or 'ok' in query:
                b=b+1
                sender = "healthcaremajor10@gmail.com"
                password = "major102021"
                speak("Tell me the patient name-")
                n=takeCommand()
                dr="Dr shyam singh"
                d= datetime.datetime.now()
                speak("Enter your email id")
                speak("By doing this you will get token number address and contact on your email id")
                receivers = [input('Please enter your email id-')]
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(sender, password)
                s.sendmail(sender, receivers,"Token is "+str(b)+"\nDr. shyam singh\nAddress: Grant Road West, Chikalwadi, Tardeo, Mumbai, Maharashtra 400007 \n Contact: 022 6666 0099")
                s.quit()
                sql = "insert into doctor(t_no, name, doctor, date) values(%s, %s, %s, %s)"
                val = (b, n, dr, d)
                myCursor.execute(sql, val)
                conn.commit()
                speak("your email is sent")
                print("Done")
            else :
                speak("ok")

        elif 'ill' in query or 'injured' in query:
            speak("I think you need to go for a Critical care medicine specialist")
            print("I think you need to go for a Critical care medicine specialist")
            speak("They care for people who are critically ill or injured, often heading intensive care units in hospitals. You might see them if your heart or other organs are failing or if you’ve been in an accident.")
            print("They care for people who are critically ill or injured, often heading intensive care units in hospitals. You might see them if your heart or other organs are failing or if you’ve been in an accident.")
            speak("You can contact Doctor Preetha Joshi")
            print("You can contact Dr. Preetha Joshi")
            speak("Below are the address and contact number of Doctor Preetha Joshi")
            print("Address: Kokilaben Hospital, Rao Saheb, Achutrao Patwardhan Marg, Four Bungalows, Andheri West, Mumbai, Maharashtra 400053")
            print("Contact: 022 3099 9999")
            speak("Do you want to book an appoinment")
            print("Do you want to book an appoinment?")
            print("Yes or No")
            query=takeCommand().lower()
            if 'yes' in query or 'sure' in query or 'ok' in query:
                c=c+1
                sender = "healthcaremajor10@gmail.com"
                password = "major102021"
                speak("Tell me the patient name-")
                n=takeCommand()
                dr="Dr Preetha Joshi"
                d= datetime.datetime.now()
                speak("Enter your email id")
                speak("By doing this you will get token number address and contact on your email id")
                receivers = [input('Please enter your email id-')]
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(sender, password)
                s.sendmail(sender, receivers,"Token is "+str(c)+"\nDr. Preetha Joshi\nAddress: Kokilaben Hospital, Rao Saheb, Achutrao Patwardhan Marg, Four Bungalows, Andheri West, Mumbai, Maharashtra 400053 \n Contact: 022 3099 9999")
                s.quit()
                sql = "insert into doctor(t_no, name, doctor, date) values(%s, %s, %s, %s)"
                val = (c, n, dr, d)
                myCursor.execute(sql, val)
                conn.commit()
                speak("your email is sent")
                print("Done")
            else :
                speak("ok")


        elif 'skin' in query:
            speak("I think you need to go for a Dermatologists")
            print("I think you need to go for a Dermatologists")
            speak("They care for people who Have problems with your skin, hair, nails. Do you have moles, scars, acne, or skin allergies? Dermatologists can help.")
            print("They care for people who Have problems with your skin, hair, nails. Do you have moles, scars, acne, or skin allergies? Dermatologists can help.")
            speak("You can contact Doctor Rickson Pereira")
            print("You can contact Dr. Rickson Pereira")
            speak("Below are the address and contact number of Doctor Rickson Pereira")
            print("Address: 102&103, 36 Turner Road, Near Tavaa Hotel, Turner Rd, above Tanishq Showroom, Mumbai, Maharashtra 400050")
            print("Contact: 070459 52821")
            speak("Do you want to book an appoinment")
            print("Do you want to book an appoinment?")
            print("Yes or No")
            query=takeCommand().lower()
            if 'yes' in query or 'sure' in query or 'ok' in query:
                e=e+1
                sender = "healthcaremajor10@gmail.com"
                password = "major102021"
                speak("Tell me the patient name-")
                n=takeCommand()
                dr="Dr Rickson Pereira"
                d= datetime.datetime.now()
                speak("Enter your email id")
                speak("By doing this you will get token number address and contact on your email id")
                receivers = [input('Please enter your email id-')]
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(sender, password)
                s.sendmail(sender, receivers,"Token is "+str(e)+"\nDr. Rickson Pereira\nAddress: 102&103, 36 Turner Road, Near Tavaa Hotel, Turner Rd, above Tanishq Showroom, Mumbai, Maharashtra 400050 \n Contact: 070459 52821")
                s.quit()
                sql = "insert into doctor(t_no, name, doctor, date) values(%s, %s, %s, %s)"
                val = (e, n, dr, d)
                myCursor.execute(sql, val)
                conn.commit()
                speak("your email is sent")
                print("Done")

            else :
                speak("ok")



        elif 'hormones' in query or 'metabolism' in query:
            speak("I think you need to go for a Endocrinologists")
            print("I think you need to go for a Endocrinologists")
            speak("These are experts on hormones and metabolism. They can treat conditions like diabetes, thyroid problems, infertility, and calcium and bone disorders.")
            print("These are experts on hormones and metabolism. They can treat conditions like diabetes, thyroid problems, infertility, and calcium and bone disorders.")
            speak("You can contact Doctor Tanvi Mayur Patel")
            print("You can contact Dr. Tanvi Mayur Patel")
            speak("Below are the address and contact number of Doctor Tanvi Mayur Patel")
            print("Address: 55, Gokhale Rd, Dadar West, Dadar, Mumbai, Maharashtra 400028")
            print("Contact: 022 2437 9504")
            speak("Do you want to book an appoinment")
            print("Do you want to book an appoinment?")
            print("Yes or No")
            query=takeCommand().lower()
            if 'yes' in query or 'sure' in query or 'ok' in query:
                f=f+1
                sender = "healthcaremajor10@gmail.com"
                password = "major102021"
                speak("Tell me the patient name-")
                n=takeCommand()
                dr="Dr Tanvi Mayur Patel"
                d= datetime.datetime.now()
                speak("Enter your email id")
                speak("By doing this you will get token number address and contact on your email id")
                receivers = [input('Please enter your email id-')]
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(sender, password)
                s.sendmail(sender, receivers,"Token is "+str(f)+"\nDr. Tanvi Mayur Patel\nAddress: 55, Gokhale Rd, Dadar West, Dadar, Mumbai, Maharashtra 400028 \n Contact: 022 2437 9504")
                s.quit()
                sql = "insert into doctor(t_no, name, doctor, date) values(%s, %s, %s, %s)"
                val = (f, n, dr, d)
                myCursor.execute(sql, val)
                conn.commit()
                speak("your email is sent")
                print("Done")
            else :
                speak("ok")

        elif 'digestive organs' in query:
            speak("I think you need to go for a Gastroenterologists")
            print("I think you need to go for a Gastroenterologists")
            speak("They’re specialists in digestive organs, including the stomach, bowels, pancreas, liver, and gallbladder. You might see them for abdominal pain, ulcers, diarrhea, jaundice, or cancers in your digestive organs.")
            print("They’re specialists in digestive organs, including the stomach, bowels, pancreas, liver, and gallbladder. You might see them for abdominal pain, ulcers, diarrhea, jaundice, or cancers in your digestive organs.")
            speak("You can contact Doctor Mehul Choksi")
            print("You can contact Dr. Mehul Choksi")
            speak("Below are the address and contact number of Doctor Mehul Choksi")
            print("Address: Gabriel House, Gabriel Cross Road,, Mahim West, near Canossa Special School, Mumbai, Maharashtra 400016")
            print("Contact: 098337 48171")
            speak("Do you want to book an appoinment")
            print("Do you want to book an appoinment?")
            print("Yes or No")
            query=takeCommand().lower()
            if 'yes' in query or 'sure' in query or 'ok' in query:
                g=g+1
                sender = "healthcaremajor10@gmail.com"
                password = "major102021"
                speak("Tell me the patient name-")
                n=takeCommand()
                dr="Dr Mehul Choksi"
                d= datetime.datetime.now()
                speak("Enter your email id")
                speak("By doing this you will get token number address and contact on your email id")
                receivers = [input('Please enter your email id-')]
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(sender, password)
                s.sendmail(sender, receivers,"Token is "+str(g)+"\nDr. Mehul Choksi\nAddress: Gabriel House, Gabriel Cross Road,, Mahim West, near Canossa Special School, Mumbai, Maharashtra 400016 \n Contact: 098337 48171")
                s.quit()
                sql = "insert into doctor(t_no, name, doctor, date) values(%s, %s, %s, %s)"
                val = (g, n, dr, d)
                myCursor.execute(sql, val)
                conn.commit()
                speak("your email is sent")
                print("Done")
            else :
                speak("ok")

        elif 'routine checkups' in query:
            speak("I think you need to go for a Physician")
            print("I think you need to go for a Physician")
            speak("They care for the whole family, including children, adults, and the elderly. They do routine checkups and screening tests, give you flu and immunization shots, and manage diabetes and other ongoing medical conditions.")
            print("They care for the whole family, including children, adults, and the elderly. They do routine checkups and screening tests, give you flu and immunization shots, and manage diabetes and other ongoing medical conditions.")
            speak("You can contact Doctor Ameya Vijaykar")
            print("You can contact Dr. Ameya Vijaykar")
            speak("Below are the address and contact number of Doctor Ameya Vijaykar")
            print("Address: 55, Gokhale Rd, Dadar West, Dadar, Mumbai, Maharashtra 400028")
            print("Contact: 022 2437 9504")
            speak("Do you want to book an appoinment")
            print("Do you want to book an appoinment?")
            print("Yes or No")
            query=takeCommand().lower()
            if 'yes' in query or 'sure' in query or 'ok' in query:
                h=h+1
                sender = "healthcaremajor10@gmail.com"
                password = "major102021"
                speak("Tell me the patient name-")
                n=takeCommand()
                dr="Dr Ameya Vijaykar"
                d= datetime.datetime.now()
                speak("Enter your email id")
                speak("By doing this you will get token number address and contact on your email id")
                receivers = [input('Please enter your email id-')]
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(sender, password)
                s.sendmail(sender, receivers,"Token is "+str(h)+"\nDr. Ameya Vijaykar\nAddress: 55, Gokhale Rd, Dadar West, Dadar, Mumbai, Maharashtra 400028 \n Contact: 022 2437 9504")
                s.quit()
                sql = "insert into doctor(t_no, name, doctor, date) values(%s, %s, %s, %s)"
                val = (h, n, dr, d)
                myCursor.execute(sql, val)
                conn.commit()
                speak("your email is sent")
                print("Done")
            else :
                speak("ok")

        elif 'blood' in query or 'spleen' in query or 'lymph glands' in query:
            speak("I think you need to go for a Hematologists")
            print("I think you need to go for a Hematologists")
            speak("These are specialists in diseases of the blood, spleen, and lymph glands, like sickle cell disease, anemia, hemophilia, and leukemia.")
            print("These are specialists in diseases of the blood, spleen, and lymph glands, like sickle cell disease, anemia, hemophilia, and leukemia.")
            speak("You can contact Doctor V.P. Antia")
            print("You can contact Dr. V.P. Antia")
            speak("Below are the address and contact number of Doctor V.P. Antia")
            print("Address: Hospital, 60 A, Bhulabhai Desai Marg, Breach Candy, Cumballa Hill, Mumbai, Maharashtra 400026")
            print("Contact: 096195 32864")
            speak("Do you want to book an appoinment")
            print("Do you want to book an appoinment?")
            print("Yes or No")
            query=takeCommand().lower()
            if 'yes' in query or 'sure' in query or 'ok' in query:
                j=j+1
                sender = "healthcaremajor10@gmail.com"
                password = "major102021"
                speak("Tell me the patient name-")
                n=takeCommand()
                dr="Dr V.P. Antia"
                d= datetime.datetime.now()
                speak("Enter your email id")
                speak("By doing this you will get token number address and contact on your email id")
                receivers = [input('Please enter your email id-')]
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(sender, password)
                s.sendmail(sender, receivers,"Token is "+str(j)+"\nDr. V.P. Antia\nAddress: Hospital, 60 A, Bhulabhai Desai Marg, Breach Candy, Cumballa Hill, Mumbai, Maharashtra 400026 \n Contact: 096195 32864")
                s.quit()
                sql = "insert into doctor(t_no, name, doctor, date) values(%s, %s, %s, %s)"
                val = (j, n, dr, d)
                myCursor.execute(sql, val)
                conn.commit()
                speak("your email is sent")
                print("Done")
            else :
                speak("ok")

        elif 'infections' in query:
            speak("I think you need to go for a Infectious Disease Specialists")
            print("I think you need to go for a Infectious Disease Specialists")
            speak("They diagnose and treat infections in any part of your body, like fevers, Lyme disease, pneumonia, tuberculosis, and HIV and AIDS.")
            print("They diagnose and treat infections in any part of your body, like fevers, Lyme disease, pneumonia, tuberculosis, and HIV and AIDS.")
            speak("You can contact Doctor Vidyullata Koparkar")
            print("You can contact Dr. Vidyullata Koparkar")
            speak("Below are the address and contact number of Doctor Vidyullata Koparkar")
            print("Address: 5, Shroff Bungalow, Opp Pandya Hospital, near Sodawala Municipal School, Sodawala Ln, Borivali West, Mumbai, Maharashtra 400092")
            print("Contact: 090762 36902")
            speak("Do you want to book an appoinment")
            print("Do you want to book an appoinment?")
            print("Yes or No")
            query=takeCommand().lower()
            if 'yes' in query or 'sure' in query or 'ok' in query:
                k=k+1
                sender = "healthcaremajor10@gmail.com"
                password = "major102021"
                speak("Tell me the patient name-")
                n=takeCommand()
                dr="Dr Vidyullata Koparkar"
                d= datetime.datetime.now()
                speak("Enter your email id")
                speak("By doing this you will get token number address and contact on your email id")
                receivers = [input('Please enter your email id-')]
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(sender, password)
                s.sendmail(sender, receivers,"Token is "+str(k)+"\nDr. Vidyullata Koparkar\nAddress: 5, Shroff Bungalow, Opp Pandya Hospital, near Sodawala Municipal School, Sodawala Ln, Borivali West, Mumbai, Maharashtra 400092 \n Contact: 090762 36902")
                s.quit()
                sql = "insert into doctor(t_no, name, doctor, date) values(%s, %s, %s, %s)"
                val = (k, n, dr, d)
                myCursor.execute(sql, val)
                conn.commit()
                speak("your email is sent")
                print("Done")
            else :
                speak("ok")

        elif 'heridatary disorders' in query:
            speak("I think you need to go for a Medical Geneticists")
            print("I think you need to go for a Medical Geneticists")
            speak("They diagnose and treat hereditary disorders passed down from parents to children. These doctors may also offer genetic counseling and screening tests.")
            print("They diagnose and treat hereditary disorders passed down from parents to children. These doctors may also offer genetic counseling and screening tests.")
            speak("You can contact Doctor Shruti Bajaj")
            print("You can contact Dr. Shruti Bajaj")
            speak("Below are the address and contact number of Doctor Shruti Bajaj")
            print("Address: Suchak Hospital, 186, Manchubhai Road, Opposite, Malad Subway, Malad East, Mumbai, Maharashtra 400097")
            print("Contact: 091360 17545")
            speak("Do you want to book an appoinment")
            print("Do you want to book an appoinment?")
            print("Yes or No")
            query=takeCommand().lower()
            if 'yes' in query or 'sure' in query or 'ok' in query:
                l=l+1
                sender = "healthcaremajor10@gmail.com"
                password = "major102021"
                speak("Tell me the patient name-")
                n=takeCommand()
                dr="Dr Shruti Bajaj"
                d= datetime.datetime.now()
                speak("Enter your email id")
                speak("By doing this you will get token number address and contact on your email id")
                receivers = [input('Please enter your email id-')]
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(sender, password)
                s.sendmail(sender, receivers,"Token is "+str(l)+"\nDr. Shruti Bajaj\nAddress: Suchak Hospital, 186, Manchubhai Road, Opposite, Malad Subway, Malad East, Mumbai, Maharashtra 400097 \n Contact: 091360 17545")
                s.quit()
                sql = "insert into doctor(t_no, name, doctor, date) values(%s, %s, %s, %s)"
                val = (l, n, dr, d)
                myCursor.execute(sql, val)
                conn.commit()
                speak("your email is sent")
                print("Done")
            else :
                speak("ok")

        elif 'kidney' in query or 'high blood pressure' in query:
            speak("I think you need to go for a Nephrologists")
            print("I think you need to go for a Nephrologists")
            speak("They treat kidney diseases as well as high blood pressure and fluid and mineral imbalances linked to kidney disease.")
            print("They treat kidney diseases as well as high blood pressure and fluid and mineral imbalances linked to kidney disease.")
            speak("You can contact Doctor Prabhakar Bhurke")
            print("You can contact Dr.Prabhakar Bhurke")
            speak("Below are the address and contact number of Doctor Prabhakar Bhurke")
            print("Address: Prabhakar Bhurke Clinic, 6B of B wing, Gate No. 1, Crystal Plaza, Opposite Infiniti Mall, New Link Rd, behind Kailash Parbat Restaurant, Andheri West, Mumbai, Maharashtra 400053")
            print("Contact: 098203 43645")
            speak("Do you want to book an appoinment")
            print("Do you want to book an appoinment?")
            print("Yes or No")
            query=takeCommand().lower()
            if 'yes' in query or 'sure' in query or 'ok' in query:
                m=m+1
                sender = "healthcaremajor10@gmail.com"
                password = "major102021"
                speak("Tell me the patient name-")
                n=takeCommand()
                dr="Dr Prabhakar Bhurke"
                d= datetime.datetime.now()
                speak("Enter your email id")
                speak("By doing this you will get token number address and contact on your email id")
                receivers = [input('Please enter your email id-')]
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(sender, password)
                s.sendmail(sender, receivers,"Token is "+str(m)+"\nDr. Prabhakar Bhurke\nAddress: Prabhakar Bhurke Clinic, 6B of B wing, Gate No. 1, Crystal Plaza, Opposite Infiniti Mall, New Link Rd, behind Kailash Parbat Restaurant, Andheri West, Mumbai, Maharashtra 400053 \n Contact: 098203 43645")
                s.quit()
                sql = "insert into doctor(t_no, name, doctor, date) values(%s, %s, %s, %s)"
                val = (m, n, dr, d)
                myCursor.execute(sql, val)
                conn.commit()
                speak("your email is sent")
                print("Done")
            else :
                speak("ok")

        elif 'brain' in query or 'spinal Cord' in query or 'nerves' in query:
            speak("I think you need to go for a Neurologists")
            print("I think you need to go for a Neurologists")
            speak("These are specialists in the nervous system, which includes the brain, spinal cord, and nerves. They treat strokes, brain and spinal tumors, epilepsy, Parkinson's disease, and Alzheimer's disease.")
            print("These are specialists in the nervous system, which includes the brain, spinal cord, and nerves. They treat strokes, brain and spinal tumors, epilepsy, Parkinson's disease, and Alzheimer's disease.")
            speak("You can contact Doctor Rajendra Jhanwar")
            print("You can contact Dr. Rajendra Jhanwar")
            speak("Below are the address and contact number of Doctor Rajendra Jhanwar")
            print("Address: 1,vishal Complex,near Lifeline Hospital ,Narsing Lane, Goraswadi, Kandivali West, Mumbai, Maharashtra 400064")
            print("Contact: 099879 30840")
            speak("Do you want to book an appoinment")
            print("Do you want to book an appoinment?")
            print("Yes or No")
            query=takeCommand().lower()
            if 'yes' in query or 'sure' in query or 'ok' in query:
                o=o+1
                sender = "healthcaremajor10@gmail.com"
                password = "major102021"
                speak("Tell me the patient name-")
                n=takeCommand()
                dr="Dr Rajendra Jhanwar"
                d= datetime.datetime.now()
                speak("Enter your email id")
                speak("By doing this you will get token number address and contact on your email id")
                receivers = [input('Please enter your email id-')]
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(sender, password)
                s.sendmail(sender, receivers,"Token is "+str(o)+"\nDr. Rajendra Jhanwar\nAddress: 1,vishal Complex,near Lifeline Hospital ,Narsing Lane, Goraswadi, Kandivali West, Mumbai, Maharashtra 400064 \n Contact: 099879 30840")
                s.quit()
                sql = "insert into doctor(t_no, name, doctor, date) values(%s, %s, %s, %s)"
                val = (o, n, dr, d)
                myCursor.execute(sql, val)
                conn.commit()
                speak("your email is sent")
                print("Done")
            else :
                speak("ok")

        elif 'pregnancy' in query or 'childbirth' in query:
            speak("I think you need to go for a Obstetricians and Gynecologists")
            print("I think you need to go for a Obstetricians and Gynecologists")
            speak("Often called OB/GYNs, these doctors focus on women's health, including pregnancy and childbirth. They do Pap smears, pelvic exams, and pregnancy checkups. OB/GYNs are trained in both areas. But some of them may focus on women's reproductive health (gynecologists), and others specialize in caring for pregnant women (obstetricians).")
            print("Often called OB/GYNs, these doctors focus on women's health, including pregnancy and childbirth. They do Pap smears, pelvic exams, and pregnancy checkups. OB/GYNs are trained in both areas. But some of them may focus on women's reproductive health (gynecologists), and others specialize in caring for pregnant women (obstetricians).")
            speak("You can contact Doctor amrut raote")
            print("You can contact Dr. amrut raote")
            speak("Below are the address and contact number of Doctor amrut raote")
            print("Address: Rosa Vista, MH SH 42, opp. Suraj Water Park, Thane, Maharashtra 400607")
            print("Contact: 096993 04142")
            speak("Do you want to book an appoinment")
            print("Do you want to book an appoinment?")
            print("Yes or No")
            query=takeCommand().lower()
            if 'yes' in query or 'sure' in query or 'ok' in query:
                p=p+1
                sender = "healthcaremajor10@gmail.com"
                password = "major102021"
                speak("Tell me the patient name-")
                n=takeCommand()
                dr="Dr amrut raote"
                d= datetime.datetime.now()
                speak("Enter your email id")
                speak("By doing this you will get token number address and contact on your email id")
                receivers = [input('Please enter your email id-')]
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(sender, password)
                s.sendmail(sender, receivers,"Token is "+str(p)+"\nDr. amrut raote\nAddress: Rosa Vista, MH SH 42, opp. Suraj Water Park, Thane, Maharashtra 400607 \n Contact: 096993 04142")
                s.quit()
                sql = "insert into doctor(t_no, name, doctor, date) values(%s, %s, %s, %s)"
                val = (p, n, dr, d)
                myCursor.execute(sql, val)
                conn.commit()
                speak("your email is sent")
                print("Done")
            else :
                speak("ok")

        elif 'cancer' in query:
            speak("I think you need to go for a Oncologists")
            print("I think you need to go for a Oncologists")
            speak("These internists are cancer specialists. They do chemotherapy treatments and often work with radiation oncologists and surgeons to care for someone with cancer.")
            print("These internists are cancer specialists. They do chemotherapy treatments and often work with radiation oncologists and surgeons to care for someone with cancer.")
            speak("You can contact Doctor Suresh Advani")
            print("You can contact Dr. Suresh Advani")
            speak("Below are the address and contact number of Doctor Suresh Advani")
            print("Address: 201/ Sundaram Building, Next to Satyam Shopping Centre, Mahatma Gandhi Rd, Ghatkopar East, Mumbai, Maharashtra 400077")
            print("Contact: 091678 58608")
            speak("Do you want to book an appoinment")
            print("Do you want to book an appoinment?")
            print("Yes or No")
            query=takeCommand().lower()
            if 'yes' in query or 'sure' in query or 'ok' in query:
                q=q+1
                sender = "healthcaremajor10@gmail.com"
                password = "major102021"
                speak("Tell me the patient name-")
                n=takeCommand()
                dr="Dr Suresh Advani"
                d= datetime.datetime.now()
                speak("Enter your email id")
                speak("By doing this you will get token number address and contact on your email id")
                receivers = [input('Please enter your email id-')]
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(sender, password)
                s.sendmail(sender, receivers,"Token is "+str(q)+"\nDr. Suresh Advani\nAddress: 201/ Sundaram Building, Next to Satyam Shopping Centre, Mahatma Gandhi Rd, Ghatkopar East, Mumbai, Maharashtra 400077 \n Contact: 091678 58608")
                s.quit()
                sql = "insert into doctor(t_no, name, doctor, date) values(%s, %s, %s, %s)"
                val = (q, n, dr, d)
                myCursor.execute(sql, val)
                conn.commit()
                speak("your email is sent")
                print("Done")
            else :
                speak("ok")

        elif 'eye' in query:
            speak("I think you need to go for a Ophthalmologists")
            print("I think you need to go for a Ophthalmologists")
            speak("You call them eye doctors. They can prescribe glasses or contact lenses and diagnose and treat diseases like glaucoma. Unlike optometrists, they’re medical doctors who can treat every kind of eye condition as well as operate on the eyes.")
            print("You call them eye doctors. They can prescribe glasses or contact lenses and diagnose and treat diseases like glaucoma. Unlike optometrists, they’re medical doctors who can treat every kind of eye condition as well as operate on the eyes.")
            speak("You can contact Doctor Himanshu Mehta")
            print("You can contact Dr. Himanshu Mehta")
            speak("Below are the address and contact number of Doctor Himanshu Mehta")
            print("Address: 101, Hiralaya Apartment, Ashok Nagar, N S Rd Number 10, near IndusInd Bank, JVPD Scheme, Mumbai, Maharashtra 400049")
            print("Contact: 098676 56060")
            speak("Do you want to book an appoinment")
            print("Do you want to book an appoinment?")
            print("Yes or No")
            query=takeCommand().lower()
            if 'yes' in query or 'sure' in query or 'ok' in query:
                id=id+1
                sender = "healthcaremajor10@gmail.com"
                password = "major102021"
                speak("Tell me the patient name-")
                n=takeCommand()
                dr="Dr Himanshu Mehta"
                d= datetime.datetime.now()
                speak("Enter your email id")
                speak("By doing this you will get token number address and contact on your email id")
                receivers = [input('Please enter your email id-')]
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(sender, password)
                s.sendmail(sender, receivers,"Token is "+str(id)+"\nDr. Himanshu Mehta\nAddress: 101, Hiralaya Apartment, Ashok Nagar, N S Rd Number 10, near IndusInd Bank, JVPD Scheme, Mumbai, Maharashtra 400049 \n Contact: 098676 56060")
                s.quit()
                sql = "insert into doctor(t_no, name, doctor, date) values(%s, %s, %s, %s)"
                val = (id, n, dr, d)
                myCursor.execute(sql, val)
                conn.commit()
                speak("your email is sent")
                print("Done")
            else :
                speak("ok")

        elif 'ears' in query or 'nose' in query or 'throat' in query or 'sinuses' in query or 'head' in query or 'neck' in query or 'respiratory system' in query:
            speak("I think you need to go for a Otolaryngologists")
            print("I think you need to go for a Otolaryngologists")
            speak("They treat diseases in the ears, nose, throat, sinuses, head, neck, and respiratory system. They also can do reconstructive and plastic surgery on your head and neck.")
            print("They treat diseases in the ears, nose, throat, sinuses, head, neck, and respiratory system. They also can do reconstructive and plastic surgery on your head and neck.")
            speak("You can contact Doctor JAIDEEP MANKANI")
            print("You can contact Dr. JAIDEEP MANKANI")
            speak("Below are the address and contact number of Doctor JAIDEEP MANKANI")
            print("Address: EMP 46, next to Monginis Cake Shop, ठाकुर, Evershine Millennium Paradise, Thakur Village, Kandivali East, Mumbai, Maharashtra 400101")
            print("Contact: 098201 71292")
            speak("Do you want to book an appoinment")
            print("Do you want to book an appoinment?")
            print("Yes or No")
            query=takeCommand().lower()
            if 'yes' in query or 'sure' in query or 'ok' in query:
                t=t+1
                sender = "healthcaremajor10@gmail.com"
                password = "major102021"
                speak("Tell me the patient name-")
                n=takeCommand()
                dr="Dr JAIDEEP MANKANI"
                d= datetime.datetime.now()
                speak("Enter your email id")
                speak("By doing this you will get token number address and contact on your email id")
                receivers = [input('Please enter your email id-')]
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(sender, password)
                s.sendmail(sender, receivers,"Token is "+str(t)+"\nDr. JAIDEEP MANKANI\nAddress: EMP 46, next to Monginis Cake Shop, ठाकुर, Evershine Millennium Paradise, Thakur Village, Kandivali East, Mumbai, Maharashtra 400101 \n Contact: 098201 71292")
                s.quit()
                sql = "insert into doctor(t_no, name, doctor, date) values(%s, %s, %s, %s)"
                val = (t, n, dr, d)
                myCursor.execute(sql, val)
                conn.commit()
                speak("your email is sent")
                print("Done")
            else :
                speak("ok")

        elif 'tests urine' in query  and 'blood fluid samples' in query:
            speak("I think you need to go for a Pathologists")
            print("I think you need to go for a Pathologists")
            speak("These lab doctors identify the causes of diseases by examining body tissues and fluids under microscopes.")
            print("These lab doctors identify the causes of diseases by examining body tissues and fluids under microscopes.")
            speak("You can contact Doctor Abhishek vishwakarma")
            print("You can contact Dr. Abhishek vishwakarma")
            speak("Below are the address and contact number of Doctor Abhishek vishwakarma")
            print("Address: Shop No. 4, 1st Floor, Panchsheel Building, Devidayal Road, Panchrasta, Mulund West, Mumbai, Maharashtra 400080")
            print("Contact: 084540 52303")
            speak("Do you want to book an appoinment")
            print("Do you want to book an appoinment?")
            print("Yes or No")
            query=takeCommand().lower()
            if 'yes' in query or 'sure' in query or 'ok' in query:
                u=u+1
                sender = "healthcaremajor10@gmail.com"
                password = "major102021"
                speak("Tell me the patient name-")
                n=takeCommand()
                dr="Dr Abhishek vishwakarma"
                d= datetime.datetime.now()
                speak("Enter your email id")
                speak("By doing this you will get token number address and contact on your email id")
                receivers = [input('Please enter your email id-')]
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(sender, password)
                s.sendmail(sender, receivers,"Token is "+str(u)+"\nDr. Abhishek vishwakarma\nAddress: Shop No. 4, 1st Floor, Panchsheel Building, Devidayal Road, Panchrasta, Mulund West, Mumbai, Maharashtra 400080 \n Contact: 084540 52303")
                s.quit()
                sql = "insert into doctor(t_no, name, doctor, date) values(%s, %s, %s, %s)"
                val = (u, n, dr, d)
                myCursor.execute(sql, val)
                conn.commit()
                speak("your email is sent")
                print("Done")
            else :
                speak("ok")

        elif 'treat neck' in query or 'back pain' in query or 'sports' in query or 'spinal cord injuries' in query:
            speak("I think you need to go for a Physiatrists")
            print("I think you need to go for a Physiatrists")
            speak("These specialists in physical medicine and rehabilitation treat neck or back pain and sports or spinal cord injuries as well as other disabilities caused by accidents or diseases.")
            print("These specialists in physical medicine and rehabilitation treat neck or back pain and sports or spinal cord injuries as well as other disabilities caused by accidents or diseases.")
            speak("You can contact Doctor Abhishek vishwakarma")
            print("You can contact Dr. Abhishek vishwakarma")
            speak("Below are the address and contact number of Doctor Abhishek vishwakarma")
            print("Address: 302,JAgshantiniketan CHS,jagshantiniketan marg,, mira road(E), near cinemax theatre, Mumbai, Maharashtra 401107")
            print("Contact: 099208 53337")
            speak("Do you want to book an appoinment")
            print("Do you want to book an appoinment?")
            print("Yes or No")
            query=takeCommand().lower()
            if 'yes' in query or 'sure' in query or 'ok' in query:
                v=v+1
                sender = "healthcaremajor10@gmail.com"
                password = "major102021"
                speak("Tell me the patient name-")
                n=takeCommand()
                dr="Dr Abhishek vishwakarma"
                d= datetime.datetime.now()
                speak("Enter your email id")
                speak("By doing this you will get token number address and contact on your email id")
                receivers = [input('Please enter your email id-')]
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(sender, password)
                s.sendmail(sender, receivers,"Token is "+str(v)+"\nDr. Abhishek vishwakarma\nAddress: 302,JAgshantiniketan CHS,jagshantiniketan marg,, mira road(E), near cinemax theatre, Mumbai, Maharashtra 401107 \n Contact: 099208 53337")
                s.quit()
                sql = "insert into doctor(t_no, name, doctor, date) values(%s, %s, %s, %s)"
                val = (v, n, dr, d)
                myCursor.execute(sql, val)
                conn.commit()
                speak("your email is sent")
                print("Done")
            else :
                speak("ok")

        elif 'rebuild' in query and 'face' in query :
            speak("I think you need to go for a Plastic Surgeons")
            print("I think you need to go for a Plastic Surgeons")
            speak("You might call them cosmetic surgeons. They rebuild or repair your skin, face, hands, breasts, or body.")
            print("You might call them cosmetic surgeons. They rebuild or repair your skin, face, hands, breasts, or body.")
            speak("You can contact Doctor Parag Telang")
            print("You can contact Dr. Parag Telang")
            speak("Below are the address and contact number of Doctor Parag Telang")
            print("Address: 401-402, Vastu Precinct, Opp Mercedes showroom, Sundervan, Lokhandwala Road, Andheri West, Mumbai, Maharashtra 400053")
            print("Contact: 075067 10258")
            speak("Do you want to book an appoinment")
            print("Do you want to book an appoinment?")
            print("Yes or No")
            query=takeCommand().lower()
            if 'yes' in query or 'sure' in query or 'ok' in query:
                w=w+1
                sender = "healthcaremajor10@gmail.com"
                password = "major102021"
                speak("Tell me the patient name-")
                n=takeCommand()
                dr="Dr Parag Telang"
                d= datetime.datetime.now()
                speak("Enter your email id")
                speak("By doing this you will get token number address and contact on your email id")
                receivers = [input('Please enter your email id-')]
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(sender, password)
                s.sendmail(sender, receivers,"Token is "+str(w)+"\nDr. Parag Telang\nAddress: 401-402, Vastu Precinct, Opp Mercedes showroom, Sundervan, Lokhandwala Road, Andheri West, Mumbai, Maharashtra 400053 \n Contact: 075067 10258")
                s.quit()
                sql = "insert into doctor(t_no, name, doctor, date) values(%s, %s, %s, %s)"
                val = (w, n, dr, d)
                myCursor.execute(sql, val)
                conn.commit()
                speak("your email is sent")
                print("Done")
            else :
                speak("ok")

        elif 'ankles' in query or 'feet' in query:
            speak("I think you need to go for a Podiatrists")
            print("I think you need to go for a Podiatrists")
            speak("They care for problems in your ankles and feet. That can include injuries from accidents or sports or from ongoing health conditions like diabetes.")
            print("They care for problems in your ankles and feet. That can include injuries from accidents or sports or from ongoing health conditions like diabetes.")
            speak("You can contact Doctor Shah")
            print("You can contact Dr.Shah")
            speak("Below are the address and contact number of Doctor Shah")
            print("Address: 9th Floor, Mahalaxmi Chambers, 22, Bhulabhai Desai Marg, Mahalaxmi West, Mumbai, Maharashtra 400026")
            print("Contact: 084549 20321")
            speak("Do you want to book an appoinment")
            print("Do you want to book an appoinment?")
            print("Yes or No")
            query=takeCommand().lower()
            if 'yes' in query or 'sure' in query or 'ok' in query:
                x=x+1
                sender = "healthcaremajor10@gmail.com"
                password = "major102021"
                speak("Tell me the patient name-")
                n=takeCommand()
                dr="Dr Saha"
                d= datetime.datetime.now()
                speak("Enter your email id")
                speak("By doing this you will get token number address and contact on your email id")
                receivers = [input('Please enter your email id-')]
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(sender, password)
                s.sendmail(sender, receivers,"Token is "+str(x)+"\nDr. Shah\nAddress: 9th Floor, Mahalaxmi Chambers, 22, Bhulabhai Desai Marg, Mahalaxmi West, Mumbai, Maharashtra 400026 \n Contact: 084549 20321")
                s.quit()
                sql = "insert into doctor(t_no, name, doctor, date) values(%s, %s, %s, %s)"
                val = (x, n, dr, d)
                myCursor.execute(sql, val)
                conn.commit()
                speak("your email is sent")
                print("Done")
            else :
                speak("ok")

        elif 'mental' in query or 'emotional' in query  or 'addictive disorders' in query:
            speak("I think you need to go for a Psychiatrists")
            print("I think you need to go for a Psychiatrists")
            speak("These doctors work with people with mental, emotional, or addictive disorders. They can diagnose and treat depression, schizophrenia, substance abuse, anxiety disorders, and sexual and gender identity issues.")
            print("These doctors work with people with mental, emotional, or addictive disorders. They can diagnose and treat depression, schizophrenia, substance abuse, anxiety disorders, and sexual and gender identity issues.")
            speak("You can contact Doctor Priyanka Raut")
            print("You can contact Dr. Priyanka Raut")
            speak("Below are the address and contact number of Doctor Priyanka Raut")
            print("Address: B-8, Ground Floor, Nirmala Niwas, 4/10, Aimai Merwanji St, near Laal Maidan, Parel, Mumbai, Maharashtra 400012")
            print("Contact: 081694 29044")
            speak("Do you want to book an appoinment")
            print("Do you want to book an appoinment?")
            print("Yes or No")
            query=takeCommand().lower()
            if 'yes' in query or 'sure' in query or 'ok' in query:
                y=y+1
                sender = "healthcaremajor10@gmail.com"
                password = "major102021"
                speak("Tell me the patient name-")
                n=takeCommand()
                dr="Dr Priyanka Raut"
                d= datetime.datetime.now()
                speak("Enter your email id")
                speak("By doing this you will get token number address and contact on your email id")
                receivers = [input('Please enter your email id-')]
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(sender, password)
                s.sendmail(sender, receivers,"Token is "+str(y)+"\nDr. Priyanka Raut\nAddress: B-8, Ground Floor, Nirmala Niwas, 4/10, Aimai Merwanji St, near Laal Maidan, Parel, Mumbai, Maharashtra 400012 \n Contact: 081694 29044")
                s.quit()
                sql = "insert into doctor(t_no, name, doctor, date) values(%s, %s, %s, %s)"
                val = (y, n, dr, d)
                myCursor.execute(sql, val)
                conn.commit()
                speak("your email is sent")
                print("Done")
            else :
                speak("ok")

        elif 'lungs' in query:
            speak("I think you need to go for a Pulmonologists")
            print("I think you need to go for a Pulmonologists")
            speak("You would see these specialists for problems like lung cancer, pneumonia, asthma, emphysema, and trouble sleeping caused by breathing issues.")
            print("You would see these specialists for problems like lung cancer, pneumonia, asthma, emphysema, and trouble sleeping caused by breathing issues.")
            speak("You can contact Doctor Miti A. Shah")
            print("You can contact Dr.Miti A. Shah")
            speak("Below are the address and contact number of Doctor Miti A. Shah")
            print("Address: 6A/3, 1st floor, Sindhi Colony, opp. Gurukripa Hotel, Sion West, Mumbai, Maharashtra 400022")
            print("Contact: 098205 32470")
            speak("Do you want to book an appoinment")
            print("Do you want to book an appoinment?")
            print("Yes or No")
            query=takeCommand().lower()
            if 'yes' in query or 'sure' in query or 'ok' in query:
                z=z+1
                sender = "healthcaremajor10@gmail.com"
                password = "major102021"
                speak("Tell me the patient name-")
                n=takeCommand()
                dr="Dr Miti A. Shah"
                d= datetime.datetime.now()
                speak("Enter your email id")
                speak("By doing this you will get token number address and contact on your email id")
                receivers = [input('Please enter your email id-')]
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(sender, password)
                s.sendmail(sender, receivers,"Token is "+str(z)+"\nDr. Miti A. Shah\nAddress: 6A/3, 1st floor, Sindhi Colony, opp. Gurukripa Hotel, Sion West, Mumbai, Maharashtra 400022 \n Contact: 098205 32470")
                s.quit()
                sql = "insert into doctor(t_no, name, doctor, date) values(%s, %s, %s, %s)"
                val = (z, n, dr, d)
                myCursor.execute(sql, val)
                conn.commit()
                speak("your email is sent")
                print("Done")
            else :
                speak("ok")

        elif 'joint' in query or 'muscle' in query or 'bone' in query or 'tendon' in query:
            speak("I think you need to go for a Rheumatologists")
            print("I think you need to go for a Rheumatologists")
            speak("They specialize in arthritis and other diseases in your joints, muscles, bones, and tendons. You might see them for your osteoporosis (weak bones), back pain, gout, tendinitis from sports or repetitive injuries, and fibromyalgia.")
            print("They specialize in arthritis and other diseases in your joints, muscles, bones, and tendons. You might see them for your osteoporosis (weak bones), back pain, gout, tendinitis from sports or repetitive injuries, and fibromyalgia.")
            speak("You can contact Doctor amrut raote")
            print("You can contact Dr.amrut raote")
            speak("Below are the address and contact number of Doctor amrut raote")
            print("Address: Mayuresh Srishti Complex, Srishti Heights Parking Rd, Bhandup, Rajiv Gandhi Nagar, Bhandup West, Mumbai, Maharashtra 400078")
            print("Contact: 022 2594 6624")
            speak("Do you want to book an appoinment")
            print("Do you want to book an appoinment?")
            print("Yes or No")
            query=takeCommand().lower()
            if 'yes' in query or 'sure' in query or 'ok' in query:
                ia=ia+1
                sender = "healthcaremajor10@gmail.com"
                password = "major102021"
                speak("Tell me the patient name-")
                n=takeCommand()
                dr="Dr amrut raote"
                d= datetime.datetime.now()
                speak("Enter your email id")
                speak("By doing this you will get token number address and contact on your email id")
                receivers = [input('Please enter your email id-')]
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(sender, password)
                s.sendmail(sender, receivers,"Token is "+str(ia)+"\nDr. amrut raote\nAddress: Mayuresh Srishti Complex, Srishti Heights Parking Rd, Bhandup, Rajiv Gandhi Nagar, Bhandup West, Mumbai, Maharashtra 400078 \n Contact: 022 2594 6624")
                s.quit()
                sql = "insert into doctor(t_no, name, doctor, date) values(%s, %s, %s, %s)"
                val = (ia, n, dr, d)
                myCursor.execute(sql, val)
                conn.commit()
                speak("your email is sent")
                print("Done")
            else :
                speak("ok")

        elif 'tumors' in query or 'appendices' in query or 'gallbladders' in query or 'repair hernias' in query:
            speak("I think you need to go for a Surgeons")
            print("I think you need to go for a Surgeons")
            speak("These doctors can operate on all parts of your body. They can take out tumors, appendices, or gallbladders and repair hernias. Many surgeons have subspecialties, like cancer, hand, or vascular surgery.")
            print("These doctors can operate on all parts of your body. They can take out tumors, appendices, or gallbladders and repair hernias. Many surgeons have subspecialties, like cancer, hand, or vascular surgery.")
            speak("You can contact Doctor Anuj Singh")
            print("You can contact Dr. Anuj Singh")
            speak("Below are the address and contact number of Doctor Anuj Singh")
            print("Address: Dr. Anuj Singh's Hip & Knee centre. Namaha Healthcare, SV Road, near East West Flyover, Kandivali west, Mumbai, Maharashtra 400067")
            print("Contact: 099678 11910")
            speak("Do you want to book an appoinment")
            print("Do you want to book an appoinment?")
            print("Yes or No")
            query=takeCommand().lower()
            if 'yes' in query or 'sure' in query or 'ok' in query:
                ib=ib+1
                sender = "healthcaremajor10@gmail.com"
                password = "major102021"
                speak("Tell me the patient name-")
                n=takeCommand()
                dr="Dr Anuj Singh"
                d= datetime.datetime.now()
                speak("Enter your email id")
                speak("By doing this you will get token number address and contact on your email id")
                receivers = [input('Please enter your email id-')]
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(sender, password)
                s.sendmail(sender, receivers,"Token is "+str(ib)+"\nDr. Anuj Singh\nAddress: Dr. Anuj Singh's Hip & Knee centre. Namaha Healthcare, SV Road, near East West Flyover, Kandivali west, Mumbai, Maharashtra 400067 \n Contact: 099678 11910")
                s.quit()
                sql = "insert into doctor(t_no, name, doctor, date) values(%s, %s, %s, %s)"
                val = (ib, n, dr, d)
                myCursor.execute(sql, val)
                conn.commit()
                speak("your email is sent")
                print("Done")
            else :
                speak("ok")

        elif 'urinary tract' in query:
            speak("I think you need to go for a Urologists")
            print("I think you need to go for a Urologists")
            speak("These are surgeons who care for men and women for problems in the urinary tract, like a leaky bladder. They also treat male infertility and do prostate exams.")
            print("These are surgeons who care for men and women for problems in the urinary tract, like a leaky bladder. They also treat male infertility and do prostate exams.")
            speak("You can contact Doctor Ajaykumar R. Gajengi")
            print("You can contact Dr. Ajaykumar R. Gajengi")
            speak("Below are the address and contact number of Doctor Ajaykumar R. Gajengi")
            print("Address: These are surgeons who care for men and women for problems in the urinary tract, like a leaky bladder. They also treat male infertility and do prostate exams.")
            print("Contact: 077770 72031")
            speak("Do you want to book an appoinment")
            print("Do you want to book an appoinment?")
            print("Yes or No")
            query=takeCommand().lower()
            if 'yes' in query or 'sure' in query or 'ok' in query:
                ic=ic+1
                sender = "healthcaremajor10@gmail.com"
                password = "major102021"
                speak("Tell me the patient name-")
                n=takeCommand()
                dr="Dr Ajaykumar R. Gajengi"
                d= datetime.datetime.now()
                speak("Enter your email id")
                speak("By doing this you will get token number address and contact on your email id")
                receivers = [input('Please enter your email id-')]
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(sender, password)
                s.sendmail(sender, receivers,"Token is "+str(ic)+"\nDr. Ajaykumar R. Gajengi\nAddress: These are surgeons who care for men and women for problems in the urinary tract, like a leaky bladder. They also treat male infertility and do prostate exams. \n Contact: 077770 72031")
                s.quit()
                sql = "insert into doctor(t_no, name, doctor, date) values(%s, %s, %s, %s)"
                val = (ic, n, dr, d)
                myCursor.execute(sql, val)
                conn.commit()
                speak("your email is sent")
                print("Done")
            else :
                speak("ok")


        elif 'back' in query or 'menu' in query:
            speak("redirecting to menu")
            menu()

        else:
            speak("Cannot find any doctor for this")
            speak("please specify the body part in which you have problem")



if __name__ == '__main__':
    clear = lambda: os.system('cls')
    clear()
    wishMe()
    usrname()
    menu()










