function setup() {
  createCanvas(windowWidth, windowHeight);
  background(100);

}

function draw() {
  //draw grid at 10px spacing
  stroke(200,200,200);
  for (var x = 0; x < windowWidth; x+=10) {
    line(x,0,x,windowHeight);
  }
  for (var y = 0; y < windowHeight; y+=10) {
    line(0,y,windowWidth,y);
  }
  //draw axes
  strokeWeight(3); //same color as grid but thicker
  line(0,windowHeight/2,windowWidth,windowHeight/2);
  line(windowWidth/2,0,windowWidth/2,windowHeight);
  
  //draw plotted lines
  stroke(255, 0, 0); //red to stand out
  //x=40 (vertical line)
  for (var y = -windowHeight/2; y < windowHeight/2; y++) {
    x = 40;
    point(x+windowWidth/2,y+windowHeight/2);
  }
  
  for (var x = 0; x < windowWidth; x++) { 
    y = windowHeight/2-100;
    point(x,windowHeight/2-y);
    //println(x);
  }
  /*for(var x = -windowWidth/2; x < windowWidth/2; x++) {
    y = -(2*x + 20);
    point(x+windowWidth/2,y+windowHeight/2);
  }*/

  //drawing a plotted parabola is a little tougher without using
  //dedicated functions; I use a variable to hold the previous 
  //value for each coordinate and draw a tiny line between each 
  //point for each value of x that would appear.  Would be less
  //costly to determine only those that exist in the drawn plane,
  //but that's an exercise for another day.
  var prevX, prevY;
  for(var x = -windowWidth/2; x < windowWidth/2; x++) {
    y = -(pow(x,2)+2*x+1);
    if (prevY !== undefined) {
        line(prevX+windowWidth/2,prevY+windowHeight/2,x+windowWidth/2,y+windowHeight/2);
    }
    prevX = x;
    prevY = y;
    point(x+200,y+200);
  }

}
