$(document).ready(function() {
    var add = $("#add");
    var sub = $("#sub");
    var mul = $("#mul");
    var div = $("#div");
    var reset = $("#reset");

    add.click(function() {
        console.log('Add clicked');
        var a = parseFloat($("#num1").val());
        var b = parseFloat($("#num2").val());
        if (isNaN(a) || isNaN(b)) {
            alert("Enter a valid number");
            return;
        }
        var c = $("#result");
        c.val(a + b);
        c.css('display','block')
    });

    sub.click(function() {
        console.log('Subtract clicked');
        var a = parseFloat($("#num1").val());
        var b = parseFloat($("#num2").val());
        if (isNaN(a) || isNaN(b)) {
            alert("Enter a valid number");
            return;
        }
        var c = $("#result");
        c.val(a - b);
        c.css('display','block');
    });

    mul.click(function() {
        console.log('Multiply clicked');
        var a = parseFloat($("#num1").val());
        var b = parseFloat($("#num2").val());
        if (isNaN(a) || isNaN(b)) {
            alert("Enter a valid number");
            return;
        }
        var c = $("#result");
        c.val(a * b);
        c.css('display','block');
    });

    div.click(function() {
        console.log('Divide clicked');
        var a = parseFloat($("#num1").val());
        var b = parseFloat($("#num2").val());
        if (isNaN(a) || isNaN(b)) {
            alert("Enter a valid number");
            return;
        }
        var c = $("#result");
        c.val(a / b);
        c.css('display','block');
    });

    reset.click(function() {
        console.log('Reset clicked');
        $("#num1").val("");
        $("#num2").val("");
        $("#result").css('display','none');
        $("#num1").focus();
    });
});


