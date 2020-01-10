Title: The Top 25 Jazz Standards
Date: 2020-02-01

{% from 'markup.html' import h2 %}


Mastering jazz repertoire takes a lifetime of study, and
can sometimes seem overwhelming. There are thousands of
songs to choose from and it can seem like the repertoire
is endless when you’re at a jam session where every song
that gets called is completely new to you.

The good news is, some jazz standards are very much more
important than others.

Some tunes get called often while others are obscure and
come up rarely. Believe it or not, the number of songs
that are called all the time is actually quite manageable
- start with these and you'll be well on your way to being
on familiar territory most of the time.

{{ h2("How do we know it’s these songs?") }}

Lots of people have made lists of these big songs - and
there's a broad consensus - but I wanted something a bit
more objective and data-driven. This is exactly the kind
of problem that’s well suited to a really good spreadsheet.

So for the last 6 months or so I've been keeping a record
of every song that gets called at every session I've played
at so I can take a look at the patterns that emerge.

This sample is of 500+ calls (occasions when a song was
played) at jam sessions in London since mid 2019. This data
reflects my experience - if you go to different sessions
then yours will contrast - but based on research and
conversations, the broad sweep seems relatively consistent.

So what do we learn from the data now it's been collected?

{{ h2("Most songs are called only very rarely") }}

![Chart of call count frequency]({static}/images/512-call-count-freq.png)

In this dataset songs only called once are by far the
largest group. Many of these are relatively obscure tunes
brought by a horn player or singer to one jam session that
probably won't come up again. This long tail behaviour is
what you'd expect given the thousands of jazz songs out
there and the social nature of jazz musicianship.

500 or so is still a relatively tiny sample. You would
expect some of these at least to get called more and climb
up the chart, while the overall shape of the distribution
remained similar.

{{ h2("A relatively small number of songs comprise the majority of calls") }}

If you only knew 10 songs, this would make up 20% of all
calls at jam sessions. If you only knew 25 songs this
would get you to 40%.

![Chart of call count percentage]({static}/images/512-call-count-perc.png)

Getting to the point where you knew every other song requires
you to know 35 songs - which is in fact very manageable. One
of the challenges that face musicians starting out in their
journey to conquer the jazz repertoire is knowing which songs
these are.

To help with that, I've incorporated a list of the "Top 10"
and "Top 25" tunes into this site. These songs are
broadly-speaking driven by this data, although I've
editorialised slightly to make them fit such nice round
numbers and make the lists more approachable.

{{ h2("Top 10 standards (20% of all calls)") }}

* [All Blues](/all-blues.html)
* [Autumn Leaves](/autumn-leaves.html)
* [Black Orpheus](/black-orpheus.html)
* [Blue Monk](/blue-monk.html)
* [Cherokee](/cherokee.html)
* [Corcovado](/corcovado.html)
* [Misty](/misty.html)
* [On Green Dolphin Street](/on-green-dolphin-street.html)
* [St Thomas](/st-thomas.html)
* [Take The A Train](/take-the-a-train.html)

{{ h2("Top 25 standards (40% of all calls)") }}

* [All Blues](/all-blues.html)
* [Autumn Leaves](/autumn-leaves.html)
* [Billie's Bounce](/billies-bounce.html)
* [Black Orpheus](/black-orpheus.html)
* [Blue Bossa](/blue-bossa.html)
* [Blue Monk](/blue-monk.html)
* [Bye Bye Blackbird](/bye-bye-blackbird.html)
* [Cherokee](/cherokee.html)
* [Corcovado](/corcovado.html)
* [Footprints](/footprints.html)
* [How High The Moon](/how-high-the-moon.html)
* [I Wish I Knew How It Would Feel To Be Free](/i-wish-i-knew-how-it-would-feel-to-be-free.html)
* Lucky Southern
* [Misty](/misty.html)
* [Moanin'](/moanin.html)
* [Night In Tunisia](/night-in-tunisia.html)
* [On Green Dolphin Street](/on-green-dolphin-street.html)
* [Softly As In A Morning Sunrise](/softly-as-in-a-morning-sunrise.html)
* [Song For My Father](/song-for-my-father.html)
* [St Thomas](/st-thomas.html)
* [Summertime](/summertime.html)
* [Take The A Train](/take-the-a-train.html)
* [There Will Never Be Another You](/there-will-never-be-another-you.html)
* [Watermelon Man](/watermelon-man.html)
* [Well You Needn't](/well-you-needent.html)

As I carry on collecting data, I’ll be adjusting these to
reflect any changes that come up.

(For instance I would guess
that Stella By Starlight and All The Things You Are end up in
the top 25 and their omission is an indicator that I haven’t
collected enough yet.)

{{ h2("The Top 201 Standards on this site are a good expanded list") }}

Songs from the list on this site comprise some 83% of calls. For
a list that's aiming to be representative of the most important
tunes in the repertoire rather than exhaustive, that feels pretty
decent.

{{ h2("What should I do if I already know these 25?") }}

By the time you know these tunes, it’s time to forge your own path
through the repertoire. While picking common songs is still helpful,
once you have that core set of tunes down, it can also be fun to
pick something a bit more obscure !

If you don’t already have a list of songs you like and want to learn,
I’d suggest listening to the
[master spotify playlist](https://open.spotify.com/playlist/2jCq77SrgiVScSECYfbeDQ?si=efxyUA0tQl6zISYoBWF9fA) of 200+ songs on shuffle and waiting till something
really grabs your ear, then investigating that!


{{ h2("Notes") }}

The raw data underlying this post is
[available in a CSV here](https://github.com/davidmiller/repertoire/tree/master/content/data/512.calls.csv).

It takes in 522 calls from 36 jam sessions since 22 Jun 2019.
