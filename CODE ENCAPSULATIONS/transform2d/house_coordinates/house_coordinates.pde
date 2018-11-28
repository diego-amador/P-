size(400,400); // GRID SIZE HERE
background(0);
strokeWeight(4);
stroke(250);
fill(127);

for(int y=0;y<height;y=y+20){
for (int x=0;x<width;x=x+20){
    rect(x,y,20,20);
}
}
