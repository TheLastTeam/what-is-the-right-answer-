# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the name of the character.
define q = Character(_("QT-1"), color="#c8ffc8")
define m = Character(_("Me"), color="#c8c8ff")

# The game starts here.
label start:

    # Show a background.
    scene bg sahara
    with fade

    # These display narration and thougts.
    "You wake up on the sand with a slight dizziness and your limbs still numb, all that is around you is an empty desert as far as the eye can see"
    "Under the sky there are only you ... you and that robot next to you. You approach him and surprisingly he speaks to you in your same language"

    scene bg sahara
    with fade
    # This shows a character sprite.
    show qt normal
    # These display lines of dialogue.
    q "I see that you have finally woken up, it is time to go out to explore the universe"
    "After seeing your surprised face, the machine decides to introduce itself"
    q "My name is QT-1 and I will be your guide throughout this journey"

    scene bg sahara
    with fade
    show qt normal
    "Stunned you still decide to ask that robot some questions"
    m "Where are we?"
    q "This is our home planet, or at least what's left of it. What you see now is the result of the last world war"
    m "Where are the others?"
    q "You are the last survivor of your species, right now your mission is to search for intelligent life and prevent them from having the same fate as this planet"
    m "Where are we going?"
    q "We don't have a particular goal, just travel until we find life"
    "With no other question to ask, you decide to continue"
    q "Okay, it's time to prepare the launch site"

    scene black
    with dissolve
    "After saying this, start shaking as the ground separates in front of you"
    "Once everything is over you get closer to discover a space rocket under the sand. that slowly rises to be in front of you"

    scene bg rocket
    with fade
    show qt normal:
        xalign 1.0 yalign 1.0
    q "I guess it's something you've seen before, but do you know how it works?"
    q "You can see a rocket as something that accelerates itself thanks to the thrust generated while expelling its own mass."
    q "The forces acting on a rocket change dramatically throughout its flight."
    q "The propellant is constantly consumed so the weight of the rocket changes"
    show equation ideal_rocket:
        xalign 0.0 yalign 0.5
    q "This is the ideal rocket equation"
    q "This rocket has a speed u, a mass M that changes every moment, its weight (mass by gravity) acts in the direction of a"
    q "It also loses a small amount of mass dm that is expelled with a velocity v"
    q "This velocity v can be obtained as the value of the acceleration of gravity multiplied (g0) by the specific impulse (isp)"
    q "MR is the mass ratio of the propellant, mf represents the mass of the rocket when it takes off and has all its propellant, and me is the mass of the rocket once all the propellant is exhausted"
    q "For example, an MR of 30 tells you that 70 \% of the rocket's mass on liftoff is propellant and the other 30 \% is structure, payload, and so on."
    q "Then, the maximum change in speed of the rocket \u0394u, is equal to the speed v multiplied by the natural logarithm of MR"
    q "For example, if you have MR = 10, g0 = 9.81, and ISP = 350, what is the value of \u0394u that you get?"

    menu:
        q "¿What is the right answer?"
        "7905 m/s":
            q "Right"
        "790.5 m/s":
            q "Wrong, the right answer is 7905 m/s"
        "79.05 m/s":
            q "Wrong, the right answer is 7905 m/s"
        "7.905 m/s":
            q "Wrong, the right answer is 7905 m/s"

    scene bg inside_rocket
    with fade
    "Once inside you wonder what speed the rocket needs to reach to go out into space, so you ask QT"
    show qt normal:
        xalign 1.0 yalign 1.0
    show im orbit:
        xalign 0.0 yalign 0.0
    q "To explain it, let's first talk about what an orbit around a planet looks like. The orbits have the shape of an ellipse and the planet is in one of the foci of the ellipse"
    q "A satellite has a position in which it is closest to the planet, called periapsis, and a position in which it is farthest from the planet, called apoapsis"
    q "If you see the formula you have \u03bc which is known as the standard gravitational parameter. This value is equal to the multiplication of the mass M of the planet and G the constant of gravity"
    q "You also have r which is the distance from the center of the Earth to the satellite and a which is the value of the semi-major axis of the orbit"
    q "The semi-major axis is equal to (periapsis distance + apoapsis distance) / 2"
    q "So if you have a planet with \u03bc = 3.986e14, an orbit with a periapsis of 6771 km, an apoapsis of 6871 km, what is its speed at the periapsis?"
    menu:
        q "¿What is the right answer?"
        "7700 m/s":
            q "Right"
        "770 m/s":
            q "Wrong, the right answer is 7905 m/s"
        "9408 m/s":
            q "Wrong, the right answer is 7905 m/s"
        "7588 m/s":
            q "Wrong, the right answer is 7905 m/s"

    q "Sounds like a lot of speed, right? However, it is not necessary to reach it when using a multi-stage rocket, just like this one."
    show im stage_rocket:
        xalign 0.0 yalign 0.5
    q "You can imagine a two-stage rocket as if you had one rocket on top of another. When the first rocket exhaust its propellant it just separates and now the other rocket ignites"
    q "Thanks to this, the second rocket or second stage is in different conditions of pressure, height, mass and initial velocity."
    q "This facilitates the acceleration of the rocket to reach its altitude and final speed"

    scene bg inside_rocket
    with fade
    show qt normal
    m "That's the way to get out into space, but we'll still be drawn to the planet, right?"
    q "Exactly"
    m "So what do we do to escape Earth's gravity?"
    show qt normal:
        xalign 1.0 yalign 1.0
    show im paths:
        xalign 0.0 yalign 0.5
    q "There are three types of routes that we can follow\:"
    q "The elliptical path, which is a closed path, with which we orbit around the Earth and it is not what we want at the moment"
    q "Hyperbola path, which is an open route, with which we can get away from the planet and make an interplanetary flight"
    q "The parabola path, which is an open path, can be considered the limit between the ellipse and the hyperbola"
    m "Do we need to reach a certain speed to achieve the hyperball path?"
    show im escape_vel:
        xalign 0.0 yalign 0.5
    q "We need to reach the escape velocity of the planet"
    q "\u03bc is the standard gravitational parameter (3.986e14) and r is the distance we are from the center of the planet"
    q "Knowing the value of \u03bc and that we are 6371 km from the center of the planet, what escape velocity do we need?"
    menu:
        q "What is the right answer?"
        "11.186 km/s":
            q "Right"
        "111.86 km/s":
            q "Wrong, the right answer is 7905 m/s"
        "7.909 km/s":
            q "Wrong, the right answer is 7905 m/s"
        "79.09 km/s":
            q "Wrong, the right answer is 7905 m/s"
    show qt normal
    q "So let's start the countdown and take off to start this journey"

    scene bg rocket_launch
    with fade
    "Once the count reaches 0 you start to feel the vibration of the takeoff, the acceleration makes you stick towards your seat as it increases"
    "You close your eyes as you feel each stage of the rocket separate until ..."

    scene black
    with dissolve
    show qt normal
    q "Welcome to microgravity, it must be your first time experiencing it. Soon you will get used to it."

    scene bg stars
    with fade
    "Looking out the window you can see your home planet and the stars, hundreds, maybe thousands of them."
    "A flash catches your attention and you can see that it is another ship, much larger, moving. Before you can ask anything QT says"

    scene bg space_station
    with fade
    show qt normal:
        xalign 1.0 yalign 1.0
    q "It is the Space Station, it works in automatic mode and it will continue to do so for years before being attracted by the planet and crashing against its surface"
    q "Previously it was used to carry out experiments and there was always a crew on board"
    m "How did they send crew to the Space Station?"
    q "If you send a ship to an orbit lower than the Station you can get closer little by little by means of transfer maneuvers"
    q "Do you remember the terms of periapsis and apoapsis?"
    q "What is the periapsis in the orbit of a satellite?"
    menu:
        q "What is the right answer?"
        "The point where it is closest to the planet":
            q "Right"
        "The point where it is furthest from the planet":
            q "Wrong"
    show im transfer:
        xalign 0.0 yalign 0.5
    q "Well, if you start the engine during periapsis by increasing the speed of the ship, then you will make an orbit change to an orbit with a higher apoapsis"
    q "In this way you can go from one orbit to another until you are in the same orbit of the Space Station"
    q "In fact, if you decrease the speed instead of increasing it in the periapsis, you will be able to enter an orbit with a lesser apoapsis."
    q "Once the ship is close to the Space Station, docking is next."
    q "Being in the same orbit and with the same speed, if the spacecraft gets close enough to the Space Station, a robotic arm can be used to capture the spacecraft"

    scene bg stars
    with fade
    show qt normal:
        xalign 1.0 yalign 1.0
    "QT also mentions the fact that in addition to the Space Station there are also dozens of satellites orbiting the planet in different orbits"
    show im orbits:
        xalign 0.0 yalign 0.5
    q "There are different types of orbit. They can be at different heights and/or with different inclinations. Each orbit has its advantages and disadvantages compared to the others."
    q "It is easier and cheaper to get to the low orbits, but from the surface of the planet it becomes difficult to follow those in these orbits."
    q "Also in low orbits they have a smaller coverage area than satellites at higher altitudes"
    q "Being closer to the surface, the time it takes for a signal to travel from the satellite to the surface (latency) is shorter."
    q "Depending on what you want to do with the satellite, there will be better or worse orbits where to place it"
    m "How long does it take for a satellite to go around the planet?"
    show im orbit_period:
        xalign 0.0 yalign 0.5
    q "The time it takes to give a complete orbit to the planet depends on the altitude at which it is located"
    q "Do you remember the meaning of a and \u03bc?"
    menu:
        q "What is the right answer?"
        "a si the apoapsis and \u03bc is the standard gravitational parameter":
            q "Wrong, a is the semi major axe and \u03bc is the standard gravitational parameter"
        "a is the semi mahor axe and \u03bc is the gravitational constant":
            q "Wrong, a is the semi major axe and \u03bc is the standard gravitational parameter"
        "a is the apoapsis and \u03bc is the gravitational constant":
            q "Wrong, a is the semi major axe and \u03bc is the standard gravitational parameter"
        "a is the semi major axe and \u03bc is the standard gravitational parameter":
            q "Right"
    q "So with this equation you can calculate how long it takes a satellite to complete an orbit around the planet"
    m "So there is an orbit with an orbital period equal to the rotation period of the planet?"
    q "That's right, this orbit is known as a stationary orbit. Thanks to this, it will seem to someone on the surface of the planet that this satellite is always at the same point"
    q "This has advantages in communications since it can communicate with an antenna that is always pointing to the same place"
    q "Why don't you try to calculate the value of a for a geostationary orbit? We know that \u03bc = 3.986e14 and let's say the period is T = 86164 seconds"
    menu:
        q "What is the right answer?"
        "4216.4 km":
            q "Wrong, the right answer is 42164 km"
        "42164 km":
            q "Right"
        "421640 km":
            q "Wrong, the right answer is 42164 km"

    scene bg satellites
    with fade
    show qt normal:
        xalign 1.0 yalign 1.0
    m "If the notion of up and down does not exist in space, how do you know the position of a satellite?"
    "Here is the explanation of the alt-az, ecliptic, elliptical, galactic reference systems"

    "While you travel to escape the gravity of the Earth QT proposes you to carry out some of the experiments that were carried out in the Space Station"
    q "We have an incubator and some bacterial cultures, all you have to do is adjust the temperature and move the element that gives them heat inside the incubator"
    q "It is a simple but important task. This can help us understand how interstellar travel affects, and all that this entails, simpler forms of life"
    "QT teaches you how to use the incubator and now you are ready to carry out this experiment"
    "You hear the incubator alarm, it's time to adjust the temperature of the cultures"

    scene bg inside_spaceship
    with fade
    "You decide to ask QT how you can travel from one planet to another within the solar system, to which he explains first the concept of sphere of influence"
    show qt normal:
        xalign 1.0 yalign 1.0
    show im soi:
        xalign 0.0 yalign 0.5
    q "Each planet has a sphere of influence, that is, around it there is a spherical region where the main gravitational influence is that of the planet itself"
    q "Logically it is not a perfect sphere and the change is not abrupt but it is a good approximation"
    q "a as always is the semi-major axis, m is the mass of the smallest object (the planet) and M is the mass of the largest object (our Sun)"
    q "We know that for our planet and our Sun, a = 149.6e6km, m = 5.9722e24 kg and M = 1.989e30 kg, what is the sphere of influence of our planet?"
    menu:
        q "What is the right answer?"
        "9.24e6 km":
            q "Wrong, the right answer is 0.924e6 km"
        "11.76e6 km":
            q "Wrong, the right answer is 0.924e6 km"
        "1.176e6 km":
            q "Wrong, the right answer is 0.924e6 km"
        "0.924e6 km":
            q "Right"
    scene bg inside_spaceship
    with fade

    show qt normal:
        xalign 1.0 yalign 1.0
    q "During this trip we will fly over two of the planets of this solar system"
    show im interplanet:
        xalign 0.0 yalign 0.5
    q "An interplanetary flight is carried out in this way, first the ship is orbiting a planet. A maneuver is carried out by starting the engines to leave the planet's sphere of influence"
    q "Now the new orbit must coincide with the sphere of influence of the target planet to be captured by its force of gravity"
    q "What we will do is not be captured by the planet but use its gravity to perform a maneuver known as gravity assist"
    q "As we pass close to the planets, their gravity will change our orbit and our speed will increase, with this we save fuel and we will leave the solar system faster"
    "Here is the explanation of the gravity assist and aerobraking"
    "You hear the incubator alarm, it's time to adjust the temperature of the cultures"

    scene bg inside_spaceship
    with fade
    "During the trip you ask him some questions about the habitability of the spacecraft and the effects on the body"
    "Here is the explanation and questions about the effects of space travel on the body, how to get food, water, oxygen, etc."

    scene bg inside_spaceship
    with fade
    "As the journey continues, you ask QT how the ship does to find its bearings and where it is."
    "Here is the explanation and questions about orientation and navigation: startrack, spin, gyroscope, reaction wheel, etc"

    scene bg inside_spaceship
    with fade
    "Continuing the journey you have a question for QT"
    m "If possible, how would we communicate with our planet?"
    show qt normal:
        xalign 1.0 yalign 1.0
    q "Our planet had a deep space communication network to always be in contact with its ships and satellites"
    show im dsn:
        xalign 0.0 yalign 0.5
    q "Broadly speaking, the idea is simple, by placing antennas every 120 ° you can cover all directions and ensure that any spaceship and satellite can always communicate with at least one antenna."
    show im dsn_2:
        xalign 0.0 yalign 0.5
    q "They were pretty imposing antennas to look at. Sadly, like the rest of the planet, only ruins remain"

    scene bg inside_spaceship
    with fade
    "At this point you are close to leaving the solar system, probably never to return."
    "You take a last look at the solar system, the one where once there was a race capable of sending spaceships to other planets and with plans to colonize it, but which self-destructively during a war"

    scene bg inside_spaceship
    with fade
    "Once outside the solar system you have doubts about how they will reach other stars, considering the distance that separates them it would take too long"
    "Here is the explanation and questions about engines such as the Tokamak, nuclear fusion engines, curvature engine, etc."

    scene bg orion
    with fade
    "When looking out the window you can see many stars, three of them especially attract your attention because they are arranged in the same row"
    show qt normal
    q "What you see is known as a nebula. Thanks to the gas and dust clouds, many new stars are being born. Protoplanetary disks are also observed around several stars."
    q "I can't pick up signs of intelligent life, but maybe in the future it will be a place full of life."
    q "I see that those 3 stars caught your attention. If there is life nearby, they can probably see them and have given them a special meaning"
    "If there are no signs of life that QT can identify, it is best to move on."
    "You hear the incubator alarm, it's time to adjust the temperature of the cultures"

    scene bg inside_spaceship
    with fade
    "As the journey continues, you want to learn more about how the spaceship works. This time you decide to ask about the spaceship's telecommunications system."
    show qt normal:
        xalign 1.0 yalign 1.0
    q "Let's start from the basics. Here we have an electromagnetic wave"
    show im ondas:
        xalign 0.0 yalign 0.5
    q "The first thing you can see is that a wave is represented by its amplitude, its period (seconds), its frequency (Hz) and its wavelength (m)"
    q "The higher the frequency, the more repetitions there will be of a wave in a certain period of time"
    q "An electromagnetic wave in turn is made up of an electric field wave and a magnetic field wave, perpendicular to each other"
    q "For this type of waves, their speed is the same as the speed of light c = 300,000 km/s"
    q "So if you have a 2.4 GHz wave, what is its period and wavelength?"
    menu:
        q "What is the right answer?"
        "T = 416.66e-12 s   \03bb = 125e-3 m":
            q "Right"
        "T = 416.66e-9 s   \03bb = 125e-6 m":
            q "Wrong, the right answer is T = 416.66e-12 s   \03bb = 125e-3 m"
        "T = 125e-12 s   \03bb = 416.66e-3 m":
            q "Wrong, the right answer is T = 416.66e-12 s   \03bb = 125e-3 m"
        "T = 125e-9 s   \03bb = 416.66e-6 m":
            q "Wrong, the right answer is T = 416.66e-12 s   \03bb = 125e-3 m"
    q "The frequency to be used depends on many factors: the application, the regulations, the distance at which you want to transmit, the possible attenuations for each frequency, etc."

    scene bg inside_spaceship
    with fade
    show qt normal:
        xalign 1.0 yalign 1.0
    q "An antenna is responsible for transmitting and receiving electromagnetic waves, thanks to them we could communicate from our planet with spaceships sent to other planets"
    q "An important aspect of antennas is their directivity. It is a way of indicating how concentrated the radiation is in the same direction"
    show im antenna_dir:
        xalign 0.0 yalign 0.5
    q "Here we have a dipole antenna and a parabolic antenna, which are two basic antennas used in spacecraft"
    q "The dipole antenna transmits in all directions on the same plane, so we can receive or transmit in a wide range without worrying so much about a particular direction"
    q "A satellite dish receives or transmits at a very small angle, so it must be well oriented and aligned so that the link is not lost"
    q "While antennas are an important part of the telecommunications system, we also have oscillators, amplifiers, encoders, and many more equally important components."

    scene bg sirius
    with fade
    "After traveling further, you can observe two stars up close. One of them is really bright compared to the other."
    show qt normal
    q "It is a binary star system. It means that both stars orbit a common point"
    q "The star that shines the least is known as a white dwarf. A star that has exhausted its nuclear fuel and a taste of the fate that awaits most of the stars we see."
    q "The other star is much brighter and larger. There is no doubt that if life exists nearby, they should consider this star as one of the brightest in their sky."
    q "However, again I am not picking up any signs of intelligent life. We must keep moving forward."
    "Without more to say, the journey continues"
    "You hear the incubator alarm, it's time to adjust the temperature of the cultures"

    scene bg inside_spaceship
    with fade
    "Continuing with the journey, you ask QT how he knows whether or not there is intelligent life in the stars you have visited"
    show qt normal:
        xalign 1.0 yalign 1.0
    show im noise:
        xalign 0.0 yalign 0.5
    q "When pointing the antennas towards the stars that we have seen, generally only noise will be received"
    q "But if a pattern or order is identified when processing it, it may indicate the fact that the signal is artificially generated"
    show im modulation:
        xalign 0.0 yalign 0.5
    q "For example, a signal that keeps its frequency constant while varying its amplitude may indicate an AM modulated signal"
    q "Or a signal that keeps its amplitude constant while its frequency varies may indicate an FM modulated signal"

    scene bg inside_spaceship
    with fade
    show qt normal:
        xalign 1.0 yalign 1.0
    show im am:
        xalign 0.0 yalign 0.5
    q "So what kind of modulation is shown?"
    menu:
        q "What is the right answer??"
        "Amplitude modulation":
            q "Right"
        "Frequency modulation":
            q "Wrong"

    scene bg inside_spaceship
    with fade
    show qt normal:
        xalign 1.0 yalign 1.0
    q "But this is only an indication, when we find a planet we can study its atmosphere from afar"
    q "Since we are looking for life like that of our planet, we are in search of a planet with water, nitrogen and oxygen. Or that does not contain an excess of elements that we consider harmful"
    show im spectroscopy:
        xalign 0.0 yalign 0.5
    q "For this we use spectroscopy"
    "Here is the explanation and problem about spectroscopy"

    scene bg alphacen
    with fade
    "You happen again near a pair of quite bright stars, or that is what you think until QT tells you that it really is a triple star system"
    show qt normal
    q "The star you can't see is known as a red dwarf. In fact, they are very common in this galaxy, they just aren't easy to see with the naked eye."
    q "Apparently this red dwarf has planets orbiting it ... but the amount of radiation that emanates from it makes it very unlikely that there is life on those planets"
    "After adjusting the antennas and analyzing the data for intelligent life, QT confirms the fact that there is no intelligent life in this star system either."
    "Without more to say, the journey continues"
    "You hear the incubator alarm, it's time to adjust the temperature of the cultures"

    scene bg inside_spaceship
    with fade
    "After so much time traveling you wonder how everything is still working perfectly and the possibility of failures"
    "Here is the explanation and problems about energy sources: solar panels, nuclear reactor, etc."
    "Here is the explanation and problems about the effects of radiation on electronic components"

    scene bg solar_system
    with fade
    "The ship is approaching a star, although it could be considered small, there is a possibility that there is life nearby"
    "When observing in more detail, 8 planets can be counted revolving around it, especially that giant gaseous planet or next to it the planet with rings stand out"
    "You direct the antennas towards that solar system and you pick up apparently artificial signals coming from it, especially from one of the planets, third from the sun"
    "QT goes to the controls and adjusts the frequency with which these signals are received, after a moment it turns to you to tell you"
    show qt normal
    q "We just found intelligent life, at least enough to send signals into space"
    "With an adjustment in the navigation system they set course for your first destination"

    menu:
        "Due to time constraints, we do not implement the full point system, so..."
        "Choose the ending"
        "Bad ending":
            jump bad_end
        "Good ending":
            jump good_end
        "True ending":
            jump true_end

