

function runScript(){
    $.ajax({
        method: 'POST',
        processData: false,
        contentType: false,
        mimeType: "multipart/form-data",
        url: 'gerar_pagamento',
        data: data,
        success: function(response) {
            console.log('Yeah! Your data were sent and saved!');
        }
    })
  }

  

