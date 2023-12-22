const bar = document.getElementById('bar');
$(document).ready(function() {
    $('#uploadButton').on('click', function() {
        alert("请留在当前页面等待上传成功")
        const formData = new FormData();
        const imageInputs = $('#image-input')[0].files;
        for (let i = 0; i < imageInputs.length; i++) {
            formData.append('image', imageInputs[i]);
        }
        formData.append('text', $('#text-input').val());
        bar.style.display = 'block';
        $.ajax({
            url: '/up_load/',
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            xhr: function() {
                const xhr = new window.XMLHttpRequest();
                xhr.upload.addEventListener('progress', function(e) {
                    if (e.lengthComputable) {
                        const percent = Math.round((e.loaded / e.total) * 100);
                        $('.progress-bar').css('width', percent + '%').text(percent + '%' + '...请不要退出页面');
                    }
                });
                return xhr;
                },
            success: function(data) {
                $('.progress-bar').text('上传完成');
            }
        });
    });
});