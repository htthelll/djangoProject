document.addEventListener('DOMContentLoaded', function() {
    const downloadButtons = document.querySelectorAll('.download-button');

    downloadButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            const markerId = button.getAttribute('data-marker-id');
            const downloadUrl = `/download_marker_images/${markerId}/`;
            alert("即将开始下载")
            // Create a temporary link to trigger the download
            const link = document.createElement('a');
            link.href = downloadUrl;
            link.download = `${markerId}_data.zip`;
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        });
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const detectButtons = document.querySelectorAll('.detect-button');

    detectButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            const markerId = button.getAttribute('data-marker-id');

            fetch('/detect_marker_images/' + markerId + '/')
                .then(response => {
                    if (!response.ok) {
                        throw new Error('请求失败');
                    }
                    return response.json();
                })
                .then(data => {
                    alert('已开始识别，请稍后来查看');
                    //alert后刷新页面
                    location.reload();
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        });
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const deleteButtons = document.querySelectorAll('.delete-button');

    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            const markerId = button.getAttribute('data-marker-id');

            fetch('/delete_marker_images/' + markerId + '/')
                .then(response => {
                    if (!response.ok) {
                        throw new Error('请求失败');
                    }
                    return response.json();
                })
                .then(data => {
                    alert('已删除！');
                    //alert后刷新页面
                    location.reload();
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        });
    });
});