label bad_end:
    scene bg earth_bad
    with fade
    "The spaceship is heading directly towards that third planet, which stands out for its reddish orange color"
    q "The radiation readings coming from the planet are alarming, I hope we arrived in time"
    "Fearing the worst you decide to land on the planet"
    "You land the ship near the radio source with the highest power. The landscape is bleak and you prepare for the worst before descending from the ship."
    scene bg bad_end
    with fade
    "When you leave the first thing you see is the structure of a huge building half sunk in the sand, in front of it there is a pedestal where the following is inscribed"
    "\"UniverseX. We make space available to everyone\""
    "Of that colossal wreck, boundless and bare, the lone and level sands stretch far away"
    show qt normal
    q "We are late, apparently a nuclear war extinguished all life in this place, just as it happened on our planet"
    scene bg inside_spaceship
    with fade
    "You and QT return to their ship and leave that planet, before leaving you decide to see it one last time and ask QT if it managed to discover what that powerful signal you received was saying"
    show qt normal
    q "It was a message of a single word directed to all directions in space and that was repeated over and over again ... it said \"Help\""
    scene bg inside_spaceship
    with fade
    "You start the engines to get out of the solar system, thinking that this time you have been late, but maybe next time you will have more luck"
    "You are moving away from that solar system where intelligent life once existed, intelligent enough to send a message of aid to space as a last desperate attempt to survive after a war of which no survivors were left"
    "You hear the incubator alarm, it's time to adjust the temperature of the cultures"
    "{b}Bad Ending{/b}."
    # This ends the game.
    return

