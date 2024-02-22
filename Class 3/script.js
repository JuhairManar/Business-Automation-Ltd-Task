// console.log(a);

var add=document.getElementById("add");
var sub=document.getElementById("sub");
var mul=document.getElementById("mul");
var div=document.getElementById("div");
var reset=document.getElementById("reset");


add.addEventListener('click',function(){
    console.log('Add clicked');
    var a=parseFloat(document.getElementById("num1").value);
    var b=parseFloat(document.getElementById("num2").value);
    if(isNaN(a) || isNaN(b))
    {
        alert("Enter a valid number");
        return ;
    }
    var c=document.getElementById("result");
    c.value=a+b;
    c.style.display="block";
})

sub.addEventListener('click',function(){
    console.log('Add clicked');
    var a=parseFloat(document.getElementById("num1").value);
    var b=parseFloat(document.getElementById("num2").value);
    if(isNaN(a) || isNaN(b))
    {
        alert("Enter a valid number");
        return ;
    }
    var c=document.getElementById("result");
    c.value=a-b;
    c.style.display="block";
})

mul.addEventListener('click',function(){
    console.log('Add clicked');
    var a=parseFloat(document.getElementById("num1").value);
    var b=parseFloat(document.getElementById("num2").value);
    if(isNaN(a) || isNaN(b))
    {
        alert("Enter a valid number");
        return ;
    }
    var c=document.getElementById("result");
    c.value=a*b;
    c.style.display="block";
})

div.addEventListener('click',function(){
    console.log('Add clicked');
    var a=parseFloat(document.getElementById("num1").value);
    var b=parseFloat(document.getElementById("num2").value);
    if(isNaN(a) || isNaN(b))
    {
        alert("Enter a valid number");
        return ;
    }
    var c=document.getElementById("result");
    c.value=a/b;
    c.style.display="block";
})

reset.addEventListener('click',function(){
    console.log('clicked');
    document.getElementById("num1").value="";
    document.getElementById("num2").value="";
    document.getElementById("result").style.display="none";
    document.getElementById("num1").focus();
})