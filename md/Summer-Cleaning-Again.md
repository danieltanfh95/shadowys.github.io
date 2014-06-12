Posted on 10th June 2014

June 16th. The day of reckoning. We're going to launch a community alpha release on that day, so everything should be as prim and proper before we step out to the world and say, "Here's the game!".

And that includes the dev base, which also includes the codebase. Just a week before, we've got Lee, who is an [indie Unity3d dev](https://www.kickstarter.com/projects/quickfix/magic-meisters-a-co-op-magical-action-rpg-for-pc-m), with plenty of experience come and help out. While he haven't contributed code yet, he has already provided valuable experience into improving the game. :D

After some back and forth, I was finally convinced to port the entire codebase from Boo to Csharp, for two reasons in particular, NGUI, the future of Unity GUI (may change in Unity 4.6 though) and the main inclination of the community of Unity3d development. I still have misgivings about C sharp as a language (LINQ, and compiler type inference, in particular, as I have to use them in place of comprehensions and duck typing.), though it is relatively simple to port the code from Boo to C sharp. 

Just add tons of compiler needed braces and semicolons and typings (var can't be used outside its scope.) and casts ( no idea why don't generics do generic stuff...why does GetComponent(typeof(fooclass)) still needs to be casted is beyond me, but a [quick google](http://answers.unity3d.com/questions/358992/c-getcomponent-result-error-cast.html) shows C sharp generics are more closer to Java than to C++/D generics, so there goes the execution penalty without casting...) and you're mostly done! That said, the editor is much optimised for Csharp (helpful completions here and there once everything is typed.) than Boo (not that I needed it when coding in Boo anyway...) so everything is quite easy once the workflow settles in.

Now that I'm using full fledged C sharp (not minding the generics yet, oh my how I enjoy the D templates), I hope the unity community are much inclined to develop the game, even at the (I hope) minor cost of readability and extraneous syntax for the parser...

We've already got Lee and Kam, another enthusiastic fellow who shows great commitment and has contributed his first code :D , a spinner for the WIP sign. 

Well, apart from all that coding stuff, I cleared the unused asset resources, and while it was apparent that there were still many texture and sounds, the compilation time has already decreased from a minute to 10 seconds (changing from Boo to C sharp sped it up a little before, but this is amazing)

Cheers! Hopefully it will well received by the community. 