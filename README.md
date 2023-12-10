# Turning Kepler Orbits into Ptolemaic Orbits
Back in the olden days, they used to the think the Earth was the center of the universe and every other object was made to travel around it. This view of the universe is incorrect, but humans believed it for thousands of years because that's what it <i>looks</i> like when you're standing on the Earth. The Earth <i>looks</i> stationary to us. This programs takes the standard Sun-centered (heliocentric) orbits and converts them into Earth-centered (geocentric) orbits so you can see the view of the universe as the ancient would have imagined it. It's done with a simple coordinate transformation:

```ruby
Ptolemy[i].pos = Kepler[i].pos - Kepler[Earth].pos
```

Rather than figure out the shapes of the paths, the code just continuously subtracts the Earth's location from the location of the other objects. Might not be very efficient, but it runs smoothly anyway.

## Necessary Software
This program is coded in Python 3.8 using the Visual Python 7 (vpython) package. If you haven't already, install Python then type the following into your command line to add the vpython package:

```
pip install vpython --upgrade
```

You'll also need to download the <a href="https://github.com/ScienceAsylum/Orbital-Transformation/tree/main/Maps">maps</a> because they're used as textures for the planets.

## How to Use
When you first start the program, give it a second to load the Sun and all the planets. Then just click anywhere in the display canvas to start the simulation. The Sun and planets will begin to oribit the Earth, many along curly paths. Those paths will be drawn as the program runs.

<img src="https://github.com/ScienceAsylum/Orbital-Transformation/blob/main/Screenshot.png">

It only includes the Sun, Mercury, Venus, Earth, Jupiter, and Saturn because those are the objects that ancient Greeks (like Ptolemy) knew about. Distances are to scale, but object sizes are not (for visibility reasons).

## Room for Improvement
I think the animations turned out well, but I had to approximate the orbits as perfect circles because I ran out of time. I'd love to make the orbits ellipses and include orbital parameters (like inclination) to make it more accurate.

## Purpose of the Project
I was making a YouTube video about the history of Earth-centered models (geocentrism) and why calling it &quote;incorrect&quote; is a bit too harsh.

<a href="https://youtu.be/yC74lhJX9Ck">
    <b>How can Planets be in Retrograde? Geocentrism Explained</b></br>
    <img src="https://img.youtube.com/vi/yC74lhJX9Ck/mqdefault.jpg">
</a>

## License
This code is under the <a href="https://github.com/ScienceAsylum/Orbital-Transformation">GNU General Public License v3.0</a>.
