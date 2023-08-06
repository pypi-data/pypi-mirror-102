Installation:
To install just hit pip install typetowritescreen
for linux or macosx pip3 install typetowrite sceen
Usage:
In your main.kv file 
 


:#:import TypeToWriteScreen typetowritescreen.typetowritescreen.TypeToWriteScreen
TypeToWriteScreen:

    id:typetowritescreen
    name:"typetowritescreen"
to change the Background in your main.py self.screen.ids.typetowritescreen.background = 'background.jpg'

