var canvas = document.querySelector('canvas');
canvas.width= window.innerWidth;
canvas.height=window.innerHeight;
var c = canvas.getContext('2d');

 function Rect(x,y,width,height,dx){
 	this.x=x;
 	this.y=y;
    this.width=width;
    this.height=height;
    this.dx=dx;

 	this.draw= function(){

         c.beginPath();
         c.rect(this.x,this.y,this.width,this.height);
         c.lineWidth= 5;
         c.stroke();
 	}
 	this.update = function(){
	     if(this.width>100 || this.width<20 || this.height<20 ){
	       this.dx= -this.dx;
          }
           this.width += this.dx;
          this.height += this.dx;
          this.draw();
 	}
 }
var rectArray=[];

 for(var i= 0;i<100;i++){
 var x= Math.random()*innerWidth;
var y = Math.random()*innerHeight;
var width=Math.random()*50 + 50;
var height=Math.random()*50 + 50;
var dx= 1

  var rect = new Rect(100,100,75,75,1);
  rectArray.push(new Rect(x,y,width,height,dx));
}

function animate(){
	requestAnimationFrame(animate);
	c.clearRect(0,0,innerWidth,innerHeight);
         // Rect.update();
    for (var i=0;i<rectArray.length;i++){
    	rectArray[i].update();
    }

}

animate();