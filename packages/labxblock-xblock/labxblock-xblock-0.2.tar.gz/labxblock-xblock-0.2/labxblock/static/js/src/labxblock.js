function LabXBlock(runtime, element) {

    let createdInputType = '';
    const  usageId =element.getAttribute('data-usage-id')

    $.ajax({
        type: "GET",
        url: runtime.handlerUrl(element, 'lab'),
        success: function(data) {
                // console.log(data)
               if (data.block_id == usageId){
                const labElement = $(element).find('.lab');
                if (labElement.length > 0) {
                    const inputHtml = `<input type="${data.type}" id="input"/>`;
                    labElement.append(inputHtml);
                    createdInputType = data.type;
                    viewResult(data);
                }

               }   
        }
    });


 

    function viewResult(data) {
        const link = data.url;
        const result_lab = data.result
        if (link.length > 0) {
            const text = `
                <div>
                    <a href='${link}' target='_blank'>Download</a>
                    <p>Result: ${result_lab}</p>
                </div>`;
            $(".form-upload", element).css("display", "none");
            $(".labfunix_block", element).html(text);
        }
        else if (data.result_student){
            const text = `
                <div>
                    <p>student result: ${data.result_student}</p>
                    <p>Result: ${result_lab}</p>
                </div>`;
            $(".form-upload", element).css("display", "none");
            $(".labfunix_block", element).html(text);
        }
    }

    $('#btn-submit', element).click(function (event){
        event.preventDefault();
        if (createdInputType == 'file'){
            const fileInput = $('#input', element)[0].files[0];
            if (fileInput) {
                const formData = new FormData();
                formData.append("file", fileInput);
                formData.append('type', 'lab');
                $.ajax({
                    type: "POST",
                    url: runtime.handlerUrl(element, 'upload'),
                    contentType: false,
                    processData: false,
                    data: formData,
                    success: viewResult
                });
               
            } else {
                console.log('No file selected');
            }
        }
        else if (createdInputType == 'text'){
            const text = $('#input', element).val();
            const formData = new FormData();
            formData.append("text", text);
            formData.append('type', 'lab');
            $.ajax({
                type: "POST",
                url: runtime.handlerUrl(element, 'lab_text'),
                contentType: false,
                processData: false,
                data: formData,
                success: function (data){
                    if (data.result_student){
                        const result_lab = data.result
                        const text = `
                            <div>
                                <p>student result: ${data.result_student}</p>
                                <p>Result: ${result_lab}</p>
                            </div>`;
                        $(".form-upload", element).css("display", "none");
                        $(".labfunix_block", element).html(text);
                    }
                }
            });
        }
      
    })
    

}