# lastfm
Simple command-line program to query last.fm for similar songs/artists.

Imagine that you are playing a song with your preferred music player and you would like to know which songs from your collection are similar to the ones that you are currently playing? This is one of the aspects that I miss the most from Amarok 1.4's "Rediscover your music" experience, since it offered music from my own library to be played and it was usually music that I had already forgotten about that I had (yes, my music library is *huge*).

I briefly described this [feature request with text and screenshots][0] for the [Clementine Music player][1] (which is the spiritual successor of Amarok 1.4), and many people warmly supported my description.

Alas, since then, I have not seen anything like that and, unfortunately, Amarok 1.4 isn't widely distributed (and lacks many other features that we take for granted in current music players, like replaygain support etc.).

So, why not have a script that can automatically take suggestions from Last.fm for what you are currently listening? In the (near) future, I hope to have it feed those suggestions back into your playlist (but this will depend on your music player, of course).


[0]: https://github.com/clementine-player/clementine/issues/1507
[1]: https://www.clementine-player.org/

------

# The original feature request at GoogleCode

Hi there.

It's been a time since I wanted to bring this to the list.

A very appealing thing for me from Amarok 1.4 was the way that I could "rediscover my music" in a way that it could show me connections between artists that I already have in my library.

More specifically, when one opens Amarok 1.4, one sees a summary of the newest albums available in one's collection (see [1]), and scrolling down that section of the screen, the list of the preferred albums in the library (see [2]).

That's what one gets when nothing is being played.

When something is playing, though, things get even more interesting: in the part of the screen where metadata appears in general, there is some information regarding the album, followed by:

* There is a list of artists related to the one that is playing. If you have something by that artist in your library, its name appears in an upright font, while if you don't have anything by the other artists, their names appear in italic.  See [3].

  When you drag the name of the artist to your playlist, the songs of those artists are put into your playlist.

* Also part of the "rediscover your music" experience, right below that, a list of the top rated songs taken from your library, by the artists related to what is playing is show, so that you can drag and drop that.

  Immediately below that, there is a list of favourite tracks by the artist that is currrently playing.

* Lastly, a little bit down is the list of the albums by the artist that is playing, sorted by year, and the list of the songs in those albums, with the thumbnails of the covers. The currently playing music has its name in italic.

  Clicking on a given album toggles the open/closed state of that album, to make the display more compact. See [4].


Is there anybody else that would like to see something similar to this (if not exactly this) in Clementine?


Thanks for any comments,

Rogério Brito

