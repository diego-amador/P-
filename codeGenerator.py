
import subprocess
import os

initialCode = []
variables = {}
sinewaveCode = ["void renderWave() {}"]
circleCode = ["void renderCircle() {}"]
cardioidCode = ["void renderCardiod(){}"]
variables["Amplitude"]= 50
variables ["Frequency"]=500
variables["Radius"] = 20
variables["Radius2"] = 20

radiusCheck = 1


def render(function):
        createInitialCode()
        if(len(function) > 3):
                
                if function[3] == "sin":
                        print(function[3])
                        renderWave()

        if function[0] == "rotate":
                print("cardiod")
                renderCardioid()

        if function[0] == "g": print("Grid")

def updateValue(property,propertyValue):
        global radiusCheck
        if property=="Amplitude":
                variables[property]=propertyValue*5
                
        if property=="Frequency":
                variables[property]=propertyValue*10
                
        if property == "Radius":
                if radiusCheck == 1:
                        variables[property] = propertyValue
                        radiusCheck = -1
                        
                else: 
                        variables["Radius2"] = propertyValue
        print('the attribute :',property,' has a value of ',propertyValue)
                        

        
    
def createInitialCode():
        
    defaultCode =   "Graph graph; \n" \
                    "PFont font; \n" \
                    "PVector pos; \n" \
                    "boolean locked = false; \n" \
                    "float xOffset = 0; \n" \
                    "float yOffset = 0; \n" \
                    "float scale = 1; \n" \
                    "int xspacing = 16;   // How far apart should each horizontal location be spaced \n" \
                    "int w;              // Width of entire wave \n" \
                    "float theta = 0.0;  // Start angle at 0 \n" \
                    "float amplitude = "+str(variables["Amplitude"])+ ";  // Height of wave \n" \
                    "float period = "+str(variables["Frequency"])+ ";  // How many pixels before the wave repeats \n" \
                    "float dx;  // Value for incrementing X, a function of period and xspacing \n" \
                    "float[] yvalues;  // Using an array to store height values for the wave \n" \
                    "//Credit to TimelyToga for the base code for Cardiods\n" \
                        "//https://github.com/TimelyToga/DrawingCardioidsWithProcessing/blob/master/cardioids.pde\n" \
                        "class Point {\n" \
                        "float x;\n" \
                        "float y;\n" \
                        "public Point(float x, float y){\n" \
                        "this.x = x;\n" \
                        "this.y = y;\n" \
                        "  }\n" \
                        "}\n" \
                        "float circleX = 0;\n" \
                        "float circleY = 0; \n" \
                        "int xSize = 0;\n" \
                        "int ySize = 0;\n" \
                        "int xCenter = xSize / 2;\n" \
                        "int yCenter = ySize / 2;\n" \
                        "ArrayList<Point> points;\n" \
                        "float size = 10;\n" \
                        "float radiusMultiplier1 = "+str(variables["Radius"])+ ";\n" \
                        "float radiusMultiplier2 = "+str(variables["Radius2"])+ ";\n" \
                        "float sizeCircle1 = size * radiusMultiplier1; //default\n" \
                        "float sizeCircle2 = size * radiusMultiplier2; //default\n" \
                        "float gridSize = size / 2; // radius of our circles\n" \
                        "float t = 0;\n" \
                    "void setup() { \n" \
                    "fullScreen(); \n" \
                    "font = createFont(\"Consolas\", 50); \n" \
                    "textFont(font, 15); \n" \
                    "pos = new PVector(width/2, height/2); \n" \
                    "textAlign(CENTER); \n" \
                    "graph = new Graph(-1, 0, 10); \n" \
                    "//rectMode(CENTER); \n" \
                    "strokeWeight(2); \n" \
                    "noFill(); \n" \
                    "//SINEWAVE \n" \
                    "w = width+90; \n" \
                    "dx = (TWO_PI / period) * xspacing; \n" \
                    "yvalues = new float[w/xspacing]; \n" \
                    "//END_SINEWAVE \n" \
                        "circleX = float(xSize / 2);\n" \
                        "circleY = float(ySize / 2);\n" \
                        "points = new ArrayList();\n" \
                    "} \n" \
                    "void mousePressed() { \n" \
                    "locked = true; \n" \
                    "xOffset = mouseX-pos.x;  \n" \
                    "yOffset = mouseY-pos.y; \n" \
                    "} \n" \
                    "void mouseDragged() { \n" \
                    "if (locked) { \n" \
                    "    pos.x = mouseX-xOffset;  \n" \
                    "    pos.y = mouseY-yOffset; \n" \
                    "} \n" \
                    "} \n" \
                    "void mouseReleased() { \n" \
                    "locked = false; \n" \
                    "} \n" \
                    "void draw() { \n " \
                    "background(0); \n" \
                    "translate(pos.x, pos.y); \n" \
                    "textSize(20); \n" \
                    "graph.displayGrid(); \n" \
                    "calcWave(); \n" \
                    "renderWave(); \n" \
                    "//renderCircle(); \n" \
                    "renderCardiod();\n" \
                    "} \n" \
                    "class Graph { \n" \
                    "ArrayList<PVector> points = new ArrayList<PVector>(); \n" \
                    "float[] variables = new float[3]; \n" \
                    "float increment = 0.1; //the smaller, the more accurate \n" \
                    "float range = 100; \n" \
                    "float graphincrement = 50; \n" \
                    "float scale = 10; //scaled down by 10 \n" \
                    "Graph(float a, float b, float c) { \n" \
                    "    variables[0] = a; \n" \
                    "    variables[1] = b; \n" \
                    "    variables[2] = c; \n" \
                    "    for (float i = -range; i < range+increment; i += increment) { \n" \
                    "    if ((i > -range*10) && (i < range*10)) { \n" \
                    "        PVector p = new PVector(i, equation(i)); \n" \
                    "        p.mult(scale); \n" \
                    "        points.add(p); \n" \
                    "    } \n" \
                    "    } \n" \
                    "} \n" \
                    "float equation(float n){ \n" \
                    "    //put equation here \n" \
                    "    return -variables[0]*pow(n, 2) - variables[1]*n - variables[2]; \n" \
                    "} \n" \
                    "void displayGrid() { \n" \
                    "    textSize(15); \n" \
                    "    for (float x = -range*10; x < range*10+graphincrement; x += graphincrement) { \n" \
                    "    if (x == 0) { \n" \
                    "        strokeWeight(5); \n" \
                    "        stroke(255, 200); \n" \
                    "    } else { \n" \
                    "        strokeWeight(2); \n" \
                    "        stroke(255, 100); \n" \
                    "    } \n" \
                    "    line(x, -range*10, x, range*10); \n" \
                    "    text(round(x/scale), x, -15); \n" \
                    "    } \n" \
                    "    for (float y = -range*10; y < range*10+graphincrement; y += graphincrement) { \n" \
                    "    if (y == 0) { \n" \
                    "        strokeWeight(5); \n" \
                    "        stroke(255, 200); \n" \
                    "    } else { \n" \
                    "        strokeWeight(2); \n" \
                    "        stroke(255, 100); \n" \
                    "    } \n" \
                    "    line(-range*10, y, range*10, y); \n" \
                    "    text(round(-y/scale), -15, y); \n" \
                    "    } \n" \
                    "} \n" \
                    "} \n" \
                    "void calcWave() { \n" \
                    "// Increment theta (try different values for 'angular velocity' here \n" \
                    "theta += 0.02; \n" \
                    "// For every x value, calculate a y value with sine function \n" \
                    "float x = theta; \n" \
                    "for (int i = 0; i < yvalues.length; i++) { \n" \
                    "    yvalues[i] = sin(x)*amplitude; \n" \
                    "    x+=dx; \n" \
                    "} \n" \
                    "} \n" 
   
    initialCode.append(defaultCode)

