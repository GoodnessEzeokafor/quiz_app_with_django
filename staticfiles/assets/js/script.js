var forms = document.forms[0];
var txt = "";
var i;
for (i =0; i < forms.length ; i++){
    if(forms[i].checked){
        txt = txt + forms[i].value + " ";
    }
}

document.getElementById("order").value = `You selected % ${txt}`;
console.log(`You selected % ${txt}`);
console.log(forms);
