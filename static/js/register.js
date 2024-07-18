

let yourname;

function your_name(){
    const name = document.getElementById("username")
    yourname = name.value
    localStorage.setItem('yourname', yourname);
    console.log(yourname)

    
    
}