def renderWave():
       
        swc = "void renderWave() { \n" \
                    "noStroke(); \n" \
                    "fill(255); \n" \
                    "// A simple way to draw the wave with an ellipse at each location \n" \
                    "for (int x = 0; x < yvalues.length; x++) { \n" \
                    "ellipse(x*xspacing-width/2, height/2+yvalues[x] - height/2, 16, 16); \n" \
                    "} } " \
                    
        sinewaveCode[0] = swc

def renderCardioid():

        cc =    "void renderCardiod(){\n" \
                "//Credit to TimelyToga for the base code for Cardiods\n" \
                "//https://github.com/TimelyToga/DrawingCardioidsWithProcessing/blob/master/cardioids.pde\n" \
                "// Draw axes\n" \
                "stroke(190);\n" \
                "strokeWeight(2);\n" \
                "line(0, ySize / 2, xSize, ySize / 2);\n" \
                "line(xSize / 2, 0, xSize / 2, ySize);\n" \
                "int curXLine = 1;\n" \
                "while(curXLine * gridSize <= xSize){\n" \
                "float xDelta = curXLine * gridSize;\n" \
                "line(xCenter + xDelta, 0, xCenter + xDelta, ySize);\n" \
                "line(xCenter - xDelta, 0, xCenter - xDelta, ySize);\n" \
                "curXLine++;\n" \
                "}\n" \
                "int yL = 1;\n" \
                "while(yL * gridSize <= ySize){\n" \
                "float yD = yL * gridSize;\n" \
                "line(0, yCenter + yD, xSize, yCenter + yD);\n" \
                "line(0, yCenter - yD, xSize, yCenter - yD);\n" \
                "yL++;\n" \
                "}\n" \
                "// Calculate cur position of rotating circle\n" \
                "float xOffset = sizeCircle1 * cos(t);\n" \
                "float yOffset = sizeCircle1 * sin(t);\n" \
                "float x = circleX + xOffset;\n" \
                "float y = circleY + yOffset;\n" \
                "// Draw center circle\n" \
                "stroke(18, 185, 204);\n" \
                "strokeWeight(3);\n" \
                "noFill();\n" \
                "ellipse(circleX, circleY, sizeCircle1 - 3, sizeCircle1 - 3);\n" \
                "// Draw rotating circle\n" \
                "noStroke();\n" \
                "fill(232, 152, 118);\n" \
                "ellipse(x, y, sizeCircle2, sizeCircle2);\n" \
                "// Add a new drawing point\n" \
                "float dx = x - (sizeCircle2 / 2.0) * cos(2*t);\n" \
                "float dy = y - (sizeCircle2 / 2.0) * sin(2*t);\n" \
                "points.add(new Point(dx, dy));\n" \
                "//Draw rotation line\n" \
                "strokeWeight(3);\n" \
                "stroke(252, 222, 168);\n" \
                "line(x, y, dx, dy);\n" \
                "// Draw our cardioid\n" \
                "stroke(214, 79, 21);\n" \
                "strokeWeight(3);\n" \
                "noFill();\n" \
                "beginShape();\n" \
                "for(Point p: points){\n" \
                "curveVertex(p.x, p.y);\n" \
                "}\n" \
                "endShape();\n" \
                "// Timestep\n" \
                "t += 0.03;\n" \
                "if(t >= 2 * 3.14159) {\n" \
                "t = 0;\n" \
                "// If we have rotated once, stop animating\n" \
                "//noLoop();\n" \
                "}\n" \
                "}\n" \

        cardioidCode[0] = cc


        
def run():
    finalCode = initialCode[0]
    finalCode += sinewaveCode[0]
    finalCode += cardioidCode[0]
    #finalCode += circleCode[0]    
    #finalCode += "\n } "

    filePath = "PPP/PPP.pde"
    ProcessingCode = open(filePath, 'w')
    ProcessingCode.write(finalCode)
    ProcessingCode.close()
    os.system("processing-java --sketch=PPP  --present")
    

def cleanUpload():
        os.system( "upload clean")
        
