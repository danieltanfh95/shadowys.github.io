-title:p
Summer Cleaning

-body
Posted on 15th May 2014

It's time for cleaning out messy hacks! When I write code sometimes I just had to get the job done first, then clean up, resulting in all the WTFs you can see in [this place](https://github.com/Shadowys/Blitz/tree/master/Assets/BOO/Legacy), prompting the rewrite of the entire code base. Of course, the current rewrite is not perfect and there are still horribly mangled code hiding among the current code, such as [the timer](http://shadowys.svbtle.com/tick-tock), and non-commented code, and a misplaced equals sign in Bullet Handle, which caused the weapon pointer not to cycle correctly, so some cleaning is still needed.
I've also uploaded all the [models](https://github.com/Shadowys/Blitz/tree/master/Assets/Models) so any graphic developer can upload their models into the repository. 
Unfortunately though, I have not completed the rewrite of the GUI components so the current build will only have a rudimentary movements, shooting ability and bird eye's view. 
With a departure from previous concepts, we have new code:

##Zoid (with it's components that should be initialised)

- **Transform**: Initial rotation is 0,0,0
- **Animation**: Default animation is *idle, run, walk, jump, quickstepL, quickstepR*
- **Rigidbody**: Default *mass* is 35. *Use Gravity* flagged true. *Rotation* is frozen across three axes.
- **Motion_Mech**: Script to move zoid.
- **Status_Mech**: Used with individual *colliders* in each machine parts and their respective "*Parts_Mech*" script components.
- **Weapon_Handle**: Used with individual *weapons* as children in the zoid body, with their respective "*Bullet_Handle*" script components, which in turn handles bullets with "*Bullet_Mech*" script components

##Main (created from Empty GameObject)

- **Player View**: *target* is set to the one with "player" tag.
- **Sound Handle**: Used with "Sound_Mech" script component on Speaker prefab to play multiple sounds.
- **Main_Mech**: Script to strip multiple instances of main to one.

##MainCamera (default main camera)

- **Camera_Handle**: Handles states of camera follow.
- **Follow_Mech**: Simple follow script.
- **Bird_Mech**: Enable 360 degree view of the map when camera rotates around zoid.

Currently I have made a machine gun and a missile launcher for testing purposes, and the next agenda on my list is the GUI for showing weapon activated. 

##Weapon (created from empty GameObject)

- **Transform**: Initial local rotation can be 0,0,0
- **Weapon_Mech**: Holds the weapon state, for differentiating the weapon from the body, and the texture for the weapon thumbnail.
- **Bullet_Handle**: Handles the actual shooting of the bullet.

##Bullet (any GameObject with a collider)

- **Rigidbody**
- **Trail Renderer**
- **AudioSource**: Place gunshot sound in here, to be played when the bullet in alive.
- **Bullet_Mech**: Script to process bullet movements, damage dealing, and explosion on impact sounds.

A6yog has informed me that there will be a new coder in our team (Harris Piech), while I've not communicated with him, I'm a little excited at having someone else to help.

Godspeed us all.