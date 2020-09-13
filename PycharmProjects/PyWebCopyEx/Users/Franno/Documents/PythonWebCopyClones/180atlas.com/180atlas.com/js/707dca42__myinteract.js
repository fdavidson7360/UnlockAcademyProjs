/* The dragging code for '.draggable' from the demo above
 * applies to this demo as well so it doesn't have to be repeated. */

document.getElementById('northOverview').style.visibility = "hidden"
document.getElementById('eastOverview').style.visibility = "hidden"
document.getElementById('southOverview').style.visibility = "hidden"
document.getElementById('westOverview').style.visibility = "hidden"
document.getElementById('opaqueBackground').style.visibility = "hidden"
document.getElementById('exitOverview').style.visibility = "hidden"

 // target elements with the "draggable" class
interact('.draggable')
.draggable({
  // enable inertial throwing
  inertia: true,
  // keep the element within the area of it's parent
  restrict: { //http://interactjs.io/docs/restriction/ 
    restriction: "parent",
    endOnly: false,
    elementRect: { top: 0.42, left: 0.32, bottom: 0.55, right: 0.45 }   // counter clockwise
},

// restrict: {  This way will allow for auto dragging back to the middle.
//     restriction: "parent",
//     endOnly: true,
//     elementRect: { top: 0.13, left: -0.45, bottom: 0.90, right: 1.5 } 
// },
  // enable autoScroll
  autoScroll: false,

  // call this function on every dragmove event
  onmove: dragMoveListener,
  // call this function on every dragend event
  onend: function (event) {
   console.log('on end')
  },
  ondrop: function (event) {
    console.log("on drop")
    var target = event.target,
    // keep the dragged position in the data-x/data-y attributes
    x = (parseFloat(target.getAttribute('data-x')) || 0) + event.dx,
    y = (parseFloat(target.getAttribute('data-y')) || 0) + event.dy;
    if(y < -25 ){ //going North
        alert("dropped in north")
    }
  },


});

function dragMoveListener (event) {
    scrollToAnchor();
  var target = event.target,
      // keep the dragged position in the data-x/data-y attributes
      x = (parseFloat(target.getAttribute('data-x')) || 0) + event.dx,
      y = (parseFloat(target.getAttribute('data-y')) || 0) + event.dy;
      if(y < -25 ){ //going North
        // console.log("y: "+y);
        document.getElementById('compassOverview').style.visibility = "hidden"
        
        document.getElementById('northOverview').style.visibility = "visible"
        document.getElementById('eastOverview').style.visibility = "hidden"
        document.getElementById('southOverview').style.visibility = "hidden"
        document.getElementById('westOverview').style.visibility = "hidden"
        document.getElementById('opaqueBackground').style.visibility = "visible"
        

        document.getElementById('northWrapper').style.visibility = "visible"
        document.getElementById('eastWrapper').style.visibility = "hidden"
        document.getElementById('southWrapper').style.visibility = "hidden"
        document.getElementById('westWrapper').style.visibility = "hidden"

        document.getElementById('exitOverview').style.visibility = "visible"
        
        document.getElementById('compassExplanation').style.visibility = "hidden"
        
    }
      else if(y > 20 ){ //going South
        // console.log("y: "+y)
        document.getElementById('compassOverview').style.visibility = "hidden"
        
        document.getElementById('northOverview').style.visibility = "hidden"
        document.getElementById('eastOverview').style.visibility = "hidden"
        document.getElementById('southOverview').style.visibility = "visible"
        document.getElementById('westOverview').style.visibility = "hidden"
        document.getElementById('opaqueBackground').style.visibility = "visible"

        document.getElementById('northWrapper').style.visibility = "hidden"
        document.getElementById('eastWrapper').style.visibility = "hidden"
        document.getElementById('southWrapper').style.visibility = "visible"
        document.getElementById('westWrapper').style.visibility = "hidden"

        document.getElementById('exitOverview').style.visibility = "visible"
        document.getElementById('compassExplanation').style.visibility = "hidden"
        
        
      }
      else if(x < -20){ //going West
        console.log("x: "+x)
        document.getElementById('compassOverview').style.visibility = "hidden"
        document.getElementById('northOverview').style.visibility = "hidden"
        document.getElementById('eastOverview').style.visibility = "hidden"
        document.getElementById('southOverview').style.visibility = "hidden"
        document.getElementById('westOverview').style.visibility = "visible"
        document.getElementById('opaqueBackground').style.visibility = "visible"

        document.getElementById('northWrapper').style.visibility = "hidden"
        document.getElementById('eastWrapper').style.visibility = "hidden"
        document.getElementById('southWrapper').style.visibility = "hidden"
        document.getElementById('westWrapper').style.visibility = "visible"

        document.getElementById('exitOverview').style.visibility = "visible"
        
        document.getElementById('compassExplanation').style.visibility = "hidden"
        

      }else if(x > 20){ //going East
        console.log("x: "+x)
        document.getElementById('compassOverview').style.visibility = "hidden"
        document.getElementById('northOverview').style.visibility = "hidden"
        document.getElementById('eastOverview').style.visibility = "visible"
        document.getElementById('southOverview').style.visibility = "hidden"
        document.getElementById('westOverview').style.visibility = "hidden"
        document.getElementById('opaqueBackground').style.visibility = "visible"
        
        document.getElementById('northWrapper').style.visibility = "hidden"

        document.getElementById('northWrapper').style.visibility = "hidden"
        document.getElementById('eastWrapper').style.visibility = "visible"
        document.getElementById('southWrapper').style.visibility = "hidden"
        document.getElementById('westWrapper').style.visibility = "hidden"
        document.getElementById('exitOverview').style.visibility = "visible"
        
        document.getElementById('compassExplanation').style.visibility = "hidden"
        
        
    
      }else{
          console.log('hide all') 
          resetAll();         
          
      }

      
      
  // translate the element
  target.style.webkitTransform =
  target.style.transform =
    'translate(' + x + 'px, ' + y + 'px)';

  // update the posiion attributes
  target.setAttribute('data-x', x);
  target.setAttribute('data-y', y);
}

