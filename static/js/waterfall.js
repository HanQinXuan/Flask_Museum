window.onload = function () {
    waterFall();

               let container = document.getElementById("con");

               document.onscroll = throttle(function(){
                   let item = document.getElementsByClassName("item");
                   if(item[item.length - 1].getBoundingClientRect().top < window.innerHeight){
                       for(let i = 0 ; i < item.length ; i++){
                           item[i].className = "item";
                       }
                       for(let i = 0 ; i < 5 ; i++){
                           for(let i = 1 ; i <= 4 ; i++){
                               container.innerHTML += `
                                             <div class="item show">
                                                 <div class="picture">
                                                     <img src="${i}.jpg" alt="">
                                                 </div>
                                             </div>
                                `;
                           }
                       }
                       waterFall();
                   }
               },1000);

               window.onresize = throttle(function () {
                   waterFall();
               },300);
           };


           function throttle(callback,delay) {
                 let flag = true;
                 return function () {
                      if(flag){
                          flag = false;
                          setTimeout( ()=> {
                             callback.bind(this)();
                             flag = true;
                          },delay);
                      }
                 }
           }

           function waterFall() {
                    // 1. 设置container盒子的宽度
                    //     注意:   浏览器的可视区域的宽度 / 一个item元素的宽度  =  一行的排列的元素的个数
                    //     注意：  一行的排列的元素的个数 * 一个item元素的宽度
                    let container = document.getElementById("con");
                    let item = document.getElementsByClassName("item");
                    let clientWidth = document.documentElement.clientWidth;
                    let columnCount = Math.floor(clientWidth / item[0].offsetWidth);
                    container.style.width = columnCount * item[0].offsetWidth + "px";


                    // 2. 设置每一个item元素的排列位置
                    //     第一行整体的top值都是0   后面的一次找上一行高度最小的容器 在它的下面进行排列
                    let hrr = []; // 存每一行盒子的高度
                    for(let i = 0 ; i < item.length; i++){
                              if(i < columnCount){
                                  item[i].style.top = "0px";
                                  item[i].style.left = i * item[0].offsetWidth + "px";
                                  hrr.push(item[i].offsetHeight);
                              //    第一行
                              }else{
                               // 第一行之后的
                                  let min = Math.min(...hrr);
                                  let index = hrr.indexOf(min);
                                  item[i].style.top = min + "px";
                                  item[i].style.left = index * item[0].offsetWidth + "px";
                                  hrr[index] += item[i].offsetHeight;
                              }
                    }
           }