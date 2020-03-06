// Mariana Leal

import codeanticode.tablet.*;
Tablet tablet;
float miraX, miraY, x, y, px, py;
int strokeColor = 10;

void setup() {
  size(800, 800);
  background(255);
  //noFill();
  noStroke();
  colorMode(HSB, 359);
  strokeCap(ROUND);
  tablet = new Tablet (this);
}
float ellipse_radius;

void draw (){
  miraX = mouseX;
  miraY = mouseY;
  //x = pmouseX;
  //y = pmouseY;
  x = lerp(x, miraX, 0.1);
  y = lerp(y, miraY, 0.1);
  if (mousePressed) {
      stroke(strokeColor, 356, 300);
      strokeWeight(tablet.getPressure() * 40);
      line(x, y, px, py);
    px = x;
    py = y;
  }
  strokeColor += 1;
  if (strokeColor >= 359) strokeColor = 10;
}

void keyPressed() {
  background(0, 0, 359);
}
