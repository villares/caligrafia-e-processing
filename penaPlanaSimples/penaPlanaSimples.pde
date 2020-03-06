// Mariana Leal

float x;
float y;
float px;
float py;
int larguraPena = 40;

void setup() { 
  size(600, 500);
  smooth();
  background(255);
  //stroke(0);
  //fill(0);
  rectMode(CENTER);
  for (int i = 0; i < height; i = i + 5 * larguraPena){
    stroke(200);
    line(0, i, width, i);
  }
}

void draw() {
  //aqui que acontece o easing
  noStroke();
  float miraX = mouseX;
  float miraY = mouseY;
  x = lerp(x, miraX, 0.1);
  y = lerp(y, miraY, 0.1);
  if(mousePressed){
     fill (x, x / y, y, 50);
     translate(x, y);
     rotate( 5 * PI / 6);
     rect(0, 0, larguraPena, 3, 4, 4, 4, 4);
  }
}
