const wrapper   = document.querySelector(".wrapper");
const btnPopup  = document.querySelector(".btnLogin-popup");
const closedBtn = document.querySelector(".icon-close");

btnPopup.addEventListener("click", ()=>{
    wrapper.classList.toggle("active-popup");
})

closedBtn.addEventListener("click", ()=>{
    wrapper.classList.remove("active-popup")
})