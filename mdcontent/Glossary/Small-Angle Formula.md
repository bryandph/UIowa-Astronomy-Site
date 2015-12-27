Small-Angle Formula
====================
<div class='well'>
<img class='img-responsive img-rounded' style='background-color: #777' src="/static/mdcontent/angularvslinear_med.png" alt="angularvslinear">
</div>
In astronomy, the sizes of objects in the sky are often given in terms of their angular diameter as seen from Earth, rather than their actual sizes.  For a given observer, the distances $D$, $d$, and angle $θ$ in radians (as portrayed in the picture above) form a right triangle with the trigonometric relationship:

$$\tan \theta = \frac{d}{D}$$

Since these angular diameters are often small, we can use the small angle approximation which will give us:

$$\tan \theta \approx \theta $$

Since $\theta$ is in units of **radians**, we often need to convert our measurements into units of degrees.  One radian is $\frac{180}{\pi} \approx 57.3^{\circ}$. So we can rewrite our small angle approximation as:

$$\frac{d}{D} = \frac{\theta}{57.3^{\circ}}$$

When dealing with astronomically distant objects, where angle sizes are extremely small, it is often more practical to present our angles in terms of arcseconds, which is 1/3600th of one degree.  Since one radian equals $\frac{3600 \cdot 180}{\pi} \approx 206265\,arcseconds$, we can again rewrite the small angle formula as:

$$\theta_{arcseconds} = 206265 \frac{d}{D}$$

Since it is easy to measure the angular size of astronomical objects, we often use this to solve for other unknowns, such as the distance or the diameter of a celestial body.  If two objects are roughly the same distance from the observer, you can also use the formula to find the distance between the two objects.


Example:
--------

On August 27, 2003, Mars made the closest approach to Earth in recorded history due to a near synchronization of Earth being at aphelion (furthest orbital point from the sun) and Mars being at perihelion (closest orbital point from the sun). The distance between the planets that day was a mere `55.8 million km`.  Observations of Mars were quite easy to do that night, since the angular diameter of the planet was observed to be about `25.1 arcseconds`. Given this information, find the diameter of the red planet.


Solution:
---------

$\theta = {25.1}''$


$D = 55.8\,million\,km\;= 55.8 \times 10^{6}\, km\; = 5.58 \times 10^{10}\, m$


$${25.1}'' = 206265 \frac{d}{5.58 \times 10^{10}\, m}$$

$$d = \frac{{25.1}''}{206265} \cdot (5.58 \times 10^{10}\, m) = 6.67 \times 10^{6}\, m$$

So the planet's diameter is about `6790 km`, which is a little more than half the diameter of Earth.
