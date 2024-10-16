Quran Verse Reminder App

بِسْمِ اللهِ الرَّحْمَنِ الرَّحِيمِ

1) Introduction
   
With our busy lives, trying to balance work, family, hobbies, and interests, sometimes we forget to focus on what matters the most -- Allah and His Word, the Qur'an.

With that thought in mind, I created this simple app, which prompts us to read the Qur'an.

2) How it works
   
Once the app is opened, it starts with a blank screen, which is updated after 5 seconds with the Qur'anic text (in Arabic) and the number of the Surah:Ayah which we are reading from.

Every 15 minutes, the app makes a couple of API calls to generate a random verse. Then, it uses the verse reference to fetch the text of the ayah in question. The verse and reference are then displayed in the GUI.

There are a few color theme options to choose from if you right-click on any of the elements of the GUI.

For this project, we are using the modules Tkinter for the GUI, OS to resolve an issue with the .ico icon when compiling with Pyinstaller, and Requests to access the JSON dictionaries with our API calls.

I also used the Quran Foundation API (https://api-docs.quran.com/docs/category/quran.com-api), and designed the .ico file and the .png files within the "pics" directory on Canva.com.

3) Conclusion
   
May Allah make it easy for us to be reminded of His Verses, and not make us from those who abandon the Qur'an, and may He ease for us our affairs both in the Dunya (worldly life) and  the Akhirah (Hereafter). Ameen
