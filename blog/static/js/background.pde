		void setup() {
		  size(1080,720,P3D);
		}

		void draw() {
		  background(0);
		  pushMatrix();
		  translate(width/2, height/2, -height/2);
		  noFill();
		  stroke(102, 93, 82);
		  sphere(height);
		  popMatrix();
		}

		void mouseOver() {
		  camera(mouseX, height/2, (height/2) / tan(PI/6), width/2, height/2, 1, 1, 1, 0);
		}