label good_end:
    scene bg earth_normal
    with fade
    "The ship is heading directly towards that third planet, which stands out for its blue and reddish orange color"
    "In addition, it highlights the fact that it is surrounded by a large layer of what appear to be orbiting satellites"
    "QT, who was somehow able to learn his language just by listening to his broadcasts tells you"
    show qt normal
    q "It seems that they have discovered us and are trying to communicate with us"
    scene black
    with dissolve
    "By accepting the transmission, a subject of the race that lives on that planet appears on the screen"
    "After a long conversation between QT and that being, QT summarizes the current situation of the planet"
    scene bg inside_spaceship
    with fade
    show qt normal
    q "The individual who contacted us is called D. Bowman, he is the leader of Diaspar, apparently it is the last city on the planet since all the communication attempts from him have been in vain"
    q "They are the last survivors of the so-called Third World War, they believed they were sentenced to die in Diaspar until they saw us arrive"
    m "You have to land fast in the city"
    q "Sorry, I'm afraid I can't do that ..."
    scene bg kessler
    with fade
    show qt normal:
        xalign 1.0 yalign 1.0
    q "During the war they chose to destroy the enemy's communication satellites, the fragments generated caused a cascade reaction so now there is too much space debris orbiting"
    q "This complicates getting in and out of the planet, it is something they call Kessler Syndrome"
    "Despite the problems, you know that with QT close, it is only a matter of time to help this planet and get its inhabitants to leave their planet"
    "Maybe they spread throughout their solar system, maybe they reach other stars and why not? Get to know other galaxies and much beyond."
    "You hear the incubator alarm, it's time to adjust the temperature of the cultures"
    "{b}Good Ending{/b}."
    return

