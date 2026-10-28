function contea() {
  let caja1="";
  let t1="";
  let c1="";
  let input="";
  let timer=0;
  let time=0;
  let a=0;
  let b=0;
  let c=0;
  let d=0;
  let counta=0;

  if (!timer) {
    timer = setInterval(() => {
     if(time <50){
        a="#p1";
        b="#t1";
        c="#tb1";
        d="consulta1";
       
     }
     else if( time >=50 && time <100){
          a="#p2";
        b="#t2";
        c="#tb2";
       d="consulta2";

      
     }
       else if( time >=100 && time <150){
          a="#p3";
        b="#t3";
        c="#tb3";
       d="consulta3";

      
     }
     else if( time >=150 && time <200){
          a="#p4";
        b="#t4";
        c="#tb4";
       d="consulta4";

      
     }
      else if( time >=100 && time <250){
          a="#p5";
        b="#t5";
        c="#tb5";
       d="consulta5";

      
     }

      time+=50;
      console.log(time)
        caja1= document.querySelector(a);
  c1= document.querySelector(b)
    t1= document.querySelector(c);
    input= document.getElementById(d);
//     if(d != "consulta1" ){
//         if( caja1 != "p1" && caja1.textContent.trim() == ""){
//             counta=0;
//         } else{
//   if(counta ==0){

//    input.value="";
//     counta+=1;

    
//  }
//         }


// }
       if(caja1.textContent.trim() !== ""){
    console.log(caja1.textContent);
        
 console.log(caja1.textContent);
        t1.style.visibility="visible";
        c1.style.height="max-content";
        if(input.value == ""){
        input.value= caja1.textContent;
        }
      
        // if(d != "consulta1"){
        //     counta=0;
        // }
       } else{

t1.style.visibility="hidden";
c1.style.height="30px";
  // setTimeout(()=>{
  //        input.value= input.value;
  //       },10)
}

if(time==(250)){
    time=0;


}
      

    }, 50);


    
  }
}

  
contea();