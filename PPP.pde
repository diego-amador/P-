//Note: scale function results in error for processing.js.
//If working in processing GUI, uncomment scale line in draw.

//To make a custom equation, place it in the graph class's equation function
Graph graph;
PFont font;
PVector pos;
boolean locked = false;
float xOffset = 0;
float yOffset = 0;
float ySineOffset = 550;
float xSineOffset = 990;
float scale = 1;

int xspacing = 16;   // How far apart should each horizontal location be spaced
int w;              // Width of entire wave

float theta = 0.0;  // Start angle at 0
float amplitude = 75.0;  // Height of wave
float period = 500.0;  // How many pixels before the wave repeats
float dx;  // Value for incrementing X, a function of period and xspacing
float[] yvalues;  // Using an array to store height values for the wave

void setup() {

  fullScreen();
  font = createFont("Consolas", 50);
  textFont(font, 15);
  pos = new PVector(width/2, height/2);
  textAlign(CENTER);
  graph = new Graph(-1, 0, 10);
  //rectMode(CENTER);
  strokeWeight(2);
  noFill();
  
  //SINEWAVE
   w = width+90;
  dx = (TWO_PI / period) * xspacing;
  yvalues = new float[w/xspacing];
  //END_SINEWAVE
}

void mousePressed() {
  locked = true;
  xOffset = mouseX-pos.x; 
  yOffset = mouseY-pos.y;
}

void mouseDragged() {
  if (locked) {
    pos.x = mouseX-xOffset; 
    pos.y = mouseY-yOffset;
  }
}

void mouseReleased() {
  locked = false;
}

void draw() {
  background(0);
  translate(pos.x, pos.y);
  textSize(20);
  graph.displayGrid();
  
  calcWave();
  renderWave();
}

class Graph {
  ArrayList<PVector> points = new ArrayList<PVector>();
  float[] variables = new float[3];
  float increment = 0.1; //the smaller, the more accurate
  float range = 100;
  float graphincrement = 50;
  float scale = 10; //scaled down by 10

  Graph(float a, float b, float c) {
    variables[0] = a;
    variables[1] = b;
    variables[2] = c;

    //y = a*x^2 + b*x + c

    for (float i = -range; i < range+increment; i += increment) {
      if ((i > -range*10) && (i < range*10)) {
        PVector p = new PVector(i, equation(i));
        p.mult(scale);
        points.add(p);
      }
    }
  }

  float equation(float n){
    //put equation here
    return -variables[0]*pow(n, 2) - variables[1]*n - variables[2];
    
  }

  void displayGrid() {
    textSize(15);
    for (float x = -range*10; x < range*10+graphincrement; x += graphincrement) {
      if (x == 0) {
        strokeWeight(5);
        stroke(255, 200);
      } else {
        strokeWeight(2);
        stroke(255, 100);
      }
      line(x, -range*10, x, range*10);
      text(round(x/scale), x, -15);
    }
    for (float y = -range*10; y < range*10+graphincrement; y += graphincrement) {
      if (y == 0) {
        strokeWeight(5);
        stroke(255, 200);
      } else {
        strokeWeight(2);
        stroke(255, 100);
      }
      line(-range*10, y, range*10, y);
      text(round(-y/scale), -15, y);
    }
  }
}

void calcWave() {
  // Increment theta (try different values for 'angular velocity' here
  theta += 0.02;

  // For every x value, calculate a y value with sine function
  float x = theta;
  for (int i = 0; i < yvalues.length; i++) {
    yvalues[i] = sin(x)*amplitude;
    x+=dx;
  }
}

void renderWave() {
 noStroke();
 fill(255);
 // A simple way to draw the wave with an ellipse at each location
 for (int x = 0; x < yvalues.length; x++) {
   ellipse(x*xspacing-xSineOffset, height/2+yvalues[x] - ySineOffset, 16, 16);
 }
}
