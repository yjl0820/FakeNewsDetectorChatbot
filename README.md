# FakeNewsDetectorChatbot
Fake News Detecting Chatbot using RNN and LSTM with Keras and Discord (HackPSU 2020 Project)

## Installation/Setup Guide

### 1. Discord Bot API
In order to use this program, Discord's Bot API is required. Please follow below step to get Discord Bot API:
  1. Login to Discord and Go to https://discord.com/developers/applications
  2. Create New Application by clicking the button right top corner of the screen
  3. Go to your discord and create a server
  4. Create Bot and copy the Bot's token code
  5. Got to the OAuth2 tab and authenticate your API to add your bot to your Discord server
  
### 2. Setting up environment and required preparation
  1. Make sure to install all the packages required for the code using requirement.txt
  2. If you are a Mac user, go to Application/Python 3.x/ and install certificates.command to allow the code to run without authentication error
  3. Due to data file size, data is zipped into data folder, please unzip before use
  4. Go to discordbot.py and at the bottom of the code client.run(), put your Bot's token code that you copied from previous step
  5. Go to MMModels.py and check the file directory, the both .py files have to be in same directory

### 3. After running the code
  1. Use /FakeNews <content> to get result
  2. Content can be whole article for better result, but also can be just the title
  3. Enjoy! :)
  
-----------------------------------------------------------------------------------------------------------


  

