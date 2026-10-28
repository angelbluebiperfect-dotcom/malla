let activa=0
  let boton= document.querySelector("#btn");
let latera= document.querySelector("#gen");
let px = 1000;
let mediaQuery  = window.matchMedia('(max-width:' + px + 'px)');
function presiona(){

 console.log("presionado");
  setTimeout(()=>{
     boton.style.opacity=0;
          boton.style.visibility="hidden";
  },300)
  setTimeout(()=>{
     latera.style.visibility="visible";
     latera.style.opacity=1;
  },200)
}
function regresa(){
setTimeout(()=>{
         boton.style.opacity=1;
          boton.style.visibility="visible";
     latera.style.visibility="hidden";
     latera.style.opacity=0;
  },200)


}
function comprobarResolucion(e) {
  if (e.matches) {
    boton.style.opacity=1;
    boton.style.visibility="visible";

  
  } else {
    boton.style.opacity=0;
    boton.style.visibility="hidden";

    latera.style.opacity=0;
    latera.style.visibility="hidden";
  }
}

function contea() {
  let timer;
  mediaQuery.addEventListener('change', comprobarResolucion);

  if (!timer) {
    timer = setInterval(() => {
      comprobarResolucion(mediaQuery);

    }, 100);


    
  }
}
contea();