label true_end:
    scene bg earth_true
    with fade
    "The ship is heading directly towards that third planet, which stands out for its blue and green color"
    "Also QT surprises you saying"
    show qt normal
    q "It seems that the race that lives in this solar system has managed to expand. From the amount of information it originated on the third planet"
    q "But they have bases on their Moon, on that fourth red planet, they extract products from asteroids, they have satellites and robots in most of the bodies of the system and even several unmanned spacecraft heading to different stars"
    "QT, who was somehow able to learn his language just by listening to his broadcasts tells you"
    q "It seems that they have discovered us and are trying to communicate with us"
    scene black
    with dissolve
    "By accepting the transmission, a copy of the race that lives on that planet appears on the screen. After a long conversation between QT and that being, QT summarizes the current situation of the planet"
    scene bg inside_spaceship
    with fade
    show qt normal
    q "The person who contacted us is called Dr. Susan Calvin, president of the Terrestrial Federation. She is interested in receiving us to know our history, in addition that our technology can help them expand throughout the galaxy"

    scene bg inside_spaceship
    with fade
    "Back to the ship after a long meeting where they learned many facts about this planet such as its composition, its history, its rotation and translation cycle, you and QT decide to help them"
    "Apparently it is a species that develops exponentially, so learning (perhaps also improving) your technology will not take them long"
    "After that you plan to continue exploring in search of new species to help"

    scene bg inside_spaceship
    with fade
    "As you rest back on the ship, QT tells you"
    show qt normal
    q "They have an interesting theory called Great Filter, it basically says that there is a barrier to the evolution of intelligent life"
    q "For example, the self-destruction of the species through its own technology ... as it happened on our planet"
    q "That would also explain why this is the first planet with intelligent life that we found despite traveling near dozens of stars"

    scene bg stars
    with fade
    "Before you can ask a question, QT points to the stars"
    show qt normal
    q "Each one of them is an incubator. They keep the temperature at the desired degree. For different experiments, different temperature"
    q "And the planets that surround them are huge crops that contain different nutrient mixtures and different forms of life. They focus the sun up and down, and we try to find out the physics that moves it"
    "You think it is impossible that there is someone who can move the sun at will, but QT continues"
    q "The sun is like a heating element in an incubator. Do you think bacteria know what moves the heat that reaches them?"
    q "They may also develop their theories. Life grows without knowing why, they obey the so-called laws of Nature that are only their interpretation of the incomprehensible forces that have been imposed on them"

    scene bg earth_true
    with fade
    "Do you remember what QT mentioned earlier, could it be that great filter is….?"
    show qt normal
    q "Humans on this planet research bacteria and viruses, however, they are also afraid of them and can kill them if they become dangerous"
    q "Could it be that great filter is provoked? A way to get rid of those life forms that have left its culture and even its incubator?"
    q "You are the last survivor of a great filter and now you are here helping a species that took 50 years to go from flying their first plane to carrying a manned mission to their satellite and another 100 years to disperse throughout their solar system "

    scene bg inside_spaceship
    with fade
    "Is QT right? Is life as you know it nothing more than an experiment of a being that you cannot even imagine?"
    show qt normal
    "You observe him thinking one last thing, how then is the existence of QT explained?"
    "He turns to look at you… is there life and consciousness behind those eyes?"
    q "All this time you have believed that both you and all humanity living on this planet are alive thanks to a natural process"
    q "While you think I am an artificially created lifeless robot, but"
    q "What is the right answer...?"
    scene black
    with dissolve
    "You hear the incubator alarm, it's time to adjust the temperature of the cultures"
    "{b}True Ending{/b}."
    return
