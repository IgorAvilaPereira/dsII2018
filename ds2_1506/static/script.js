function loadXMLDoc() {
    var req = new XMLHttpRequest();

    req.onreadystatechange = function() {
        if (req.readyState == 4){
            if (req.status == 200){
                var response = JSON.parse(req.responseText);
                document.getElementById('myDiv').innerHTML = response.username;
            }
        }
    }
    
    req.open('POST', '/ajax');
    req.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    var un = document.getElementById('scname').value;
    var sec = document.getElementById('secret').value;
    var postVars = 'username='+un+'&secret='+sec;
    req.send(postVars);        
    return false;
}


 function ajax_igor() {
        var req = new XMLHttpRequest();        
        req.onreadystatechange = function() {        
            if (req.readyState == 4){
                if (req.status == 200){
                    // var response = JSON.parse(req.responseText);
                    document.getElementById('buscaResultado').innerHTML = req.responseText;
                }
            }
        }
        
        req.open('POST', '/ajax_igor');
        req.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        var campo = document.getElementById('busca').value;
        var postVars = 'campo='+campo;
        req.send(postVars);        
        return false;
}