// this is used later in the resizing and gesture demos
window.dragMoveListener = dragMoveListener;
var innerCircleInitialPosition;
$(document).ready(function(){
    var innerCircle = $( "#compass_3d_inner_circle" )
    innerCircleInitialPosition = innerCircle.offset();
    console.log($( "#compass_3d_inner_circle" ).css("left"))
    
    $(".exitOverview").click(function(){
        resetAll();
        // $( "#compass_3d_inner_circle" ).css({"left":innerCircleInitialPosition.left})
        // $( "#compass_3d_inner_circle" ).css({"top":innerCircleInitialPosition.top})
        
    })
   
});

function resetAll(){
    document.getElementById('compassOverview').style.visibility = "visible"
    document.getElementById('northOverview').style.visibility = "hidden"
    document.getElementById('eastOverview').style.visibility = "hidden"
    document.getElementById('southOverview').style.visibility = "hidden"
    document.getElementById('westOverview').style.visibility = "hidden"
    document.getElementById('opaqueBackground').style.visibility = "hidden"


    document.getElementById('northWrapper').style.visibility = "visible"
    document.getElementById('eastWrapper').style.visibility = "visible"
    document.getElementById('southWrapper').style.visibility = "visible"
    document.getElementById('westWrapper').style.visibility = "visible" 
    document.getElementById('exitOverview').style.visibility = "hidden"

    document.getElementById('compassExplanation').style.visibility = "visible"
    
    
}

function scrollToAnchor(){
    console.log("dfhldj")
    var aTag = $("div[name='topOfCompass']");
    // $('html,body').animate(...)
    
    // $('html,body').stop(true, false).animate({scrollTop: aTag.offset().top - 50},100);
}


/////////////////////////////////////////////////////////////////////////////

// enable draggables to be dropped into this
// interact('#northOverview').dropzone({

//     // only accept elements matching this CSS selector
//     accept: '#compass_3d_inner_circle',
//     // Require a 75% element overlap for a drop to be possible
//     overlap: 0.15,
  
//     // listen for drop related events:
  
//     ondropactivate: function (event) {
//         var target = event.target,
//         // keep the dragged position in the data-x/data-y attributes
//         x = (parseFloat(target.getAttribute('data-x')) || 0) + event.dx,
//         y = (parseFloat(target.getAttribute('data-y')) || 0) + event.dy;
        
//         // debugger;
//         console.log("dropactivated")
//       // add active dropzone feedback
//       event.target.classList.add('drop-active');
      
//     },
//     ondragenter: function (event) {
//       var draggableElement = event.relatedTarget,
//           dropzoneElement = event.target;
  
//       // feedback the possibility of a drop
//       dropzoneElement.classList.add('drop-target');
//       draggableElement.classList.add('can-drop');
//       draggableElement.textContent = 'Dragged in';

//       console.log("entereed")
      
//     },
//     ondragleave: function (event) {
//       // remove the drop feedback style
//       event.target.classList.remove('drop-target');
//       event.relatedTarget.classList.remove('can-drop');
//       event.relatedTarget.textContent = 'Dragged out';
//       console.log("drag leave")
//     },
//     ondrop: function (event) {
//         var target = event.target,
//         // keep the dragged position in the data-x/data-y attributes
//         x = (parseFloat(target.getAttribute('data-x')) || 0) + event.dx,
//         y = (parseFloat(target.getAttribute('data-y')) || 0) + event.dy;
//         console.log("dropped")
//         debugger;
        
//       event.relatedTarget.textContent = 'Dropped';
//     },
//     ondropdeactivate: function (event) {
//       // remove active dropzone feedback
//       var target = event.target,
//       // keep the dragged position in the data-x/data-y attributes
//       x = (parseFloat(target.getAttribute('data-x')) || 0) + event.dx,
//       y = (parseFloat(target.getAttribute('data-y')) || 0) + event.dy;


//     //   debugger;
//       event.target.classList.remove('drop-active');
//       event.target.classList.remove('drop-target');

//       console.log("dropdeactivated")
      
//     }

//   });
/*!
* AerWebCopy Engine [version 6.3.0]
* Copyright Aeroson Systems & Co.
* File mirrored from https://180atlas.com/js/myinteract.js
* At UTC time: 2020-06-22 07:37:21.015092
*/
