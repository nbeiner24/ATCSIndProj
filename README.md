# ATCSIndProj
My final project for the 2024 Advanced Topics in CS course at Polytechnic School

Probably gonna make a game or something in Processing but will decide fully later.

# 5/10/2024
Decided to fully commit to recreating (part of) World 1-1 of the original super mario game.
Installed Processing and made some classes.

# 5/15/2024
Found out about pygame and decided to use that instead of processing
Set up a basic little display program and learned how to set an icon for the program window
(I used the star from super mario)

# 5/17/2024
Was supposed to make a commit today but computer died. Dove a bit into making an actual Sprite class.

# 5/19/2024
I realized partway through that this task is far more complicated than I originally made it out to be, so the program is honestly far more rudimentary and inefficient than I wanted it to be, in terms of both visuals and the code itself. I think that if I had a whole month I could actually recreate a 1:1 replica of the first level of the original Super Mario. I also was pretty busy during the week and weekend with AP's, prom, and my weekend job, but I still appreciate what I could do for the program :).

# FINAL WORDS
I really had fun learning pygame, and I think I might either continue this project or start a new one over the summer, because I really like how intuitive the pygame built-in methods are, and theres a really strong and beginner friendly community on Youtube and other areas of the internet. One thing that I regret doing is making my own sprite class because halfway through my project, things started becoming really ineficcient in terms of code, and I realized that pygame actually has its own built-in sprite class that probably would have made the project a little bit easier. There were two things that I wanted to add to my little demo but either couldn't figure out a solution or decided that my weird home-made Sprite class wouldn't allow me to go further.

The first is that I wanted to make the mario sprite change from the small pixel art to the large version. I have all the files in the folder, but I couldn't manage to try and get it to render the large version after consuming the mushroom. I think it's because once I created a player object, I couldn't edit the image that represented it, but I could be wrong.

I also wanted to make the basic black bars have the texture of actual Mario bricks, but I couldn't find a good texture on the internet. Additionally, I'm not sure how a set texture would work with varying sizes of rectangles, like the ones I had in the demo program.

Finally, the last thing I wanted to do with the demo was that I wanted to add animations to Mario and the Goomba, but as I was researching how to animate in pygame, I learned that not only do you need an image called a sprite sheet, which helps you animate easier, but all the sources I found were telling me how to do it by using pygame's built-in sprite class. As I said earlier, I made and used my own sprite class, so I ended up dropping the animation idea after an hour or so of research.

Again, just to paraphrase, I think pygame is really cool and I either want to finish this project or start another one over the summer. I know I made some mistakes along the way and was restricted by timing and my personal schedule :( , but now that I know more about pygame, I think I could actually make a good program with well thought-out functions and efficient coding. 

# FINAL FINAL WORDS (5/20/2024)
Forgot to write about some other things I wanted to eventually have in my replica of level 1-1 yesterday, so I'm doing it now.

Instead of just putting the player back at the top or beginning of the stage, I wanted to make a formal game over/restart screen so that the player had the optiojn to restart or quit without having to press the exit button on the top corner of the game window. I think that the quit game would be fairly easy to implement, but I never really researched on how to reset the stage fully without closing the game window, which is something to note as something to learn the future. I also wanted to make a game timer, but that does not seem very hard to implement, as there is probably some sort of method within pygame's clock class, or I could just do some shenanigans with python's time module.

Another aspect that I wanted to implement eventually that I believe would be quite challenging is creating the subterranean part of level 1-1 of the original Super Mario. The hardest part would probably be clearing the whole entire screen and then instantly rendering in the subterranean part of the level, but again, I'm just making educated predictions. For all I know, this could be super easy to do.

Optimization and efficiency issues:
When writing all of the collision code, I could probably have made a singular method that just substitutes object1 and object2 with given variables instead of rewriting the collision if and elif statements over and over and over again. I guess hindsight is 20/20. <------ (Over the years of progamming I've done and while doing this project I've realized this statement is VERY VERY true). This same optimization issue also goes for the classes that derived from My_Sprite, as I could've just added all the methods I used in said classes into the My_Sprite class, so I wouldn't have to remake so many methods throughout different classes.